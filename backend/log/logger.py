import os
import subprocess
from supabase import create_client, Client
from dotenv import load_dotenv
import sqlalchemy as sa
from sqlalchemy import Table, MetaData, select, insert
from monitor.monitor import SensorDataMonitor

load_dotenv()

SUPABASE_URL = "https://kpypbiqtjzcctqrcrnwt.supabase.co"
SUPABASE_KEY = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJzdXBhYmFzZSIsInJlZiI6ImtweXBiaXF0anpjY3RxcmNybnd0Iiwicm9sZSI6ImFub24iLCJpYXQiOjE3MTQ4MjQ5NDcsImV4cCI6MjAzMDQwMDk0N30.NqOmREZ7PNWhXOAOarrcvGOyzC7Xhch_ThwOOt4z1rA"

url: str = SUPABASE_URL
key: str = SUPABASE_KEY
supabase: Client = create_client(url, key)


class SensorDataLogger:
    """
    A class for logging sensor data to a local database and syncing with Supabase.

    Args:
        db_url (str): The URL of the local database.

    Attributes:
        engine (sqlalchemy.engine.Engine): The local database engine.
        metadata (sqlalchemy.MetaData): The metadata of the local database.
        sensor_data (sqlalchemy.Table): The table for storing sensor data in the local database.
        anomaly_logs (sqlalchemy.Table): The table for storing anomaly logs in the local database.
        monitor (SensorDataMonitor): The sensor data monitor instance.

    """

    def __init__(self, db_url):
        self.engine = sa.create_engine(db_url)
        self.metadata = MetaData()
        self.sensor_data = Table('sensor_data', self.metadata, autoload_with=self.engine)
        self.anomaly_logs = Table('anomaly_logs', self.metadata, autoload_with=self.engine)
        self.monitor = SensorDataMonitor()

    def sync_to_supabase(self):
        """
        Synchronize the local database with the Supabase database.
        """
        if subprocess.check_output(["ping", "-c", "1", "8.8.8.8"]):
            print("Syncing to server.")
            with self.engine.connect() as conn:
                logs_result = conn.execute(select(self.sensor_data))
                logs_anomaly_result = conn.execute(select(self.anomaly_logs))

                sensor_data = [
                    {
                        "id": log.id,
                        "timestamp": log.timestamp.isoformat(),
                        "temperature": log.temperature,
                        "ph": log.ph,
                        "dissolved_oxygen": log.dissolved_oxygen,
                        "salinity": log.salinity,
                    }
                    for log in logs_result
                ]

                anomaly_data = [
                    {
                        "id": log.id,
                        "timestamp": log.timestamp.isoformat(),
                        "temperature": log.temperature,
                        "ph": log.ph,
                        "dissolved_oxygen": log.dissolved_oxygen,
                        "salinity": log.salinity,
                    }
                    for log in logs_anomaly_result
                ]

                if sensor_data:
                    supabase.table('sensor_data').upsert(sensor_data, ignore_duplicates=True).execute()
                if anomaly_data:
                    supabase.table('anomaly_logs').upsert(anomaly_data, ignore_duplicates=True).execute()
        else:
            print("No internet connection. Skipping synchronization to server.")

    def log(self, temperature, ph, dissolved_oxygen, salinity):
        """
        Log sensor data to the local database.

        Args:
            temperature (float): The temperature value.
            ph (float): The pH value.
            dissolved_oxygen (float): The dissolved oxygen value.
            salinity (float): The salinity value.

        Returns:
            sqlalchemy.sql.dml.Insert: The insert query.
        """
        query = insert(self.sensor_data).values(
            temperature=temperature,
            ph=ph,
            dissolved_oxygen=str(dissolved_oxygen),
            salinity=salinity
        )
        return query

    def log_anomaly(self, temperature, ph, dissolved_oxygen, salinity):
        """
        Log an anomaly in the sensor data to the anomaly_logs table.

        Args:
            temperature (float): The temperature value.
            ph (float): The pH value.
            dissolved_oxygen (float): The dissolved oxygen value.
            salinity (float): The salinity value.

        Returns:
            sqlalchemy.sql.dml.Insert: The insert query.
        """
        if not (self.monitor.check_parameter_level('temperature', temperature) and
                self.monitor.check_parameter_level('ph', ph) and
                self.monitor.check_parameter_level('dissolved_oxygen', dissolved_oxygen) and
                self.monitor.check_parameter_level('salinity', salinity)):
            anomaly_query = insert(self.anomaly_logs).values(
                temperature=temperature,
                ph=ph,
                dissolved_oxygen=str(dissolved_oxygen),
                salinity=salinity
            )
            return anomaly_query
        else:
            return None

    def execute_queries(self, queries):
        """
        Execute multiple database queries in a single transaction.

        Args:
            queries (list): A list of SQLAlchemy queries to execute.

        """
        with self.engine.begin() as conn:
            for query in queries:
                conn.execute(query)