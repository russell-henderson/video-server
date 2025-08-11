import { PropsWithChildren, ElementType } from "react";
import clsx from "clsx";

type Props<T extends ElementType> = PropsWithChildren<{
  as?: T;
  className?: string;
}>;

const GlassPanel = <T extends ElementType = "div">({
  as,
  className,
  children,
}: Props<T>) => {
  const Comp = (as || "div") as ElementType;
  return (
    <Comp
      className={clsx(
        "glass-panel rounded-2xl border border-white/10 bg-white/[0.06] backdrop-blur-xl shadow-lg shadow-black/20",
        className
      )}
    >
      {children}
    </Comp>
  );
};

export default GlassPanel;
