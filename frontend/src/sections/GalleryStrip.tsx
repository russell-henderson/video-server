import GlassPanel from "../ui/GlassPanel";

type Props = { kind: "videos" | "images" };

const skeleton = new Array(10).fill(null);

const GalleryStrip = ({ kind }: Props) => {
  // Future: fetch from /api/media?type=video|image&limit=20
  return (
    <GlassPanel>
      <div className="flex gap-3 overflow-x-auto snap-x snap-mandatory pb-1">
        {skeleton.map((_, i) => (
          <div
            key={i}
            className="min-w-[220px] snap-start rounded-xl overflow-hidden bg-white/5 border border-white/10"
          >
            <div className="aspect-video bg-white/5" />
            <div className="p-3">
              <div className="h-4 w-3/4 bg-white/10 rounded mb-2" />
              <div className="h-3 w-1/2 bg-white/10 rounded" />
            </div>
          </div>
        ))}
      </div>
      <p className="sr-only">{kind === "videos" ? "Video strip" : "Image strip"}</p>
    </GlassPanel>
  );
};

export default GalleryStrip;
