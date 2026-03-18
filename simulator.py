import paho.mqtt.client as mqtt
import json
import time
import random

# Konfigurasi Broker
MQTT_BROKER = "localhost"
MQTT_PORT = 1883
MQTT_TOPIC = "energy/telemetry"

client = mqtt.Client()
client.connect(MQTT_BROKER, MQTT_PORT, 60)

print("Simulasi Perangkat Energi Dimulai... Tekan Ctrl+C untuk berhenti.")

try:
    energy_accumulated = 15.0 # Memulai dari nilai awal [cite: 69]
    
    while True:
        # 1. Simulasi Parameter Listrik [cite: 61]
        voltage = round(random.uniform(220, 240), 1)  # Volt (V) [cite: 61, 66]
        current = round(random.uniform(1, 10), 2)    # Ampere (A) [cite: 61, 67]
        frequency = round(random.uniform(49.5, 50.5), 1) # Hertz (Hz) [cite: 61, 71]
        power_factor = round(random.uniform(0.8, 0.98), 2) # Efficiency [cite: 61, 70]
        
        # 2. Menghitung Daya (P = V x I) 
        power = round(voltage * current * power_factor, 1) # Watt (W) [cite: 61, 68]
        
        # Simulasi akumulasi energi (kWh)
        energy_accumulated += (power / 3600000) * 5 # Bertambah setiap 5 detik
        
        # 3. Mengemas data ke format JSON [cite: 17, 62]
        payload = {
            "device_id": "meter-001", # Unique identifier [cite: 46, 61, 65]
            "voltage": voltage,
            "current": current,
            "power": power,
            "energy": round(energy_accumulated, 2),
            "power_factor": power_factor,
            "frequency": frequency
        }
        
        # 4. Publish pesan ke Message Broker [cite: 18, 25, 88]
        client.publish(MQTT_TOPIC, json.dumps(payload))
        print(f"Mengirim Data: {payload}")
        
        time.sleep(5) # Kirim data setiap 5 detik [cite: 114]

except KeyboardInterrupt:
    print("Simulasi dihentikan.")
    client.disconnect()