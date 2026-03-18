# IoT Energy Monitoring Pipeline

[cite_start]This project demonstrates a generic IoT energy monitoring pipeline where simulated devices measure electrical parameters and send telemetry data through a messaging system into a time-series database for visualization and analysis.

## 🏗️ Architecture Overview
[cite_start]The system follows a decoupled architecture pattern used in industrial smart grid systems[cite: 11]:
1. [cite_start]**IoT Energy Meter (Simulated)**: A Python script that measures electrical parameters ($V$, $I$, $f$, $PF$), calculates power ($P = V \times I$), and packages telemetry data[cite: 16, 17, 74].
2. [cite_start]**Message Broker (MQTT)**: Uses Eclipse Mosquitto to buffer incoming telemetry and enable asynchronous communication[cite: 7, 27, 28].
3. [cite_start]**Ingestion Service**: A Python-based service that subscribes to streams, validates data, and stores measurements in a database[cite: 37, 38, 39].
4. [cite_start]**Time-Series Database (InfluxDB)**: Optimized storage for time-based electrical measurements[cite: 41, 42].
5. [cite_start]**Visualization Dashboard (Grafana)**: Real-time monitoring of power consumption, voltage stability, and energy trends[cite: 51, 56, 58].

## 📊 Telemetry Data Fields
[cite_start]The typical telemetry message contains[cite: 61]:
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
