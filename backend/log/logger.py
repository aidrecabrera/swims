import os
from supabase import create_client, Client
from dotenv import load_dotenv
import datetime
import sys
import sqlalchemy as sa
from sqlalchemy import Table, MetaData

load_dotenv()

url: str = os.environ.get("SUPABASE_URL")
key: str = os.environ.get("SUPABASE_KEY")
supabase: Client = create_client(url, key)


class SensorDataLogger:
    """
    A class for logging sensor data to a local database and syncing with Supabase.

    Args:
        db_url (str): The URL of the local database.

    Attributes:
        engine (sqlalchemy.engine.Engine): The local database engine.
        connection (sqlalchemy.engine.Connection): The local database connection.
        metadata (sqlalchemy.MetaData): The metadata of the local database.
        sensor_data (sqlalchemy.Table): The table for storing sensor data in the local database.

    """ 

    def __init__(self, db_url):
        self.engine = sa.create_engine(db_url)
        self.connection = self.engine.connect()
        self.metadata = MetaData()
        self.sensor_data = Table('sensor_data', self.metadata, autoload_with=self.engine)

    def sync_to_supabase(self):
        """
        Synchronize the local database with the Supabase database.
        """
        # execute the query to retrieve logs from the local database
        logs_result = self.execute_query(self.get_logs())

        if logs_result:
            for log in logs_result:
                data = {
                    "id": log.id,
                    "timestamp": log.timestamp.isoformat(),
                    "temperature": log.temperature,
                    "ph": log.ph,
                    "dissolved_oxygen": log.dissolved_oxygen,
                    "salinity": log.salinity,
                }
                # upsert the log to the Supabase database
                supabase.table('sensor_data').upsert(data, ignore_duplicates=True).execute()    



    def log(self, temperature, ph, dissolved_oxygen, salinity):
        """
        Log sensor data to the local database.

        Args:
            temperature (float): The temperature value.
            ph (float): The pH value.
            dissolved_oxygen (float): The dissolved oxygen value.
            salinity (float): The salinity value.
            timestamp (datetime.datetime, optional): The timestamp of the log. If None, the current time is used.

        Returns:
            sqlalchemy.sql.dml.Insert: The insert query.
        """

        query = sa.insert(self.sensor_data).values(
            temperature=temperature,
            ph=ph,
            dissolved_oxygen=str(dissolved_oxygen),
            salinity=salinity
        )
        return query

    def get_logs(self):
        """
        Get all sensor data logs from the local database.

        Returns:
            sqlalchemy.sql.selectable.Select: The select query.

        """
        query = sa.select(self.sensor_data)
        return query

    def get_logs_by_timestamp(self, timestamp):
        """
        Get sensor data logs from the local database based on timestamp.

        Args:
            timestamp (datetime.datetime): The timestamp to filter the logs.

        Returns:
            sqlalchemy.sql.selectable.Select: The select query.

        """
        query = sa.select(self.sensor_data).where(self.sensor_data.c.timestamp == timestamp)
        return query

    def execute_query(self, query):
        """
        Execute a database query.

        Args:
            query (sqlalchemy.sql.expression.Executable): The query to execute.

        Returns:
            list or None: The query result as a list of rows, or None if the query is not a select query.

        """
        with self.connection.begin():
            result = self.connection.execute(query)
            if isinstance(query, sa.sql.selectable.Select):
                return result.fetchall()
            else:
                return None
