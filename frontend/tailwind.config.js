/** @type {import('tailwindcss').Config} */
export default {
  content: [
    "./index.html",
    "./src/**/*.{vue,js,ts,jsx,tsx}",
  ],
  theme: {
    extend: {
      fontFamily: {
        pixel: ['cubic-11', 'sans-serif'],
      },
      height: {
        '1/10': '10dvh',
        '2/10': '20dvh',
        '3/10': '30dvh',
        '4/10': '40dvh',
        '5/10': '50dvh',
        '6/10': '60dvh',
        '7/10': '70dvh',
        '8/10': '80dvh',
        '9/10': '90dvh',
      },
    },
  },
  plugins: [],
}
