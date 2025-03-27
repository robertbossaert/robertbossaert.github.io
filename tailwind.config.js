/** @type {import('tailwindcss').Config} */
export default {
  content: ['./themes/**/*.{html,js}'],
  theme: {
    container: {
      center: true,
      padding: {
        DEFAULT: '1.2rem',
        md: '2rem',
      },
    },
    extend: {},
  },
  plugins: [],
}