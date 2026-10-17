import { createFileRoute, redirect } from "@tanstack/react-router";

// The Tapetto landing page is a static HTML file in public/tapetto/.
export const Route = createFileRoute("/")({
  beforeLoad: () => {
    throw redirect({ href: "/tapetto/index.html" });
  },
  head: () => ({
    meta: [
      { title: "Tapetto — Tapetes e capachos personalizados no Rio de Janeiro" },
      { name: "description", content: "Tapetes e capachos personalizados e grama sintética no Rio de Janeiro." },
      { property: "og:title", content: "Tapetto — Tapetes e capachos personalizados" },
      { property: "og:description", content: "Tapetes e capachos personalizados e grama sintética no Rio de Janeiro." },
    ],
  }),
});
