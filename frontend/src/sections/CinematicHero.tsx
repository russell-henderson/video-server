import { motion } from "framer-motion";
import GlassPanel from "../ui/GlassPanel";

const CinematicHero = () => {
  return (
    <GlassPanel as="section" className="relative overflow-hidden">
      <div className="relative z-10 p-6 md:p-10">
        <h1 className="text-3xl md:text-5xl font-semibold leading-tight">
          Your Private Cinema
        </h1>
        <p className="mt-3 max-w-xl text-white/70">
          Explore photos and videos with Glass & Glow elegance, VR comfort,
          and local‑only AI. Instant slideshows. Smart discovery. Zero cloud.
        </p>
        <div className="mt-6 flex flex-wrap gap-3">
          <a href="/library" className="btn-primary">Open Library</a>
          <a href="/discover" className="btn-secondary">Curator Mode</a>
          <a href="/slideshow" className="btn-secondary">Start Slideshow</a>
        </div>
      </div>

      {/* Ambient poster silhouette */}
      <motion.div
        aria-hidden
        className="absolute inset-0"
        initial={{ scale: 1.05, opacity: 0.4 }}
        animate={{ scale: 1.0, opacity: 0.55 }}
        transition={{ duration: 2 }}
        style={{
          background:
            "radial-gradient(1200px 500px at 20% 10%, rgba(16,185,129,0.15), transparent 60%), radial-gradient(1000px 500px at 100% 100%, rgba(34,211,238,0.12), transparent 60%)",
        }}
      />
    </GlassPanel>
  );
};

export default CinematicHero;
