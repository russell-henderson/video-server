<p align="center">
  <img src="https://i.ibb.co/Q3s4XRqh/logo.png" alt="Local Premium Media Server Logo" height="80"/>
</p>

<h1 align="center">🎬 Local Premium Media Server</h1>

<p align="center">
  <em>Luxury, Cinematic, VR-Ready Media Experience — Powered by FastAPI & React/Vite</em><br/>
  Multi-platform, privacy-first, and fully AI-integrated for the Meta Quest 2 and beyond.
</p>

<p align="center">
  <a href="https://github.com/russell-henderson/video-server/stargazers">
    <img src="https://img.shields.io/github/stars/russell-henderson/video-server?style=for-the-badge&color=gold" alt="GitHub Stars"/>
  </a>
  <a href="https://github.com/YOUR_USERNAME/YOUR_REPO_NAME/issues">
    <img src="https://img.shields.io/github/issues/russell-henderson/video-server?style=for-the-badge&color=blue" alt="GitHub Issues"/>
  </a>
  <a href="https://github.com/russell-henderson/video-server/blob/main/LICENSE">
    <img src="https://img.shields.io/github/license/russell-henderson/video-server?style=for-the-badge&color=green" alt="License"/>
  </a>
  <img src="https://img.shields.io/github/last-commit/russell-henderson/video-server?style=for-the-badge&color=purple" alt="Last Commit"/>
</p>

---

## ✨ Overview

The **Local Premium Media Server** delivers a **luxury, cinematic, and immersive gallery experience** for your personal media library.  
Built with **FastAPI** on the backend and **React + Vite** on the frontend, it’s designed for **Meta Quest 2 VR**, but scales beautifully across desktop, tablet, and mobile devices.

It’s not just a media server — it’s a **high-end private cinema** in your home network, enhanced by **local AI** for tagging, searching, and discovering your content without compromising privacy.

---

## 🎯 Key Features

- **🎨 Glass & Glow Theme**  
  Polished, luxury-inspired UI with default **Cinematic Dark** mode and optional Gallery Light, Warm Gold, or Minimal Dark variations.

- **📱 PWA Installable**  
  Works offline, installable on desktop, mobile, or directly on VR devices.

- **🖼️ Hybrid Welcome Screen**  
  Cinematic hero carousel paired with quick-access navigation for an engaging first impression.

- **🕶️ VR-Optimized UI**  
  Split Panel + Gallery Room layouts, radial quick menus, and spatial hotspots designed for VR comfort.

- **🔍 Hybrid Search**  
  Metadata-driven and AI-powered semantic search using Meilisearch with CLIP/ViT embeddings.

- **🧠 Local AI Processing**  
  Tagging, captioning, deduplication, and recommendations powered by **Ollama** models (`gpt-oss:20b`, `mistral:7b`, `llava-phi3`, `moondream`).

- **🎞️ Smart Slideshows**  
  Theme-aware transitions, cinematic overlays, and related suggestions at a single click.

- **🛡️ Privacy-Focused**  
  LAN-only HTTPS, IP allowlist, no cloud dependencies by default.

---

## 📂 Tech Stack

| Layer        | Technology |
|--------------|------------|
| **Backend**  | FastAPI, Celery/RQ, SQLite, Meilisearch |
| **Frontend** | React + Vite, TailwindCSS, Framer Motion, Zustand |
| **Media**    | FFmpeg (NVENC), JPEG/WEBP thumbnails, MP4 H.265 |
| **AI**       | Ollama (`gpt-oss:20b`, `mistral:7b`, `llava-phi3`, `moondream`) |
| **Target**   | Meta Quest 2 (VR), desktop, mobile |

---

## 🚀 Getting Started

### 1. Prerequisites
- **Node.js** v20+
- **Python** 3.11+
- **Redis** (for job queue)
- **FFmpeg** (with NVENC if GPU supports it)
- **Meilisearch** running locally

---

### 2. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/YOUR_REPO_NAME.git
cd YOUR_REPO_NAME
```
### 3. Install Frontend
```bash
cd frontend
npm install
npm run dev
```
### 4. Install Backend
```bash
cd backend
pip install -r requirements.txt
uvicorn app.main:app --host 0.0.0.0 --port 8080 \
  --ssl-keyfile config/https/server.key \
  --ssl-certfile config/https/server.crt
```
### 5. Access the App
Open your browser (or Quest browser) to:
```bash
https://<YOUR_LOCAL_IP>:8080
```
## 🖌️ UI/UX Highlights

- **Glass & Glow aesthetic** with dynamic ambient backdrops
- Smooth, subtle animations optimized for VR comfort
- Context-aware UI: core controls always visible, media-type tools appear on demand
- Adjustable density modes and theme personalization
- Segmented infinite scroll for large collections

---

## 📸 Screenshots

*Coming Soon* — In-app previews showcasing VR and desktop layouts.

---

## 🛠️ Roadmap

- [ ] GitHub Pages demo of the frontend
- [ ] Expanded AI Smart Collections
- [ ] Full VR environment themes
- [ ] Playlist and watch-later features
- [ ] Remote control from companion device

---

## 🤝 Contributing

Contributions are welcome!  
Please fork the repo and submit a pull request, or open an issue for discussion.

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<p align="center">
  <img src="https://i.ibb.co/LXLwpm2t/favicon.png" alt="Local Premium Media Server Icon" height="48"/>
</p>

<p align="center">
  <em>Crafted for those who value privacy, performance, and premium design in their personal media experience.</em>
</p>

