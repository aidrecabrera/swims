// App.js
import { format } from "date-fns";
import { useState } from "react";
import {
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

const Dashboard = () => {
  const [startDate, setStartDate] = useState("");
  const [endDate, setEndDate] = useState("");

  // Mock data for testing purposes
  const data = [
    {
      id: "33679",
      temperature: "33",
      ph: "6",
      dissolved_oxygen: "11.33",
      salinity: "0.09",
      timestamp: "2024-05-13 09:03:10+00",
    },
  ];

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

  return (
    <div className="container p-4 mx-auto">
      <div className="grid grid-cols-1 gap-4 mb-4 sm:grid-cols-2 lg:grid-cols-4">
        <RecentMetricsCard
          key={`${latestMeasurement.id}-temperature`}
          title="Temperature"
          count={parseFloat(latestMeasurement.temperature)}
          change={0} // replace with actual change value
        />
        <RecentMetricsCard
          key={`${latestMeasurement.id}-ph`}
          title="pH"
          count={parseFloat(latestMeasurement.ph)}
          change={0} // replace with actual change value
        />
        <RecentMetricsCard
          key={`${latestMeasurement.id}-dissolved_oxygen`}
          title="Dissolved Oxygen"
          count={parseFloat(latestMeasurement.dissolved_oxygen)}
          change={0} // replace with actual change value
        />
        <RecentMetricsCard
          key={`${latestMeasurement.id}-salinity`}
          title="Salinity"
          count={parseFloat(latestMeasurement.salinity)}
          change={0} // replace with actual change value
        />
      </div>
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
      {/* For combined charts */}
      <div>
        <div className="my-4">
          <Card>
            <CardHeader>
              <h2 className="mb-4 text-xl font-bold">Combined Chart</h2>
            </CardHeader>
            <CardContent>
              <ResponsiveContainer width="100%" height={300}>
                <LineChart data={filteredData}>
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
                    type="monotone"
                    dataKey="temperature"
                    stroke="#8884d8"
                  />
                  <Line type="monotone" dataKey="ph" stroke="#82ca9d" />
                  <Line
                    type="monotone"
                    dataKey="dissolved_oxygen"
                    stroke="#ffc658"
                  />
                  <Line type="monotone" dataKey="salinity" stroke="#ff7300" />
                </LineChart>
              </ResponsiveContainer>
            </CardContent>
          </Card>
        </div>
      </div>
      {/* For individual charts */}
      <div className="grid grid-cols-1 gap-4 md:grid-cols-2">
        <Card>
          <CardHeader>
            <h2 className="mb-4 text-xl font-bold">Temperature</h2>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={filteredData}>
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
                <Line type="monotone" dataKey="temperature" stroke="#8884d8" />
              </LineChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <h2 className="mb-4 text-xl font-bold">pH</h2>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={filteredData}>
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
                <Line type="monotone" dataKey="ph" stroke="#82ca9d" />
              </LineChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>

        <Card>
          <CardHeader>
            <h2 className="mb-4 text-xl font-bold">Dissolved Oxygen</h2>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={filteredData}>
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
                  type="monotone"
                  dataKey="dissolved_oxygen"
                  stroke="#ffc658"
                />
              </LineChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>
        <Card>
          <CardHeader>
            <h2 className="mb-4 text-xl font-bold">Salinity</h2>
          </CardHeader>
          <CardContent>
            <ResponsiveContainer width="100%" height={300}>
              <LineChart data={filteredData}>
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
                <Line type="monotone" dataKey="salinity" stroke="#ff7300" />
              </LineChart>
            </ResponsiveContainer>
          </CardContent>
        </Card>
      </div>
    </div>
  );
};

export default Dashboard;
