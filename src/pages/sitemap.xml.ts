import { existsSync } from "node:fs";
import { resolve } from "node:path";
import { getCollection } from "astro:content";
import menu from "../data/menu.json";

const siteURL = "https://znkblog.github.io";

function escapeXml(value: string) {
  return value
    .replaceAll("&", "&amp;")
    .replaceAll("<", "&lt;")
    .replaceAll(">", "&gt;")
    .replaceAll('"', "&quot;")
    .replaceAll("'", "&apos;");
}

export async function GET() {
  const posts = await getCollection("posts");
  const allowedCategories = new Set<string>();
  const urls = new Map<string, string | undefined>([[`${siteURL}`, undefined]]);

  for (const { category, order } of menu) {
    if (!/^[\w-]+$/.test(category)) {
      throw new Error(`Invalid category "${category}" in src/data/menu.json.`);
    }

    if (order !== "asc" && order !== "desc") {
      throw new Error(`Invalid order "${order}" for category "${category}".`);
    }

    if (!existsSync(resolve(process.cwd(), "content", category))) {
      continue;
    }

    allowedCategories.add(category);
    urls.set(`${siteURL}/category/${encodeURIComponent(category)}`, undefined);
  }

  for (const post of posts) {
    const separatorIndex = post.id.indexOf("/");

    if (separatorIndex === -1) {
      throw new Error(`Invalid post ID "${post.id}". Expected "<category>/<slug>".`);
    }

    const slug = post.id.slice(separatorIndex + 1);
    const postURL = `${siteURL}/post/${encodeURIComponent(slug)}`;
    urls.set(postURL, post.data.updated);
  }

  const entries = Array.from(urls, ([url, lastModified]) => {
    const lastmod = lastModified ? `<lastmod>${lastModified}</lastmod>` : "";
    return `<url><loc>${escapeXml(url)}</loc>${lastmod}</url>`;
  }).join("");

  return new Response(
    `<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">${entries}</urlset>`,
    { headers: { "Content-Type": "application/xml; charset=utf-8" } },
  );
}
