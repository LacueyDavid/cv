import React from "react";

function Name() {
  return (
    <>
      <h1 className="name">My Name</h1>
    </>
  );
}

function Experience() {
  return (
    <>
      <h2 className="experience">Experience</h2>
      <p className="experience-description">
        I have experience in React, Node.js, and more.
      </p>
    </>
  );
}

export default function WhoAmI() {
  return (
    <div className="flex flex-col pl-4">
      <Name />
      <p className="whoami">I am a developer</p>
      <Experience />
    </div>
  );
}
