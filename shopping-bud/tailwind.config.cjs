
module.exports = {
  content: ['./src/**/*.{html,js,svelte,ts}'],
  daisyui: {
    themes: ["light", "dark", "retro","lemonade","night","pastel","cupcake"],
  },
  theme: {
    fontFamily: {
      'nunito': ['nunito', 'sans-serif'],
    },
    extend: {
      colors: {
        "red": "#E4572E",
        "yellow": "#FFC914",
        "blue": "#17BEBB",
        "green": "#76B041",
        "black": "#1E2433",
        "dark": "#2C3763",
        "white": "#FEFFFE",
        "dark-grey": '#596475',
        "light-grey": "#DCE0E5",
        "pink":"#D0C1D6",
        "light-blue":"#4591b4"
      }
    }
  },
  plugins: [ require("@tailwindcss/typography"),require("daisyui")]
};
