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
import { Button } from "../ui/button";
import { Card, CardContent, CardHeader } from "../ui/card";
import RecentMetricsCard from "./recent-metric-card";

export type TSwims = {
  id?: string;
  temperature?: string;
  ph?: string | number;
  dissolved_oxygen?: string;
  salinity?: string;
  timestamp?: any;
};

const Dashboard = () => {
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");
  const [data, setData] = useState<TSwims[]>([]);
  const [calibrationValues, setCalibrationValues] = useState({
    ph: 5,
    temperature: 0,
    dissolved_oxygen: 0,
    salinity: 0,
  });

  const fetchSwimsData = async () => {
    let sensorData = localStorage.getItem("sensorData");
    if (sensorData) {
      return JSON.parse(sensorData);
    } else {
      const { data: sensorData, error } = await supabase
        .from("sensor_data")
        .select("*");

      if (error) {
        console.error("Error fetching data:", error.message);
      } else {
        localStorage.setItem("sensorData", JSON.stringify(sensorData));
      }

      return sensorData;
    }
  };

  useEffect(() => {
    fetchSwimsData().then((sensorData) => {
      if (Array.isArray(sensorData)) {
        sensorData = sensorData.map((data: TSwims) => {
          if (data.ph) {
            data.ph = (Number(data.ph) - calibrationValues.ph).toFixed(2);
          }
          if (data.temperature) {
            data.temperature = (
              Number(data.temperature) + calibrationValues.temperature
            ).toFixed(2);
          }
          if (data.dissolved_oxygen) {
            data.dissolved_oxygen = (
              Number(data.dissolved_oxygen) + calibrationValues.dissolved_oxygen
            ).toFixed(2);
          }
          if (data.salinity) {
            data.salinity = (
              Number(data.salinity) + calibrationValues.salinity
            ).toFixed(2);
          }
          return data;
        });
        setData(sensorData);
      }
    });
  }, [calibrationValues]);

  const handleCalibration = (type: keyof typeof calibrationValues) => {
    const newCalibrationValue = prompt(
      `Enter new calibration value for ${type}:`
    );
    if (newCalibrationValue) {
      setCalibrationValues((prevValues) => ({
        ...prevValues,
        [type]: Number(newCalibrationValue),
      }));
    }
  };

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

  const calculateChange = (
    currentMeasurement: number,
    measurements: TSwims[]
  ) => {
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

    return change.toFixed(2);
  };

  return (
    <div className="container p-4 mx-auto">
      {latestMeasurement && (
        <div className="grid grid-cols-1 gap-4 mb-4 sm:grid-cols-2 lg:grid-cols-4">
          <RecentMetricsCard
            key={`${latestMeasurement.id}-temperature`}
            title="Temperature"
            count={parseFloat(latestMeasurement.temperature!)}
            change={
              calculateChange(
                parseFloat(latestMeasurement.temperature!),
                data
              ) as any
            }
          />
          <RecentMetricsCard
            key={`${latestMeasurement.id}-ph`}
            title="pH"
            count={parseFloat(latestMeasurement.ph! as string)}
            change={
              calculateChange(
                parseFloat(latestMeasurement.ph! as string),
                data
              ) as any
            }
          />
          <RecentMetricsCard
            key={`${latestMeasurement.id}-dissolved_oxygen`}
            title="Dissolved Oxygen"
            count={parseFloat(latestMeasurement.dissolved_oxygen!)}
            change={
              calculateChange(
                parseFloat(latestMeasurement.dissolved_oxygen!),
                data
              ) as any
            }
          />
          <RecentMetricsCard
            key={`${latestMeasurement.id}-salinity`}
            title="Salinity"
            count={parseFloat(latestMeasurement.salinity!)}
            change={
              calculateChange(
                parseFloat(latestMeasurement.salinity!),
                data
              ) as any
            }
          />
        </div>
      )}

      <div className="flex flex-col justify-between lg:flex-row">
        <div className="flex flex-row items-center gap-2 mb-4 md:flex-row lg:flex-row sm:flex-row">
          <div>
            <label htmlFor="startDate" className="mb-0 mr-2 sm:mb-0">
              Start Date:
            </label>
            <input
              type="date"
              id="startDate"
              value={startDate}
              onChange={(e) => setStartDate(e.target.value)}
              className="px-2 border border-gray-300 rounded sm:mb-0 sm:mr-4"
            />
          </div>
          <div>
            <label htmlFor="endDate" className="mb-0 mr-2 sm:mb-0">
              End Date:
            </label>
            <input
              type="date"
              id="endDate"
              value={endDate}
              onChange={(e) => setEndDate(e.target.value)}
              className="px-2 border border-gray-300 rounded"
            />
          </div>
        </div>
        <div className="flex gap-2">
          <Button onClick={() => handleCalibration("ph")}>
            Calibrate pH: {calibrationValues.ph}
          </Button>
          <Button onClick={() => handleCalibration("temperature")}>
            Calibrate Temperature: {calibrationValues.temperature}
          </Button>
          <Button onClick={() => handleCalibration("dissolved_oxygen")}>
            Calibrate Dissolved Oxygen: {calibrationValues.dissolved_oxygen}
          </Button>
          <Button onClick={() => handleCalibration("salinity")}>
            Calibrate Salinity: {calibrationValues.salinity}
          </Button>
        </div>
      </div>

      {/* Combined charts */}
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

      {/* Individual charts */}
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
    { title: "pH", dataKey: "ph", stroke: "#82ca9d" },
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
    <Card key={card.title} className="col-span-3">
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
              <YAxis
                domain={
                  card.dataKey === "temperature"
                    ? [0, 80]
                    : card.dataKey === "ph"
                      ? [0, 14]
                      : card.dataKey === "dissolved_oxygen"
                        ? [0, 20]
                        : [0, 30]
                }
              />
              <Tooltip
                labelFormatter={(value: any) =>
                  format(new Date(value), "yyyy-MM-dd HH:mm")
                }
              />
              <Legend />
              <Area
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
