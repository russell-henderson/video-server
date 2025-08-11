# backend/app/core/config.py
from __future__ import annotations

import os
import ipaddress
from dataclasses import dataclass, field
from datetime import datetime, time
from pathlib import Path
from typing import List, Tuple

import yaml

try:
    from meilisearch import Client as MeiliClient  # type: ignore
except Exception:  # pragma: no cover
    MeiliClient = None  # type: ignore


# --------- Data models ---------
@dataclass
class Paths:
    images_root: str
    videos_root: str
    cache_root: str
    backups_root: str

@dataclass
class Server:
    host: str = "0.0.0.0"
    port: int = 8080
    https: bool = True
    cert_path: str = "config/https/server.crt"
    key_path: str = "config/https/server.key"

@dataclass
class Search:
    meili_host: str = "http://127.0.0.1:7700"
    refresh_interval_active_s: int = 10

@dataclass
class Jobs:
    broker_url: str = "redis://127.0.0.1:6379/0"
    max_workers: int = 3
    quiet_hours: str = "01:00-06:00"  # HH:MM-HH:MM local time

@dataclass
class Thumbnails:
    sizes: List[int] = field(default_factory=lambda: [256, 512, 1024])
    video_poster_width: int = 1280
    cache_cap_gb: int = 50

@dataclass
class AI:
    local_first: bool = True
    openai_fallback: bool = False
    max_concurrent_jobs: int = 2

@dataclass
class VideoTranscode:
    enable_smart: bool = True
    max_bitrate_mbps: int = 15
    codec: str = "hevc"
    container: str = "mp4"

@dataclass
class VideoSubtitles:
    default_font_family: str = "Merriweather"
    default_font_size_pt: int = 18

@dataclass
class Video:
    transcode: VideoTranscode = field(default_factory=VideoTranscode)
    subtitles: VideoSubtitles = field(default_factory=VideoSubtitles)

@dataclass
class Security:
    lan_only: bool = True
    ip_allowlist: List[str] = field(default_factory=list)

@dataclass
class Retention:
    trash_days: int = 60
    logs_days: int = 90
    logs_max_mb: int = 500

@dataclass
class Settings:
    paths: Paths
    server: Server
    search: Search
    jobs: Jobs
    thumbnails: Thumbnails
    ai: AI
    video: Video
    security: Security
    retention: Retention

    # Convenience objects (initialized at runtime)
    meili: object | None = None

    def quiet_hours_window(self) -> Tuple[time, time]:
        start_s, end_s = self.jobs.quiet_hours.split("-")
        h1, m1 = map(int, start_s.split(":"))
        h2, m2 = map(int, end_s.split(":"))
        return time(h1, m1), time(h2, m2)

    def in_quiet_hours(self, now: datetime | None = None) -> bool:
        now = now or datetime.now()
        start, end = self.quiet_hours_window()
        t = now.time()
        return (t >= start) or (t < end) if start > end else (start <= t < end)

    def is_ip_allowed(self, ip: str) -> bool:
        # If explicit allowlist exists, enforce it strictly
        if self.security.ip_allowlist:
            return any(_cidr_match(ip, cidr) for cidr in self.security.ip_allowlist)
        # Otherwise, if lan_only=True, allow RFC1918 + loopback ranges only
        if self.security.lan_only:
            return any(
                ipaddress.ip_address(ip) in ipaddress.ip_network(cidr)
                for cidr in ("127.0.0.0/8", "10.0.0.0/8", "172.16.0.0/12", "192.168.0.0/16")
            )
        return True

    def ensure_runtime_dirs(self) -> None:
        for p in (self.paths.cache_root, self.paths.backups_root):
            Path(p).mkdir(parents=True, exist_ok=True)

    def init_meili(self) -> None:
        if MeiliClient is None:
            return
        try:
            self.meili = MeiliClient(self.search.meili_host)
            # Touch the server to validate connection (won't raise on newer clients, but safe)
            _ = self.meili.health()  # type: ignore[attr-defined]
        except Exception:
            self.meili = None


# --------- Loaders & helpers ---------
_DEFAULT_CONFIG_PATH = os.environ.get("MEDIA_SERVER_CONFIG", "config/server.yaml")


def load_settings(config_path: str | os.PathLike[str] = _DEFAULT_CONFIG_PATH) -> Settings:
    with open(config_path, "r", encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}

    paths = Paths(**raw.get("paths", {}))
    server = Server(**raw.get("server", {}))
    search = Search(**raw.get("search", {}))
    jobs = Jobs(**raw.get("jobs", {}))
    thumbnails = Thumbnails(**raw.get("thumbnails", {}))
    ai = AI(**raw.get("ai", {}))
    video = Video(
        transcode=VideoTranscode(**raw.get("video", {}).get("transcode", {})),
        subtitles=VideoSubtitles(**raw.get("video", {}).get("subtitles", {})),
    )
    security = Security(**raw.get("security", {}))
    retention = Retention(**raw.get("retention", {}))

    settings = Settings(
        paths=paths,
        server=server,
        search=search,
        jobs=jobs,
        thumbnails=thumbnails,
        ai=ai,
        video=video,
        security=security,
        retention=retention,
    )
    return settings


def _cidr_match(ip: str, cidr: str) -> bool:
    try:
        return ipaddress.ip_address(ip) in ipaddress.ip_network(cidr, strict=False)
    except Exception:
        return False

# Module-level singleton (loaded by app.main)
settings: Settings | None = None


def get_settings() -> Settings:
    global settings
    if settings is None:
        settings = load_settings()
    return settings