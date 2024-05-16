import { Database } from "@/components/component/database";
import { createFileRoute } from "@tanstack/react-router";

export const Route = createFileRoute("/historical")({
  component: Database,
});
