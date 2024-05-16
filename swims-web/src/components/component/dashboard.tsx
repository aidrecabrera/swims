// App.js
import { supabase } from "@/services/supabaseClient";
import { format } from "date-fns";
import { useEffect, useState } from "react";
import {
  Area,
  AreaChart,
  CartesianGrid,
  Legend,
  Line,
  LineChart,
  ResponsiveContainer,
  Tooltip,
  XAxis,
  YAxis,
} from "recharts";
import { Card, CardContent, CardHeader } from "../ui/card";
import RecentMetricsCard from "./recent-metric-card";

export type TSwims = {
  id?: string;
  temperature?: string;
  ph?: string;
  dissolved_oxygen?: string;
  salinity?: string;
  timestamp?: any;
};

const Dashboard = () => {
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [data, setData] = useState<TSwims[]>([]);

  const fetchSwimsData = async () => {
    const { data: sensor_data, error } = await supabase
      .from("sensor_data")
      .select("*")
      .range(1000, 7000);
    if (error) {
      console.error("Error fetching data:", error.message);
    }
    return sensor_data;
  };

  useEffect(() => {
    fetchSwimsData().then((sensor_data) => {
      if (sensor_data) {
        setData(sensor_data);
      }
    });
  }, []);

  const filteredData = data.filter((item) => {
    const itemDate = new Date(item.timestamp);
    const start = startDate ? new Date(startDate) : null;
    const end = endDate ? new Date(endDate) : null;

    if (start && end) {
      return itemDate >= start && itemDate <= end;
    } else if (start) {
      return itemDate >= start;
    } else if (end) {
      return itemDate <= end;
    }
    return true;
  });

  const latestMeasurement = data[data.length - 1];

  function calculateChange(currentMeasurement: number, measurements: any[]) {
    const oneHourAgo = new Date();
    oneHourAgo.setHours(oneHourAgo.getHours() - 1);

    const lastHourMeasurement = measurements.find(
      (measurement) => new Date(measurement.timestamp) <= oneHourAgo
    );

    if (!lastHourMeasurement) {
      return 0;
    }

    const change =
      ((currentMeasurement - parseFloat(lastHourMeasurement.temperature!)) /
        parseFloat(lastHourMeasurement.temperature!)) *
      100;

    return change.toFixed(2) as any;
  }
  return (
    <div className="container p-4 mx-auto">
      {latestMeasurement && (
        <div className="grid grid-cols-1 gap-4 mb-4 sm:grid-cols-2 lg:grid-cols-4">
          <RecentMetricsCard
            key={`${latestMeasurement.id}-temperature`}
            title="Temperature"
            count={parseFloat(latestMeasurement.temperature!)}
            change={calculateChange(
              parseFloat(latestMeasurement.temperature!),
              data
            )}
          />
          <RecentMetricsCard
            key={`${latestMeasurement.id}-ph`}
            title="pH"
            count={parseFloat(latestMeasurement.ph!)}
            change={calculateChange(parseFloat(latestMeasurement.ph!), data)}
          />
          <RecentMetricsCard
            key={`${latestMeasurement.id}-dissolved_oxygen`}
            title="Dissolved Oxygen"
            count={parseFloat(latestMeasurement.dissolved_oxygen!)}
            change={calculateChange(
              parseFloat(latestMeasurement.dissolved_oxygen!),
              data
            )}
          />
          <RecentMetricsCard
            key={`${latestMeasurement.id}-salinity`}
            title="Salinity"
            count={parseFloat(latestMeasurement.salinity!)}
            change={calculateChange(
              parseFloat(latestMeasurement.salinity!),
              data
            )}
          />
        </div>
      )}
      <div className="flex flex-col items-center mb-4 sm:flex-row">
        <label htmlFor="startDate" className="mb-2 mr-2 sm:mb-0">
          Start Date:
        </label>
        <input
          type="date"
          id="startDate"
          value={startDate}
          onChange={(e) => setStartDate(e.target.value)}
          className="px-2 py-1 mb-2 border border-gray-300 rounded sm:mb-0 sm:mr-4"
        />

        <label htmlFor="endDate" className="mb-2 mr-2 sm:mb-0">
          End Date:
        </label>
        <input
          type="date"
          id="endDate"
          value={endDate}
          onChange={(e) => setEndDate(e.target.value)}
          className="px-2 py-1 border border-gray-300 rounded"
        />
      </div>
      {/* combined charts */}
      <div className="my-4">
        <Card>
          <CardHeader>
            <h2 className="mb-4 text-xl font-bold">Combined Chart</h2>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart
                margin={{
                  top: 0,
                  right: 0,
                  left: -25,
                  bottom: 0,
                }}
                data={filteredData}
              >
                <CartesianGrid strokeDasharray="3 3" />
                <XAxis
                  dataKey="timestamp"
                  tickFormatter={(value: any) =>
                    format(new Date(value), "HH:mm")
                  }
                />
                <YAxis />
                <Tooltip
                  labelFormatter={(value: any) =>
                    format(new Date(value), "yyyy-MM-dd HH:mm")
                  }
                />
                <Legend />
                <Line
                  dot={false}
                  strokeWidth={3}
                  type="monotone"
                  dataKey="temperature"
                  stroke="#8884d8"
                />
                <Line
                  dot={false}
                  strokeWidth={3}
                  type="monotone"
                  dataKey="ph"
                  stroke="#82ca9d"
                />
                <Line
                  dot={false}
                  strokeWidth={3}
                  type="monotone"
                  dataKey="dissolved_oxygen"
                  stroke="#ffc658"
                />
                <Line
                  dot={false}
                  strokeWidth={3}
                  type="monotone"
                  dataKey="salinity"
                  stroke="#ff7300"
                />
              </LineChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>
      </div>
      {/* For individual charts */}
      <div className="grid grid-cols-1 gap-4 sm:grid-cols-2 lg:grid-cols-6">
        <IndividualChart filteredData={filteredData} />
      </div>
    </div>
  );
};

