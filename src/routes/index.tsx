import { createFileRoute, redirect } from "@tanstack/react-router";

// The Tapetto landing page is a static HTML file in public/tapetto/.
export const Route = createFileRoute("/")({
  beforeLoad: () => {
    throw redirect({ href: "/tapetto/index.html" });
  },
  head: () => ({
    meta: [
      { property: "og:type", content: "website" },
      { name: "twitter:card", content: "summary_large_image" },
      { title: "Tapetto — Tapetes personalizados no Rio de Janeiro" },
      { name: "description", content: "Tapetes personalizados com logotipo, nome, cores ou desenho no Rio de Janeiro." },
      { property: "og:title", content: "Tapetto — Tapetes personalizados" },
      { property: "og:description", content: "Tapetes personalizados sob medida para empresas, condomínios, casas e escolas no Rio de Janeiro." },
    ],
  }),
});
