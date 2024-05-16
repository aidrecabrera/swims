import { Activity } from "lucide-react";

import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface RecentMetricsCardProps {
  title: string;
  count: number;
  change: number;
}

export default function RecentMetricsCard({
  title,
  count,
  change,
}: RecentMetricsCardProps) {
  return (
    <Card className="flex-grow">
      <CardHeader className="flex flex-row items-center justify-between pb-2 space-y-0">
        <CardTitle className="text-sm font-medium">{title}</CardTitle>
        <Activity className="w-4 h-4 text-muted-foreground" />
      </CardHeader>
      <CardContent>
        <div className="text-2xl font-bold">{count}</div>
        <p className="text-xs text-muted-foreground">
          {change} since last hour
        </p>
      </CardContent>
    </Card>
  );
}
