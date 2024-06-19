/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./templates/**/*.html",
    "./static/src/**/*.js"
  ],
  theme: {
    extend: {},
  },
  plugins: [],
  variants: {
    extend: {
      opacity: ['group-hover'], // Ensure 'group-hover' variant for opacity is enabled
    },
  },
}
