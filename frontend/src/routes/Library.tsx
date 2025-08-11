import React from "react";
import GlassPanel from "../components/GlassPanel";

export default function Library() {
  return (
    <div className="page-root">
      <div className="container">
        <h2 className="section-title">Library</h2>
        <GlassPanel>
          <div style={{ padding: 16 }}>
            <p>
              This is a placeholder. Wire this view to <code>/api/media</code> with
              segmented infinite scroll next.
            </p>
          </div>
        </GlassPanel>
      </div>
    </div>
  );
}