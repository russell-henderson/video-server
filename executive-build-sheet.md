# Executive Build Sheet — Local Premium Media Server

### 1. Platform \& Core Stack

- **Backend Framework:** FastAPI (async, high-performance, AI-ready)
- **Frontend Framework:** React with Vite (modular, performant UI)
- **PWA:** Yes (installable \& offline-capable)
- **Primary Target Device:** Meta Quest 2 VR (fully multi-platform adaptive)
- **Deployment:** Direct run initially; optional nginx reverse proxy later


### 2. Search \& Indexing

- **Search Engine:** Meilisearch (rich full-text + semantic)
- **Metadata Store:** SQLite + JSON sidecar files per media item
- **Index Refresh Cap:** Max once every 10 seconds during active use


### 3. Background Job Processing

- **Task Runner:** RQ or Celery (advanced queue management)
- **Quiet Hours:** 1am–6am for heavy jobs (AI, thumbnails)
- **Max Concurrent Workers:** 3


### 4. Media Handling

- **Video Toolchain:** FFmpeg latest stable with NVENC hardware acceleration
- **Max Transcode Bitrate:** 15 Mbps for 4K video
- **Container \& Codec:** MP4 with H.265/HEVC
- **Thumbnail Cache:** `V:\video-server\cache`, 50 GB cap; sizes: 256, 512, 1024 px plus video posters at 1280 px
- **Thumbnail Format:** High-quality JPEG/WEBP (not lossless)
- **Subtitles:** Serif font, 18 pt size with soft outline to complement UI typography


### 5. AI \& Machine Learning

- **AI Runtime:** Local via Ollama models—gpt-oss:20b, mistral:7b, llava-phi3, moondream
- **Fallback:** OpenAI API (lowest cost model) only if enabled, strict \$3 credit monitoring
- **Vision Tagging \& Similarity:** CLIP/ViT embeddings + lightweight detector (llava-phi3)
- **Max AI Jobs Concurrent:** 2


### 6. VR \& Interaction

- **Primary Input:** Oculus Quest controllers preferred; hand tracking optional fallback
- **Navigation:** Hybrid of flat UI panels, radial menus for quick actions, and spatial hotspots for immersion
- **Radial Menu Default Bindings:** Play/Pause, Next/Previous, Theme Toggle, Density, Cast
- **Comfort Features:** Vignette on fast pans, snap scrolling in galleries


### 7. Casting \& Network

- **Prioritized Protocols:** Chromecast \& DLNA primary; AirPlay secondary
- **Port \& Binding:** Port 8080, 0.0.0.0 host binding for LAN access
- **Security:** Local HTTPS with self-signed certificate, IP allowlist enforced
- **Startup:** Runs as Windows Service on OS boot


### 8. Backup \& Data Retention

- **Backup Path:** Local or external drive (e.g., `E:\media-server-backups`)
- **Backup Schedule:** Daily at 3 AM (database + sidecars)
- **Trash Retention:** 60 days before automatic purge
- **Log Retention:** 90 days or 500 MB max size


### 9. UI \& UX Design

- **Theme \& Style:** Glass \& Glow with curated variants (Cinematic Dark, Gallery Light, Warm Gold Accent, Minimal Dark)
- **Animations:** Smooth and subtle, optimized per device
- **Density:** Balanced default with per-mode adjustability
- **Large Collection Browsing:** Segmented infinite scroll
- **Home Screen:** Hybrid Welcome (hero carousel + quick nav), dynamic by default with manual curation option


### 10. Accessibility \& Shortcuts

- **Accessibility Standards:** WCAG AA, high contrast, focus outlines, large hit areas
- **Desktop Shortcuts:** Ctrl+F (search), Space (slideshow), T (tag edit), arrow keys (navigate)
- **Quest VR Gestures:** Long press toggles radial menu, quick favorite, view related media

***

This build sheet consolidates the technology choices, AI integrations, UI/UX paradigms, VR and multi-platform considerations, and security policies to ensure every development step aligns with your premium, immersive, and cost-effective media server vision.

Let me know if you want me to prepare the exact folder structure and first-run setup files next!

