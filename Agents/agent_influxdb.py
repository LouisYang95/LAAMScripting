#!/usr/bin/python3
import datetime
import time
import psutil
import influxdb_client
import os
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS

token = os.environ.get("INFLUXDB_TOKEN")
org = "LAAMScripting"
url = "http://10.57.33.13:8086"

write_client = influxdb_client.InfluxDBClient(url=url, token="jYG7wF2aNGq9FSw_1fdOcZcJchjV2-7fSxPeqULTGzMjkK964W6G9LM5Cz1DpETI4YiIi3UHdJTGth9sqvzDfA==", org=org)
bucket = "ScriptAdmin"

write_api = write_client.write_api(write_options=SYNCHRONOUS)

try:
    COUNT = 1

    while True:
        if COUNT == 1:
            cpu_times = psutil.cpu_times_percent(interval=0, percpu=False)
            point = (
                Point("cpu_usage")
                .field("user", cpu_times.user)
                .field("system", cpu_times.system)
                .field("idle", cpu_times.idle)
            )
            write_api.write(bucket=bucket, org=org, record=point)
            COUNT += 1
            time.sleep(10)
        elif COUNT == 2:
            virtual_memory = psutil.virtual_memory()
            used_memory_percent = (virtual_memory.total - virtual_memory.available) / virtual_memory.total * 100
            point = (
                Point("memory_usage")
                .field("used_percent", used_memory_percent)
            )
            write_api.write(bucket=bucket, org=org, record=point)
            COUNT += 1
            time.sleep(10)
        elif COUNT == 3:
            disk_io = psutil.disk_io_counters(perdisk=False, nowrap=True)
            point = (
                Point("disk_io")
                .field("read_count", disk_io.read_count)
                .field("write_count", disk_io.write_count)
                .field("read_bytes", disk_io.read_bytes)
                .field("write_bytes", disk_io.write_bytes)
            )
            write_api.write(bucket=bucket, org=org, record=point)
            COUNT += 1
            time.sleep(10)
        elif COUNT == 4:
            net_io = psutil.net_io_counters()
            point = (
                Point("network_io")
                .field("bytes_sent", net_io.bytes_sent)
                .field("bytes_recv", net_io.bytes_recv)
                .field("packets_sent", net_io.packets_sent)
                .field("packets_recv", net_io.packets_recv)
            )
            write_api.write(bucket=bucket, org=org, record=point)
            COUNT = 1
            time.sleep(10)

except Exception as e:
    print(str(e).capitalize())
except KeyboardInterrupt:
    print("Finished")
