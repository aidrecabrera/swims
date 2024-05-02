import sqlalchemy as sa
from sqlalchemy import Table, MetaData

import sqlalchemy as sa
from sqlalchemy import MetaData, Table

class SensorDataLogger:
    """
    A class for logging sensor data to a database.

    Args:
        db_url (str): The URL of the database.

    Attributes:
        engine (sqlalchemy.engine.Engine): The database engine.
        connection (sqlalchemy.engine.Connection): The database connection.
        metadata (sqlalchemy.MetaData): The metadata of the database.
        sensor_data (sqlalchemy.Table): The table for storing sensor data.

    """

    def __init__(self, db_url):
        self.engine = sa.create_engine(db_url)
        self.connection = self.engine.connect()
        self.metadata = MetaData()
        self.sensor_data = Table('sensor_data', self.metadata, autoload_with=self.engine)

    def log(self, temperature, ph, dissolved_oxygen, salinity):
        """
        Log sensor data to the database.

        Args:
            temperature (float): The temperature value.
            ph (float): The pH value.
            dissolved_oxygen (float): The dissolved oxygen value.
            salinity (float): The salinity value.

        Returns:
            sqlalchemy.sql.dml.Insert: The insert query.

        """
        query = sa.insert(self.sensor_data).values(
            temperature=temperature,
            ph=ph,
            dissolved_oxygen=str(dissolved_oxygen),  # convert to string
            salinity=salinity
        )
        return query

    def get_logs(self):
        """
        Get all sensor data logs from the database.

        Returns:
            sqlalchemy.sql.selectable.Select: The select query.

        """
        query = sa.select(self.sensor_data)
        return query

    def get_logs_by_timestamp(self, timestamp):
        """
        Get sensor data logs from the database based on timestamp.

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