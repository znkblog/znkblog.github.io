import { defineConfig } from "astro/config";
import { unified } from "@astrojs/markdown-remark";
import githubLight from "@shikijs/themes/github-light";

const codeTheme = {
  ...githubLight,
  name: "github-light-blockquote",
  colors: {
    ...githubLight.colors,
    "editor.background": "#f5f0e7",
  },
};

function rehypeReplaceAdsense() {
  return (tree) => {
    function replaceMarker(node) {
      if (!node.children) return;

      node.children = node.children.map((child) => {
        const isAdsenseMarker =
          (child.type === "comment" && child.value === "adsense") ||
          (child.type === "raw" && child.value === "<!--adsense-->");

        if (!isAdsenseMarker) return child;

        return {
          type: "element",
          tagName: "div",
          properties: { className: ["adsense-placeholder2"] },
          children: [
            { type: "text", value: "예비 영역" },
            { type: "element", tagName: "br", properties: {}, children: [] },
            { type: "text", value: "100% x 250" },
          ],
        };
      });

      node.children.forEach(replaceMarker);
    }

    replaceMarker(tree);
  };
}

export default defineConfig({
  site: "https://znkblog.github.io",
  trailingSlash: "never",
  build: {
    format: "file",
  },
  vite: {
    server: {
      proxy: {
        "/stat": {
          target: "https://znkblog.github.io",
          changeOrigin: true,
          secure: true,
        },
      },
    },
  },
  markdown: {
    shikiConfig: { theme: codeTheme },
    processor: unified({ rehypePlugins: [rehypeReplaceAdsense] }),
  },
});
