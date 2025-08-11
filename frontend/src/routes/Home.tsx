import { motion } from "framer-motion";
import CinematicHero from "../sections/CinematicHero";
import QuickNav from "../sections/QuickNav";
import GalleryStrip from "../sections/GalleryStrip";

const Home = () => {
  return (
    <div className="flex flex-col gap-10">
      <CinematicHero />

      <QuickNav />

      <section>
        <h2 className="mb-3 text-lg font-semibold tracking-wide text-white/90">
          Continue Watching
        </h2>
        <GalleryStrip kind="videos" />
      </section>

      <section>
        <h2 className="mb-3 text-lg font-semibold tracking-wide text-white/90">
          Fresh Photos
        </h2>
        <GalleryStrip kind="images" />
      </section>

      <motion.p
        className="text-white/50 text-sm"
        initial={{ opacity: 0 }}
        animate={{ opacity: 1 }}
        transition={{ delay: 0.2 }}
      >
        Tip: Long‑press in VR to open the radial menu. Arrow keys navigate on desktop.
      </motion.p>
    </div>
  );
};

export default Home;
