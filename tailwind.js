module.exports = {
  theme: {
    extend: {},
  },
  variants: {},
  plugins: [
    require('tailwindcss')('tailwind.js'),
 		require('autoprefixer')()
  ],
}
