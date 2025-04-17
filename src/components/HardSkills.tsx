import React from "react";
import photo from "../img/photo_cv.jpg";
import { IconType } from "react-icons"; // Pour le typage de l'icône
import {
  FaMobileAlt,
  FaEnvelope,
  FaMapMarkerAlt,
  FaLinkedin,
} from "react-icons/fa";

interface ContactItemProps {
  icon: IconType;
  text: string;
}

const ContactItem = ({ icon: Icon, text }: ContactItemProps) => {
  return (
    <div className="flex items-center gap-2 bg-gray-600 w-64 shadow shadow-black/40">
      <Icon className="text-white w-10 h-8 p-1 bg-gray-600 shadow shadow-black/40 bg-gradient-to-r from-gray-500 from-60% via-gray-700 via-90% to-gray-700 to-100%" />
      <span className="text-white">{text}</span>
    </div>
  );
};

const FormationItem = () => {
  return <div className="flex bg-custom-green-500 w-64">formation</div>;
};

export default function HardSkills() {
  return (
    <div className="pr-4 flex flex-col items-center">
      <img
        src={photo}
        alt="Logo"
        className="w-64 h-64 object-cover shadow shadow-black/40"
      />
      <ContactItem icon={FaMobileAlt} text="06 67 87 94 26" />
      <ContactItem icon={FaEnvelope} text="lacuey.david@gmail.com" />
      <ContactItem icon={FaMapMarkerAlt} text="Paris, France" />
      <FormationItem />
    </div>
  );
}
