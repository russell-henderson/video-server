import { useParams } from "react-router-dom";

const Detail = () => {
  const { id } = useParams();
  return (
    <div className="glass-panel">
      <h1 className="text-2xl font-semibold mb-2">Detail</h1>
      <p className="text-white/70">Media ID: {id}</p>
    </div>
  );
};
export default Detail;
