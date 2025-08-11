import React from "react";
import clsx from "clsx";

export default function GlassPanel({ children, className }: React.PropsWithChildren<{ className?: string }>) {
  return (
    <div
      className={clsx(
        "glass",
        className
      )}
    >
      {children}
    </div>
  );
}