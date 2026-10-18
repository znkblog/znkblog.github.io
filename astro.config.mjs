import { defineConfig } from "astro/config";
import { unified } from "@astrojs/markdown-remark";

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
            { type: "text", value: "AdSense 광고 영역" },
            { type: "element", tagName: "br", properties: {}, children: [] },
            { type: "text", value: "100% × 250" },
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
  markdown: {
    processor: unified({ rehypePlugins: [rehypeReplaceAdsense] }),
  },
});
