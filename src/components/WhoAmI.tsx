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

function EnQuelquesMots() {
  return (
    <p className="text-sm">
      Je suis étudiant à l'école 42, actuellement à la recherche d’un stage. Mon
      parcours à 42 m’a permis de renforcer mes compétences en programmation, en
      résolution de problèmes et en travail d’équipe à travers des projets
      concrets.
    </p>
  );
}

function Experiences() {
  return (
    <div className="flex gap-4 flex-col">
      <CVSubHeader
        icon={<FaBriefcase className="w-5 h-5" />}
        title="EXPERIENCES"
        containerWidth="w-14" // 56px
      />

      <div className="flex gap-6 ">
        <div className="flex flex-col">
          <span className="text-xs">2023</span>
          <span className="text-xs">2025</span>
        </div>

        <div className="flex flex-col items-center h-full relative pt-4">
          <div className="absolute flex flex-col rounded-full bg-black w-2 h-2"></div>
          <div className="absolute w-[2px] h-full bg-black"></div>
        </div>

        <div className="flex flex-col gap-4">
          <div className="flex flex-col gap-1">
            <span className="font-bold text-xs">
              ARCHITECTE EN TECHNOLOGIE DU NUMERIQUE
            </span>
            <span className="text-xs text-gray-500">Ecole 42 - Paris</span>
          </div>

          <div className="flex flex-col gap-1">
            <span className="text-xs font-bold">PROJETS WEB</span>
            <span className="text-xs">
              Création d'un site (conteneurisation des services via
              docker-compose, contenant un jeu multijoueurs avec une base de
              données SQL intégrée et un chat intéractif, les technologies
              principales utilisées sont JavaScript, Django, Bootstrap,
              PostgreSQL, Docker, Docker Compose
            </span>
          </div>

          <div className="flex flex-col gap-1">
            <span className="text-xs font-bold">PROJETS C99</span>
            <span className="text-xs font-medium">
              Réalisation d'un shell (Utilisaiton d'un AST, Développement d'une
              grammaire), reproduction d'un célèbre jeu (Wolfenstein 3D) à
              l'aide du "raycasting" en utilisant une librairie graphique avec
              la minilibX
            </span>
          </div>

          <div className="flex flex-col gap-1">
            <span className="text-xs font-bold">PROJETS C++98</span>
            <span className="text-xs">
              Développement d'un serveur IRC fonctionnant sur du polling
            </span>
          </div>
        </div>
      </div>
    </div>
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
      <EnQuelquesMots />
      <Experiences />
    </div>
  );
}
