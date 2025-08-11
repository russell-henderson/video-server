// frontend/src/App.tsx
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import Home from "./routes/Home";

export default function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<Home />} />
        <Route path="/home" element={<Navigate to="/" replace />} />
        {/* Stubs so links don't 404 while you scaffold other routes */}
        <Route path="/library" element={<div style={{padding:24}}>Library (coming soon)</div>} />
        <Route path="/discover" element={<div style={{padding:24}}>Discover (coming soon)</div>} />
        <Route path="/slideshow" element={<div style={{padding:24}}>Slideshow (coming soon)</div>} />
        <Route path="/health" element={<div style={{padding:24}}>Health (coming soon)</div>} />
        <Route path="/settings" element={<div style={{padding:24}}>Settings (coming soon)</div>} />
        <Route path="*" element={<Navigate to="/" replace />} />
      </Routes>
    </BrowserRouter>
  );
}