import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card";

interface RecentMetricsCardProps {
  title: string;
  count: number;
  change: number;
}

interface Thresholds {
  [key: string]: number[];
  ph: number[];
  salinity: number[];
  dissolved_oxygen: number[];
  temperature: number[];
}

const THRESHOLDS: Thresholds = {
  ph: [6.5, 9.0],
  salinity: [4.5, 5.5],
  dissolved_oxygen: [4.8, 5.2],
  temperature: [25.0, 32.0],
};

export default function RecentMetricsCard({
  title,
  count,
  change,
}: RecentMetricsCardProps) {
  const isOutOfRange = (title: string, count: number) => {
    const [min, max] = THRESHOLDS[title.toLowerCase()] || [];
    return count < min || count > max;
  };

  const getStatusMessage = (title: string, count: number) => {
    return isOutOfRange(title, count)
      ? `${title} Status: Abnormal`
      : `${title} Status: Normal`;
  };

  return (
    <Card className="flex-grow">
      <CardHeader className="flex flex-row items-center justify-between pb-2 space-y-0">
        <CardTitle className="text-sm font-medium">{title}</CardTitle>
      </CardHeader>
      <CardContent>
        <div
          className={`text-2xl font-bold ${isOutOfRange(title, count) ? "text-red-500" : "text-green-500"}`}
        >
          {count}
        </div>
        <p className="text-xs text-muted-foreground">
          {change}% change since last hour
        </p>
        <p
          className={`text-xs ${isOutOfRange(title, count) ? "text-red-500" : "text-green-500"}`}
        >
          {getStatusMessage(title, count)}
        </p>
      </CardContent>
    </Card>
  );
}
