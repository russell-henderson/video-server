`V:\video-server` that matches everything you chose.

# **High‑level spec (concise)**

* **Platform**: FastAPI backend \+ React/Vite frontend \+ PWA.

* **Sources**: Images `G:\Dev`, Videos `V:\local-video-server\videos`.

* **Search**: Meilisearch. SQLite for core DB, JSON sidecars for tags/captions.

* **Jobs**: Celery \+ Redis. Quiet hours 1:00–6:00. Max workers 3\.

* **AI**: Local-first (CLIP/ViT embeddings, lightweight detectors). Optional OpenAI fallback. Max concurrent AI jobs 2\.

* **Thumbnails**: 256, 512, 1024 px; video posters 1280 px. WEBP/JPEG. Cache cap 50 GB at `V:\video-server\cache`.

* **Playback**: Direct play first. Smart transcode with FFmpeg \+ NVENC. 4K max 15 Mbps. MP4 HEVC. SRT/ASS/VTT styling.

* **VR focus**: Quest 2 multi‑platform optimized UI. Controllers first, hand tracking optional. Split Panel \+ Gallery cues.

* **UX**: Adaptive UI, switchable view modes, segmented infinite scroll, Glass & Glow styling, dynamic ambient backdrops, theme variations.

* **Smart**: Auto‑tag, hybrid search, duplicate hide \+ review, smart slideshows, system health dashboard with gentle notifications.

* **Security**: Local‑only by default, self‑signed HTTPS, audit log \+ version history.

* **Ops**: Windows Service at startup, port 8080 on 0.0.0.0, optional nginx later. Backups to `E:\media-server-backups`. Trash 60 days, logs 90 days or 500 MB.

# **Project scaffold (initial)**

| V:\\video-server\\├─ backend\\│  ├─ app\\│  │  ├─ api\\│  │  │  ├─ routes\_media.py│  │  │  ├─ routes\_search.py│  │  │  ├─ routes\_slideshow.py│  │  │  ├─ routes\_health.py│  │  │  └─ routes\_admin.py│  │  ├─ core\\│  │  │  ├─ config.py│  │  │  ├─ deps.py│  │  │  └─ logging\_conf.py│  │  ├─ services\\│  │  │  ├─ indexer.py│  │  │  ├─ thumbnails.py│  │  │  ├─ metadata.py│  │  │  ├─ ai\_tagging.py│  │  │  ├─ dedupe.py│  │  │  ├─ slideshow.py│  │  │  ├─ casting.py│  │  │  └─ health.py│  │  ├─ models\\│  │  │  ├─ db.py           (SQLite init)│  │  │  ├─ media.py        (ORM models)│  │  │  └─ audit.py│  │  ├─ workers\\│  │  │  ├─ celery\_app.py│  │  │  └─ tasks.py│  │  ├─ schemas\\│  │  │  ├─ media.py│  │  │  ├─ search.py│  │  │  └─ health.py│  │  ├─ main.py            (FastAPI app factory)│  │  └─ sidecar\_schema.json│  ├─ tests\\│  ├─ requirements.txt│  └─ .env.example├─ frontend\\│  ├─ index.html│  ├─ vite.config.ts│  ├─ package.json│  ├─ src\\│  │  ├─ main.tsx│  │  ├─ App.tsx│  │  ├─ routes\\ (Home, Library, Detail, Discover, Slideshow, Settings, Health)│  │  ├─ components\\│  │  │  ├─ GalleryGrid.tsx│  │  │  ├─ MosaicView.tsx│  │  │  ├─ CinematicStrip.tsx│  │  │  ├─ VRPanels.tsx│  │  │  ├─ RadialMenu.tsx│  │  │  ├─ ThemeSwitcher.tsx│  │  │  ├─ DensityControl.tsx│  │  │  └─ GlassPanel.tsx│  │  ├─ styles\\ (Glass & Glow, themes)│  │  └─ pwa\\│  │     ├─ service-worker.ts│  │     └─ manifest.webmanifest├─ config\\│  ├─ server.yaml    (paths, ports, cache cap, quiet hours)│  ├─ https\\│  │  ├─ server.crt│  │  └─ server.key│  └─ nssm-scripts\\  (Windows Service helpers)├─ cache\\├─ logs\\├─ backups\\├─ scripts\\│  ├─ first*\_run\_*setup.ps1│  ├─ index\_now.ps1│  ├─ create\_cert.ps1│  ├─ install\_services.ps1│  └─ backup\_now.ps1└─ README.md |
| :---- |

## **Key configuration**

**config\\server.yaml**

