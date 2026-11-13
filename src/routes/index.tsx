import { createFileRoute, redirect } from "@tanstack/react-router";

// The pii-zu landing page is a static HTML file in public/piizu/.
export const Route = createFileRoute("/")({
  beforeLoad: () => {
    // 301: permanent, so Google treats the landing as the site's home page.
    throw redirect({ href: "/piizu/index.html", statusCode: 301 });
  },
  head: () => ({
    meta: [
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary_large_image" },
      { title: "pii-zü — Tapetes personalizados no Rio de Janeiro" },
      { name: "description", content: "Tapetes personalizados com logotipo, nome, cores ou desenho no Rio de Janeiro." },
      { property: "og:title", content: "pii-zü — Tapetes personalizados" },
      { property: "og:description", content: "Tapetes personalizados sob medida para empresas, condomínios, casas e escolas no Rio de Janeiro." },
    ],
  }),
});
