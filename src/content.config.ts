import { glob } from "astro/loaders"
import { defineCollection, z } from "astro:content"
const docs = defineCollection({
  // Load Markdown and MDX files in the `src/contents/docs/` directory.
  loader: glob({ base: "./src/contents/docs", pattern: "**/*.{md,mdx}" }),
  // Type-check frontmatter using a schema
  schema: () =>
    z.object({
      title: z.string(),
      excerpt: z.string().default(""),
      post: z.boolean().default(false),
      date: z.coerce.date().optional(),
      auto_date: z.coerce.date().optional(),
      word_count: z.number().optional(),
      tags: z.array(z.string()).default([]),
      finished: z.boolean().default(false),
      ai_comment: z.boolean().default(false),
      ai_source: z.string().optional(),
    }),
})

export const collections = { docs }
