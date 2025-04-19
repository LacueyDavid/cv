import React from "react";
import { ReactNode } from "react";

type CVSubHeaderProps = {
  icon: ReactNode;
  title: string;
  containerWidth?: string;
};

export default function CVSubHeader({
  icon,
  title,
  containerWidth = "w-16",
}: CVSubHeaderProps) {
  return (
    <div>
      <CVSubHeaderLine />
      <div className="w-full flex">
        <div
          className={`flex justify-center items-center ${containerWidth} h-8`}
        >
          {icon}
        </div>
        <div className="flex w-full pl-4 items-center">
          <h3 className="font-bold text-sm">{title}</h3>
        </div>
      </div>
      <CVSubHeaderLine />
    </div>
  );
}

const CVSubHeaderLine = () => {
  return (
    <div className="flex w-full">
      <div className="relative flex w-full h-1 items-center">
        <div className="absolute w-full h-[3px] bg-gray-400 rounded"></div>
        <div className="absolute w-12 h-[4px] bg-black rounded"></div>
      </div>
    </div>
  );
};
