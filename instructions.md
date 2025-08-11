
# Local Premium Media Server – Custom Instructions

**`/projects/media-server/custom_instructions.md`**

## **Purpose**

These instructions define the **exact tech stack, architecture, features, UI/UX, AI integrations, and VR optimizations** for building my **premium, cinematic, gallery‑inspired local media server**, primarily for Meta Quest 2, but with full multi‑platform support.

***

## **1. Project Overview**

- **Name:** Local Premium Media Server
- **Primary Device:** Meta Quest 2 VR, also desktop, tablet, and mobile
- **Core Design Goals:**
  - Luxury, cinematic, immersive gallery experience
  - Flexible but consistent UI with refined polish
  - Performance‑aware, privacy‑focused, and future‑proof
  - Heavy use of **local AI** with minimal cloud fallback
  - Multi‑platform optimized UX

***

## **2. Platform \& Tech Stack**

- **Backend:** **FastAPI** (async, performance, AI-ready)
- **Frontend:** **React + Vite**
- **PWA:** Yes (installable app + offline shell)
- **Deployment:** Initially run directly, later optionally front with nginx reverse proxy
- **VR Support:** Optimized interaction layouts for Quest 2

***

## **3. Database \& Indexing**

- **Full‑text Search:** Meilisearch
- **Metadata Store:** SQLite DB + JSON sidecars per media file
- **Index Refresh Cap:** Max 1 every 10s during active use
- **Sidecar Schema:**

```bash

<media>.json  
title, tags[], rating, captions, ai_labels[], people[], albums[],
hash, duplicates[], custom_flags[]
```

- **Data Priority:** Manual edits always override AI re-ingest

***

## **4. Background Jobs**

- **Queue System:** RQ/Celery
- **Quiet Hours:** 1am–6am
- **Max Workers:** 3
- **Job Types:** AI tagging, thumbnail generation, integrity checks, cache trim

***

## **5. Media Handling**

- **Thumbnail Cache:** `V:\video-server\cache`, 50GB limit
- **Sizes:** 256, 512, 1024 + video posters at 1280px
- **Photo Thumbs:** High‑quality JPEG/WEBP
- **FFmpeg:** Latest stable w/NVENC hardware acceleration
- **Max Transcode Bitrate:** 15 Mbps for 4K
- **Container/Codec:** MP4 + H.265/HEVC
- **Subtitles:** Luxury serif, size 18pt, soft outline

***

## **6. AI System**

- **Runtime:** Local first via Ollama models — `gpt-oss:20b`, `mistral:7b`, `llava-phi3:latest`, `moondream:latest`
- **Cloud Fallback:** OpenAI API **only if enabled** — use cheapest model, monitor \$3 credit cap
- **Vision Tagging/Similarity:** CLIP/ViT embeddings + llava-phi3 object detection
- **AI Concurrency:** Max 2 jobs
- **AI Tasks:** Auto‑tag, natural language search, dedupe/similarity, captions, themed recommendations

***

## **7. Casting \& Connectivity**

- **LAN Binding:** 0.0.0.0 on port 8080
- **Protocols:** Chromecast, DLNA (priority), AirPlay secondary
- **Security:** LAN HTTPS w/self-signed cert, IP allowlist
- **Launch:** Windows Service at boot

***

## **8. Backup \& Retention**

- **Daily 3am Backup:** DB + sidecars to `E:\media-server-backups`
- **Trash Retention:** 60 days
- **Log Retention:** 90 days or 500MB

***

## **9. UI \& UX**

### **Global Look**

- **Theme Style:** Glass \& Glow w/subtle theme variations (Cinematic Dark, Gallery Light, Warm Gold Accent, Minimal Dark)
- **Animations:** Smooth \& subtle, device‑optimized
- **Density:** Balanced per view mode, adjustable
- **Navigation:** Switchable view modes; segmented infinite scroll for large sets

### **VR-Specific**

- **Layout Style:** Split Panel + Gallery Room hybrid
- **Menus:** Flat Panels (core actions) + Radial Quick Menus + Spatial Hotspots
- **Inputs:** Controllers primary, hand tracking optional
- **Comfort:** Vignette on fast pans, snap scrolling
- **Radial Default:** Play/Pause, Next/Prev, Theme Toggle, Density, Cast
- **Detail Page:** Context-aware controls + ambient dynamic backdrop
- **Environment:** Stays in one “room,” optional theme‑adaptive scene changes

### **Home Screen**

- Hybrid Welcome layout: cinematic hero area + quick nav
- Dynamic by default, manual curation possible

### **Browsing \& Interaction**

- Context-aware UI: core controls always visible, context tools appear per media type
- Subtle framing + dynamic thumbnail effects (hover zoom, parallax)
- Photos: zoom/pan, Find Similar; Videos: playback, subtitle/audio control
- AI Smart Collections in “Curator Mode” (passive recommendations)

***

## **10. Smart Features**

- **Smart Slideshows:** One‑click launch from any collection; theme‑aware transitions, music, “Story Mode” overlays, related item suggestions
- **Duplicate Handling:** Exact + near-duplicates auto-flagged; hidden from browse until reviewed; bulk cleanup mode
- **Search:** Multi‑criteria + semantic, refiners after results, past search memory; hybrid metadata-first + AI fallback
- **System Health:** Auto performance monitoring, adaptive job throttling, proactive gentle alerts, integrity checks

***

## **11. Accessibility \& Shortcuts**

- **Target:** WCAG AA, high-contrast focus outlines, large hit areas
- **Desktop Shortcuts:** Ctrl+F (search), Space (slideshow), T (tag editor), arrows (navigate)
- **Quest Long-Press Gestures:** Toggle radial menu, quick favorite, view related media

***

**Instruction to ChatGPT when working on this project:**
All proposed code, UX flows, architecture ideas, and implementation details **must** comply with the above constraints. When in doubt, choose the option that:

1. Preserves **luxury cinematic design**
2. Ensures **VR comfort**
3. Prioritizes **local AI** over paid cloud calls
4. Keeps the UI **clean, contextual, and high‑performance**
5. Avoids breaking privacy or LAN‑only principles unless explicitly approved.

***
