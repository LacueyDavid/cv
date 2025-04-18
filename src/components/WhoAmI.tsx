import React from "react";
import LineItem from "./LineItem";
import { FaBriefcase } from "react-icons/fa";
import CVSubHeader from "./CVSubHeader";

function Name() {
  return (
    <>
      <h1 className="font-semibold text-4xl">LACUEY DAVID</h1>
    </>
  );
}

function Metier() {
  return (
    <>
      <h1 className="font-semibold text-lg">DEVELOPPEUR INFORMATIQUE</h1>
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
    <div className="flex flex-col mt-8 w-full gap-4">
      <div>
        <Name />
        <Metier />
      </div>
      <LineItem />
      <p className="whoami">
        Je suis étudiant à l'école 42, actuellement à la recherche d’un stage.
        Mon parcours à 42 m’a permis de renforcer mes compétences en
        programmation, en résolution de problèmes et en travail d’équipe à
        travers des projets concrets.
      </p>
      <CVSubHeader
        icon={<FaBriefcase className="w-6 h-6" />}
        title="EXPERIENCES"
      />
      <Experience />
    </div>
  );
}
