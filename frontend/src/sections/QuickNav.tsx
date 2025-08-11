import GlassPanel from "../ui/GlassPanel";
import DensityControl from "../components/DensityControl";

const Item = ({ title, to, desc }: { title: string; to: string; desc: string }) => (
  <a
    href={to}
    className="group rounded-2xl p-4 bg-white/5 hover:bg-white/10 focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400 transition"
  >
    <div className="text-base font-semibold">{title}</div>
    <div className="text-sm text-white/60">{desc}</div>
  </a>
);

const QuickNav = () => (
  <GlassPanel as="section">
    <div className="flex items-center justify-between mb-4">
      <h2 className="text-lg font-semibold">Quick navigation</h2>
      <DensityControl />
    </div>
    <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-4 gap-3">
      <Item title="Library" to="/library" desc="All media with filters" />
      <Item title="Discover" to="/discover" desc="AI Smart Collections" />
      <Item title="Slideshow" to="/slideshow" desc="Instant theme‑aware show" />
      <Item title="Health" to="/health" desc="System and cache status" />
    </div>
  </GlassPanel>
);

export default QuickNav;
