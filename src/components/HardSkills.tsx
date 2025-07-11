import React from "react";
import LineItem from "./LineItem";
import CVSubHeader from "./CVSubHeader";
import photo from "../img/photo_cv.png";
import { IconType } from "react-icons";
import { PiStudentFill } from "react-icons/pi";
import { IoIosPeople } from "react-icons/io";
import { BsGearFill } from "react-icons/bs";
import { FaMobileAlt, FaEnvelope, FaMapMarkerAlt } from "react-icons/fa";

interface ContactItemProps {
  icon: IconType;
  text: string;
}

const ContactItem = ({ icon: Icon, text }: ContactItemProps) => {
  return (
    <div className="flex items-center gap-2 bg-gray-600 w-64 ">
      <div className="flex items-center justify-center w-10">
        <Icon className="text-white w-10 h-8 p-1 bg-gray-600" />
      </div>
      <span className="text-white">{text}</span>
    </div>
  );
};

const ImageItem = () => {
  return (
    <div>
      <img src={photo} alt="Logo" className="w-64 h-64 object-cover " />
      <LineItem lineHeight="h-[1px]" />
      <ContactItem icon={FaMobileAlt} text="06 67 87 94 26" />
      <LineItem lineHeight="h-[1px]" />
      <ContactItem icon={FaEnvelope} text="dlacuey@student.42.fr" />
      <LineItem lineHeight="h-[1px]" />
      <ContactItem
        icon={FaMapMarkerAlt}
        text="101 Avenue Laferrière, 94000 Créteil, France"
      />
      <LineItem lineHeight="h-[1px]" />
    </div>
  );
};

const FormationItem = () => {
  return (
    <div className="gap-6 flex justify-center flex-col w-full px-4">
      <CVSubHeader
        icon={<PiStudentFill className="w-6 h-6" />}
        title="FORMATION"
      />
      <div className="flex flex-col gap-1">
        <span className="font-bold w-52 text-xs ">
          ARCHITECTE EN TECHNOLOGIE DU NUMERIQUE
        </span>
        <span className="w-52 text-xs">Ecole 42 / Paris / 2024</span>
      </div>
    </div>
  );
};

const LogicielsItem = () => {
  return (
    <div className="gap-6 flex justify-center flex-col w-full px-4">
      <CVSubHeader
        icon={<IoIosPeople className="w-6 h-6" />}
        title="LOGICIELS"
      />
      <div className="flex flex-col gap-1">
        <span className="w-52 text-xs ">VISUAL STUDIO CODE</span>
        <span className="w-52 text-xs ">NEOVIM / VIM</span>
        <span className="w-52 text-xs ">SHELL</span>
        <span className="w-52 text-xs ">DOCKER</span>
        <span className="w-52 text-xs ">GIT</span>
      </div>
    </div>
  );
};

const CompetencesItem = () => {
  return (
    <div className="gap-6 flex justify-center flex-col w-full px-4">
      <CVSubHeader
        icon={<BsGearFill className="w-5 h-5" />}
        title="COMPETENCES"
      />
      <div className="flex flex-col gap-1">
        <div className="flex space-between gap-1 items-center">
          <span className="w-36 text-xs ">REACT</span>
          <div className="bg-black w-4 h-4 rounded"></div>
          <div className="bg-black w-4 h-4 rounded"></div>
          <div className="border-2 border-black w-4 h-4 rounded"></div>
          <div className="border-2 border-black w-4 h-4 rounded"></div>
        </div>

        <div className="flex space-between gap-1 items-center">
          <span className="w-36 text-xs ">TYPESCRIPT</span>
          <div className="bg-black w-4 h-4 rounded"></div>
          <div className="bg-black w-4 h-4 rounded"></div>
          <div className="border-2 border-black w-4 h-4 rounded"></div>
          <div className="border-2 border-black w-4 h-4 rounded"></div>
        </div>

        <div className="flex space-between gap-1 items-center">
          <span className="w-36 text-xs">MYSQL / MARIADB</span>
          <div className="bg-black w-4 h-4 rounded"></div>
          <div className="bg-black w-4 h-4 rounded"></div>
          <div className="border-2 border-black w-4 h-4 rounded"></div>
          <div className="border-2 border-black w-4 h-4 rounded"></div>
        </div>

        <div className="flex space-between gap-1 items-center">
          <span className="w-36 text-xs ">LINUX / UNIX</span>
          <div className="bg-black w-4 h-4 rounded"></div>
          <div className="bg-black w-4 h-4 rounded"></div>
          <div className="bg-black w-4 h-4 rounded"></div>
          <div className="border-2 border-black w-4 h-4 rounded"></div>
        </div>

        <div className="flex space-between gap-1 items-center">
          <span className="w-36 text-xs ">C 99</span>
          <div className="bg-black w-4 h-4 rounded"></div>
          <div className="bg-black w-4 h-4 rounded"></div>
          <div className="border-2 border-black w-4 h-4 rounded"></div>
          <div className="border-2 border-black w-4 h-4 rounded"></div>
        </div>

        <div className="flex space-between gap-1 items-center">
          <span className="w-36 text-xs ">C++ 98</span>
          <div className="bg-black w-4 h-4 rounded"></div>
          <div className="border-2 border-black w-4 h-4 rounded"></div>
          <div className="border-2 border-black w-4 h-4 rounded"></div>
          <div className="border-2 border-black w-4 h-4 rounded"></div>
        </div>
      </div>
    </div>
  );
};

export default function HardSkills() {
  return (
    <div className="gap-8 flex flex-col items-center bg-gray-200">
      <ImageItem />
      <FormationItem />
      <LogicielsItem />
      <CompetencesItem />
    </div>
  );
}
