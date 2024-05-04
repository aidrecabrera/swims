import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from sqlalchemy import create_engine, Column, Integer, Float, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime, timedelta
import matplotlib.dates as mdates
import time

Base = declarative_base()

class SensorData(Base):
    __tablename__ = 'sensor_data'
    id = Column(Integer, primary_key=True)
    temperature = Column(Float)
    ph = Column(Float)
    dissolved_oxygen = Column(Float)
    salinity = Column(Float)
    timestamp = Column(DateTime)

engine = create_engine('sqlite:///swims_log.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

root = tk.Tk()
root.title("Real-time Sensor Data Graph")

fig, ax = plt.subplots()
canvas = FigureCanvasTkAgg(fig, master=root)
plot_widget = canvas.get_tk_widget()
plot_widget.pack(side=tk.TOP, fill=tk.BOTH, expand=1)

def query_recent_data():
    end_time = datetime.now()
    start_time = end_time - timedelta(minutes=60)
    query = session.query(SensorData).filter(SensorData.timestamp.between(start_time, end_time)).all()
    return query

def update_plot():
    data = query_recent_data()
    timestamps = [record.timestamp for record in data]
    temperatures = [record.temperature for record in data]
    ax.clear()
    ax.plot(timestamps, temperatures, marker='o', linestyle='-')
    ax.xaxis.set_major_formatter(mdates.DateFormatter('%H:%M:%S'))
    ax.set_xlabel("Timestamp")
    ax.set_ylabel("Temperature")
    ax.set_title("Real-time Temperature Data")
    ax.grid(True)
    fig.autofmt_xdate()
    canvas.draw()
    root.after(10000, update_plot) 

update_plot()

root.mainloop()
