import { defineCollection } from "astro:content";
import { z } from "astro/zod";
import { glob } from "astro/loaders";

const posts = defineCollection({
  loader: glob({
    pattern: "**/*.md",
    base: "./content",
    generateId: ({ entry }) => {
      const match = entry.match(
        /^([^/]+)\/\[(\d+)\](.+?)(?:\.md|\/index\.md)$/,
      );

      if (!match) {
        throw new Error(
          `Invalid post path "${entry}". Expected "<category>/[<order>]<slug>.md" or "<category>/[<order>]<slug>/index.md".`,
        );
      }

      const [, category, , slug] = match;
      return `${category}/${slug}`;
    },
  }),
  schema: z.object({
    title: z.string(),
    description: z.string(),
    updated: z.string().regex(/^\d{4}-\d{2}-\d{2}$/),
    tags: z.array(z.string()),
  }),
});

export const collections = { posts };