| paths:  images\_root: "G:\\\\Dev"  videos\_root: "V:\\\\local-video-server\\\\videos"  cache\_root: "V:\\\\video-server\\\\cache"  backups\_root: "E:\\\\media-server-backups"server:  host: "0.0.0.0"  port: 8080  https: true  cert\_path: "config/https/server.crt"  key\_path: "config/https/server.key"search:  meili\_host: "http://127.0.0.1:7700"  refresh\_interval\_active\_s: 10jobs:  broker\_url: "redis://127.0.0.1:6379/0"  max\_workers: 3  quiet\_hours: "01:00-06:00"thumbnails:  sizes: \[256, 512, 1024\]  video\_poster\_width: 1280  cache\_cap\_gb: 50ai:  local\_first: true  openai\_fallback: false  max\_concurrent\_jobs: 2video:  transcode:    enable\_smart: true    max\_bitrate\_mbps: 15    codec: "hevc"    container: "mp4"  subtitles:    default\_font\_family: "Merriweather"    default\_font\_size\_pt: 18security:  lan\_only: true  ip\_allowlist: \[\]retention:  trash\_days: 60  logs\_days: 90  logs\_max\_mb: 500 |
| :---- |

**backend\\requirements.txt**

| fastapiuvicorn\[standard\]pydanticSQLAlchemyalembicpython-multipartPillowopencv-python-headlessimagehashffmpeg-pythonmeilisearchrediscelery\[redis\]tenacitypython-dateutilcolorama |
| :---- |

**frontend\\package.json** (essentials)

| {  "name": "video-server-ui",  "private": true,  "scripts": {    "dev": "vite",    "build": "vite build",    "preview": "vite preview"  },  "dependencies": {    "react": "^18",    "react-dom": "^18",    "react-router-dom": "^6",    "zustand": "^4",    "framer-motion": "^11",    "clsx": "^2"  },  "devDependencies": {    "typescript": "^5",    "vite": "^5",    "@types/react": "^18",    "@types/react-dom": "^18"  }} |
| :---- |

**backend\\app\\sidecar\_schema.json** (base)

| {  "$schema": "https://json-schema.org/draft/2020-12/schema",  "title": "Media Sidecar",  "type": "object",  "properties": {    "title": {"type": "string"},    "tags": {"type": "array", "items": {"type": "string"}},    "rating": {"type": "number", "minimum": 0, "maximum": 5},    "captions": {"type": "string"},    "ai\_labels": {"type": "array", "items": {"type": "string"}},    "people": {"type": "array", "items": {"type": "string"}},    "albums": {"type": "array", "items": {"type": "string"}},    "hash": {"type": "string"},    "duplicates": {"type": "array", "items": {"type": "string"}},    "custom\_flags": {"type": "array", "items": {"type": "string"}}  },  "additionalProperties": true} |
| :---- |

## **First‑run setup (Windows, concise)**

1. **Install prerequisites**

* FFmpeg (latest, with NVENC if your GPU supports it) in PATH.

* Redis (Windows port or WSL service).

* Meilisearch (download and run as a service).

* Python 3.11+. Node 20+.

2. **Create self‑signed cert**

* Run `scripts\create_cert.ps1` to generate `config\https\server.crt` and `server.key`.

3. **Configure**

* Edit `config\server.yaml` paths if needed.

* Copy `backend\.env.example` to `.env` and set secrets if any.

4. **Install**

* Backend: `pip install -r backend\requirements.txt`

* Frontend: `cd frontend && npm install`

5. **Index once**

* Run `scripts\index_now.ps1` to perform initial scan, thumbnail warmup, Meilisearch ingest.

6. **Run dev**

* Terminal A: `redis-server`

* Terminal B: `meilisearch`

* Terminal C: `cd V:\video-server\backend && uvicorn app.main:app --host 0.0.0.0 --port 8080 --ssl-keyfile config/https/server.key --ssl-certfile config/https/server.crt`

* Terminal D: `cd V:\video-server\backend && celery -A app.workers.celery_app.celery_app worker -l info -Q default,ai,thumbs`

* Terminal E: `cd V:\video-server\frontend && npm run dev`

7. **Install as Windows Services** (optional now)

* Use `scripts\install_services.ps1` with NSSM to register uvicorn, celery worker, meilisearch.

## **Core API outline**

* `GET /api/media` list with segmented infinite scroll, filters, sort.

* `GET /api/media/{id}` detail with metadata, AI insights, related.

* `POST /api/actions/tag|rate|favorite|collect`

* `POST /api/search` hybrid search with refiners.

* `POST /api/slideshow/start` instant start, optional config.

* `POST /api/admin/index` scan \+ incremental index.

* `GET /api/health/status` system health, cache, queues, storage.

* `POST /api/dedupe/review` queue, decisions, unhide on keep.

## **Next step**

If you want, I can generate the initial files for `backend/app/core/config.py`, `backend/app/main.py`, `backend/app/workers/celery_app.py`, and a minimal React home with the Hybrid Welcome layout so you can run this today.

