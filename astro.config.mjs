// @ts-check
import { defineConfig } from "astro/config"
import tailwindcss from "@tailwindcss/vite"

// https://astro.build/config
export default defineConfig({
  base: "/astro_blog/",
  vite: { plugins: [tailwindcss()] },
})
