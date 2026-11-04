
import json
import random
import hmac
import hashlib
import secrest
from datetime import datetime, timezone

# Load the secret key
with open("hmac.key", "rb") as file:
    secret_key = file.read()

# Generate simulated sensor data
sensor_data = {
    "sensor_id": "SENSOR-001",
    "timestamp": datetime.now(timezone.utc).isoformat(),
    "signal_strength": secrets.randbelow(101),
    "status": "ACTIVE"
}

# Convert sensor data into consistent bytes
message = json.dumps(
    sensor_data,
    sort_keys=True,
    separators=(",", ":")
).encode("utf-8")

# Generate HMAC-SHA256 signature
signature = hmac.new(
    secret_key,
    message,
    hashlib.sha256
).hexdigest()

# Attach signature to sensor data
sensor_data["hmac"] = signature

# Save signed sensor data
with open("sensor_data.json", "w") as file:
    json.dump(sensor_data, file, indent=4)

print("Sensor data generated and signed successfully")

