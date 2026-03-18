import os
from dotenv import load_dotenv
import paho.mqtt.client as mqtt
from influxdb_client import InfluxDBClient, Point, WritePrecision
from influxdb_client.client.write_api import SYNCHRONOUS
import json

load_dotenv()

# Konfigurasi InfluxDB
INFLUX_URL = "http://localhost:8086"
INFLUX_TOKEN = os.getenv("INFLUXDB_TOKEN")
INFLUX_ORG = os.getenv("INFLUXDB_ORG")
INFLUX_BUCKET = os.getenv("INFLUXDB_BUCKET")

# Konfigurasi MQTT
MQTT_BROKER = "localhost"
MQTT_TOPIC = "energy/telemetry"

# Setup InfluxDB Client
db_client = InfluxDBClient(url=INFLUX_URL, token=INFLUX_TOKEN, org=INFLUX_ORG)
write_api = db_client.write_api(write_options=SYNCHRONOUS)

def on_message(client, userdata, msg):
    try:
        # 1. Terima & Transform Data [cite: 35, 38]
        data = json.loads(msg.payload.decode())
        print(f"Menerima telemetry dari {data['device_id']}")

        # 2. Siapkan Point Data untuk InfluxDB [cite: 43]
        point = Point("electrical_measurements") \
            .tag("device_id", data['device_id']) \
            .field("voltage", float(data['voltage'])) \
            .field("current", float(data['current'])) \
            .field("power", float(data['power'])) \
            .field("energy", float(data['energy'])) \
            .field("power_factor", float(data['power_factor'])) \
            .field("frequency", float(data['frequency']))

        # 3. Simpan ke Database [cite: 39, 42]
        write_api.write(bucket=INFLUX_BUCKET, org=INFLUX_ORG, record=point)
        
    except Exception as e:
        print(f"Error processing message: {e}")

# Setup MQTT Client
mqtt_client = mqtt.Client()
mqtt_client.on_message = on_message
mqtt_client.connect(MQTT_BROKER, 1883)
mqtt_client.subscribe(MQTT_TOPIC)

print("Ingestion Service berjalan... Menunggu data dari Broker.")
mqtt_client.loop_forever()