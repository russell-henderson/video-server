import { useState, useEffect } from "react";

const ThemeSwitcher = () => {
  const [dark, setDark] = useState(true);
  useEffect(() => {
    document.documentElement.classList.toggle("dark", dark);
  }, [dark]);
  return (
    <button
      className="px-3 py-2 rounded-xl hover:bg-white/10 focus:outline-none focus-visible:ring-2 focus-visible:ring-emerald-400"
      onClick={() => setDark((v) => !v)}
      aria-label="Toggle theme"
      title="Toggle theme"
    >
      {dark ? "🌙" : "☀️"}
    </button>
  );
};
export default ThemeSwitcher;
