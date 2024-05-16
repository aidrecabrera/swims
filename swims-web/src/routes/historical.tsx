import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/historical")({
  component: () => <div>Hello /historical!</div>,
});
