# IoT Energy Monitoring Pipeline

This project demonstrates a generic IoT energy monitoring pipeline where simulated devices measure electrical parameters and send telemetry data through a messaging system into a time-series database for visualization and analysis.

## 🏗️ Architecture Overview
The system follows a decoupled architecture pattern used in industrial smart grid systems:
1. **IoT Energy Meter (Simulated)**: A Python script that measures electrical parameters ($V$, $I$, $f$, $PF$), calculates power ($P = V \times I$), and packages telemetry data.
2. **Message Broker (MQTT)**: Uses Eclipse Mosquitto to buffer incoming telemetry and enable asynchronous communication.
3. **Ingestion Service**: A Python-based service that subscribes to streams, validates data, and stores measurements in a database.
4. **Time-Series Database (InfluxDB)**: Optimized storage for time-based electrical measurements.
5. **Visualization Dashboard (Grafana)**: Real-time monitoring of power consumption, voltage stability, and energy trends.

## 📊 Telemetry Data Fields
The typical telemetry message contains:
- `device_id`: Unique meter identifier.
- `voltage`: Electrical voltage (V).
- `current`: Electrical current (A).
- `power`: Active power consumption (W).
- `energy`: Accumulated energy usage (kWh).
- `power_factor`: Efficiency of electrical load.
- `frequency`: Grid frequency (Hz).

## 🚀 Getting Started

### Prerequisites
- Docker & Docker Desktop
- Python 3.12+

### Setup Instructions
1. **Clone the repository**:
   ```bash
   git clone https://github.com/EvoVincere/IOT-project.git
   cd IOT-project
   ```
🛠️ How to Run the Pipeline
Follow these steps to get the energy monitoring system up and running on your local machine:

1. Setup Infrastructure
   First, ensure your Docker containers are running to provide the message broker, database, and dashboard services:
      ```bash
      docker-compose up -d
      ```
   Verify that all containers (mqtt_broker, ts_database, and viz_dashboard) are active using docker ps.

2. Environment Configuration
Create a .env file in the root folder and fill it with your specific InfluxDB and Grafana credentials. This keeps your sensitive tokens safe and out of the public source code.

3. Start the Ingestion Service
   Open a terminal and run the ingestion script. This service will wait for telemetry data from the broker and write it to InfluxDB:
   ```bash
   python3 ingestion_service.py
   ```
4. Launch the Energy Simulator
   Open a new terminal and start the device simulator. You will see it begin to transmit electrical measurements like voltage, current, and power:
   ```bash
   python3 simulator.py
   ```
   The simulator uses the standard electrical formula to calculate active power: $P = V \times I$.
5. Access Dashboard
   Once the data is flowing, you can monitor the results in real-time:
   - InfluxDB Data Explorer: Visit http://localhost:8086 to verify the raw time-series data storage.
   - Grafana Visualization: Visit http://localhost:3000 to view the graphical trends of energy consumption and power stability.
  
