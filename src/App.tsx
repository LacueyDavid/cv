import React from "react";
import HardSkills from "./components/HardSkills";
import WhoAmI from "./components/WhoAmI";

export default function CV() {
  return (
    <div className="cv flex p-8 gap-8">
      <HardSkills />
      <WhoAmI />
    </div>
  );
}