export default Dashboard;

type IndividualChartProps = {
  filteredData: TSwims[];
};

const IndividualChart: React.FC<IndividualChartProps> = ({ filteredData }) => {
  const cardData = [
    {
      title: "Temperature",
      dataKey: "temperature",
      stroke: "#8884d8",
    },
    {
      title: "pH",
      dataKey: "ph",
      stroke: "#82ca9d",
    },
    {
      title: "Dissolved Oxygen",
      dataKey: "dissolved_oxygen",
      stroke: "#ffc658",
    },
    {
      title: "Salinity",
      dataKey: "salinity",
      stroke: "#ff7300",
    },
  ];

  return cardData.map((card) => (
    <Card className="col-span-3">
      <CardHeader>
        <h2 className="mb-4 text-xl font-bold">{card.title}</h2>
      </CardHeader>
      <CardContent>
        {card.dataKey === "ph" ? (
          <ResponsiveContainer width="100%" height={300}>
            <AreaChart
              margin={{
                top: 0,
                right: 0,
                left: -25,
                bottom: 0,
              }}
              data={filteredData.map((item) => ({
                ...item,
                ph: (Number(item.ph ?? 0) - 5 > 14
                  ? 14
                  : Number(item.ph ?? 0) - 5
                ).toFixed(2),
              }))}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis
                dataKey="timestamp"
                tickFormatter={(value: any) => format(new Date(value), "HH:mm")}
              />
              <YAxis domain={[0, 20]} />
              <Tooltip
                labelFormatter={(value: any) =>
                  format(new Date(value), "yyyy-MM-dd HH:mm")
                }
              />
              <Legend />
              <defs>
                <linearGradient id="splitColor" x1="0" y1="0" x2="0" y2="1">
                  <stop offset="0.5" stopColor="green" stopOpacity={1} />
                  <stop offset="0.5" stopColor="red" stopOpacity={1} />
                </linearGradient>
              </defs>
              <Area
                type="basisClosed"
                dataKey={card.dataKey}
                stroke={card.stroke}
                fill="url(#splitColor)"
              />
            </AreaChart>
          </ResponsiveContainer>
        ) : (
          <ResponsiveContainer width="100%" height={300}>
            <AreaChart
              margin={{
                top: 0,
                right: 0,
                left: -25,
                bottom: 0,
              }}
              data={filteredData}
            >
              <CartesianGrid strokeDasharray="3 3" />
              <XAxis
                dataKey="timestamp"
                tickFormatter={(value: any) => format(new Date(value), "HH:mm")}
              />
              <YAxis />
              <Tooltip
                labelFormatter={(value: any) =>
                  format(new Date(value), "yyyy-MM-dd HH:mm")
                }
              />
              <Legend />
              <Area
                type="basisClosed"
                dataKey={card.dataKey}
                stroke={card.stroke}
                fill={card.stroke}
              />
            </AreaChart>
          </ResponsiveContainer>
        )}
      </CardContent>
    </Card>
  ));
};
