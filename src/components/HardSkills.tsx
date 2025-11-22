import React from "react";
import LineItem from "./LineItem";
import CVSubHeader from "./CVSubHeader";
import photo from "../img/photo_cv.png";
import { IconType } from "react-icons";
import { PiStudentFill } from "react-icons/pi";
import { IoIosPeople } from "react-icons/io";
import { BsGearFill } from "react-icons/bs";
import { FaGithub } from "react-icons/fa";
import { FaMobileAlt, FaEnvelope, FaMapMarkerAlt } from "react-icons/fa";
import cvData from "../data/cv-data.json";

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
      <ContactItem icon={FaMobileAlt} text={cvData.personal.contact.phone} />
      <LineItem lineHeight="h-[1px]" />
      <ContactItem icon={FaEnvelope} text={cvData.personal.contact.email} />
      <LineItem lineHeight="h-[1px]" />
      <ContactItem
        icon={FaMapMarkerAlt}
        text={cvData.personal.contact.address}
      />
      <LineItem lineHeight="h-[1px]" />
      <ContactItem icon={FaGithub} text={cvData.personal.contact.github} />
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
      {cvData.formation.map((formation: any, index: number) => (
        <div key={index} className="flex flex-col gap-1">
          <span className="font-bold w-52 text-xs ">{formation.degree}</span>
          <span className="w-52 text-xs">
            {formation.school} / {formation.location} / {formation.year}
          </span>
        </div>
      ))}
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
        {cvData.skills.logiciels.map((logiciel: string, index: number) => (
          <span key={index} className="w-52 text-xs ">
            {logiciel}
          </span>
        ))}
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
        {cvData.skills.competences.map((competence: string, index: number) => (
          <div key={index} className="flex space-between gap-1 items-center">
            <span className="w-36 text-xs ">{competence}</span>
          </div>
        ))}
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
