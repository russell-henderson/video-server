import { Routes, Route, NavLink } from "react-router-dom";
import { motion } from "framer-motion";
import Home from "./routes/Home";
import Library from "./routes/Library";
import Detail from "./routes/Detail";
import Discover from "./routes/Discover";
import Slideshow from "./routes/Slideshow";
import Settings from "./routes/Settings";
import Health from "./routes/Health";
import ThemeSwitcher from "./components/ThemeSwitcher";

const navLink =
  "px-4 py-2 rounded-xl hover:bg-white/10 focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400";

const App = () => {
  return (
    <div className="min-h-dvh bg-[#0b0f14] text-white antialiased">
      {/* Glass header */}
      <header className="sticky top-0 z-40 backdrop-blur-xl bg-white/5 border-b border-white/10">
        <div className="mx-auto max-w-7xl px-4 py-3 flex items-center justify-between">
          <div className="flex items-center gap-3">
            <div className="h-8 w-8 rounded-2xl bg-gradient-to-br from-emerald-400/80 to-cyan-400/80 shadow-lg shadow-emerald-500/20" />
            <span className="text-lg font-semibold tracking-wide">Local Premium Media Server</span>
          </div>
          <nav className="flex items-center gap-1">
            <NavLink to="/" className={navLink} end>Home</NavLink>
            <NavLink to="/library" className={navLink}>Library</NavLink>
            <NavLink to="/discover" className={navLink}>Discover</NavLink>
            <NavLink to="/slideshow" className={navLink}>Slideshow</NavLink>
            <NavLink to="/health" className={navLink}>Health</NavLink>
            <NavLink to="/settings" className={navLink}>Settings</NavLink>
            <ThemeSwitcher />
          </nav>
        </div>
      </header>

      {/* Ambient glow backdrop */}
      <div className="pointer-events-none fixed inset-0 -z-10">
        <motion.div
          aria-hidden
          className="absolute -top-24 left-1/3 h-72 w-72 rounded-full blur-3xl bg-emerald-500/10"
          animate={{ x: [0, 20, -10, 0], y: [0, -10, 10, 0], scale: [1, 1.05, 1] }}
          transition={{ repeat: Infinity, duration: 20 }}
        />
        <motion.div
          aria-hidden
          className="absolute bottom-0 right-1/4 h-96 w-96 rounded-full blur-3xl bg-cyan-500/10"
          animate={{ x: [0, -10, 10, 0], y: [0, 10, -10, 0], scale: [1, 1.03, 1] }}
          transition={{ repeat: Infinity, duration: 24 }}
        />
      </div>

      {/* Routes */}
      <main className="mx-auto max-w-7xl px-4 py-8">
        <Routes>
          <Route index element={<Home />} />
          <Route path="/library" element={<Library />} />
          <Route path="/discover" element={<Discover />} />
          <Route path="/slideshow" element={<Slideshow />} />
          <Route path="/health" element={<Health />} />
          <Route path="/settings" element={<Settings />} />
          <Route path="/detail/:id" element={<Detail />} />
        </Routes>
      </main>
    </div>
  );
};

export default App;
