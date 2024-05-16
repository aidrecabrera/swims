import LandingPage from "@/page/LandingPage";
import { createLazyFileRoute } from "@tanstack/react-router";

export const Route = createLazyFileRoute("/")({
  component: LandingPage,
});
