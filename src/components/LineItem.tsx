import React from "react";

type LineItemProps = {
  lineHeight?: string;
};

export default function LineItem({ lineHeight = "h-[3px]" }: LineItemProps) {
  return <div className={`w-full ${lineHeight} bg-gray-400 rounded`}></div>;
}
