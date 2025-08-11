// frontend/src/routes/Home.tsx
import { motion } from "framer-motion";
import { Link } from "react-router-dom";

function GlassPanel({ children }: { children: React.ReactNode }) {
  return (
    <div
      style={{
        background: "rgba(255,255,255,0.06)",
        border: "1px solid rgba(255,255,255,0.12)",
        boxShadow: "0 8px 32px rgba(0,0,0,0.35)",
        backdropFilter: "blur(16px)",
        WebkitBackdropFilter: "blur(16px)",
        borderRadius: 24,
      }}
      className="p-6 md:p-8"
    >
      {children}
    </div>
  );
}

export default function Home() {
  return (
    <div
      className="min-h-screen"
      style={{
        background:
          "radial-gradient(80% 120% at 20% 10%, rgba(255,200,150,0.12), transparent 60%), radial-gradient(90% 120% at 80% 0%, rgba(100,160,255,0.12), transparent 50%), linear-gradient(180deg, #0b0f17 0%, #090c12 100%)",
        color: "#e8eef8",
      }}
    >
      <div className="max-w-6xl mx-auto px-4 py-16 md:py-24">
        {/* Cinematic hero */}
        <motion.div
          initial={{ opacity: 0, y: 12 }}
          animate={{ opacity: 1, y: 0 }}
          transition={{ duration: 0.6, ease: "easeOut" }}
          className="mb-12"
        >
          <GlassPanel>
            <div className="flex flex-col md:flex-row md:items-end gap-6">
              <div className="flex-1">
                <h1 className="text-3xl md:text-5xl font-semibold tracking-tight">
                  Your Cinematic Gallery
                </h1>
                <p className="text-sm md:text-base opacity-80 mt-3 max-w-prose">
                  A luxury, immersive library for photos & videos. Local-first. VR-ready. Private by design.
                </p>
              </div>
              <div className="flex items-center gap-3">
                <Link to="/library" className="btn-primary">Open Library</Link>
                <Link to="/discover" className="btn-ghost">Discover</Link>
              </div>
            </div>
          </GlassPanel>
        </motion.div>

        {/* Quick nav cards */}
        <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-6">
          {[
            { to: "/library", title: "Library", desc: "Browse all media" },
            { to: "/slideshow", title: "Slideshow", desc: "One-click story mode" },
            { to: "/health", title: "Health", desc: "System status & cache" },
            { to: "/settings", title: "Settings", desc: "Themes & paths" },
          ].map((card) => (
            <motion.div key={card.to} initial={{ opacity: 0, y: 8 }} whileInView={{ opacity: 1, y: 0 }} viewport={{ once: true }}>
              <Link to={card.to} aria-label={card.title}>
                <GlassPanel>
                  <div className="space-y-2">
                    <div className="text-xl font-medium">{card.title}</div>
                    <div className="text-sm opacity-75">{card.desc}</div>
                  </div>
                </GlassPanel>
              </Link>
            </motion.div>
          ))}
        </div>

        {/* Tiny style helpers */}
        <style>
          {`
          .btn-primary{display:inline-flex;align-items:center;gap:.5rem;padding:.6rem 1rem;border-radius:9999px;border:1px solid rgba(255,255,255,.2);background:linear-gradient(180deg,rgba(255,255,255,.15),rgba(255,255,255,.05));color:#e8eef8;}
          .btn-primary:hover{transform:translateY(-1px)}
          .btn-ghost{display:inline-flex;align-items:center;gap:.5rem;padding:.6rem 1rem;border-radius:9999px;border:1px solid rgba(255,255,255,.15);color:#e8eef8;background:transparent}
          .btn-ghost:hover{background:rgba(255,255,255,.06)}
          `}
        </style>
      </div>
    </div>
  );
}