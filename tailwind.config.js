/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./src/**/*.{js,jsx,ts,tsx}"],
  theme: {
    extend: {
      colors: {
        "custom-green": {
          500: "#838d4d",
          600: "#5f663a",
        },
      },
    },
  },
  plugins: [],
};
