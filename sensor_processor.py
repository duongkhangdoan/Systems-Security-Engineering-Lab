
import json
import logging
import hmac
import hashlib

# Configure security logging
logging.basicConfig(
    filename="security.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Load secret key
with open("hmac.key", "rb") as file:
    secret_key = file.read()


# Verify HMAC integrity
def verify_hmac(data):
    received_hmac = data.get("hmac")

    if not isinstance(received_hmac, str):
        logging.warning("Missing or invalid HMAC")
        return False

    # Exclude HMAC from the signed message
    original_data = {
        key: value
        for key, value in data.items()
        if key != "hmac"
    }

    message = json.dumps(
        original_data,
        sort_keys=True,
        separators=(",", ":")
    ).encode("utf-8")

    expected_hmac = hmac.new(
        secret_key,
        message,
        hashlib.sha256
    ).hexdigest()

    if not hmac.compare_digest(received_hmac, expected_hmac):
        logging.warning("HMAC verification failed: Possible data tampering")
        return False

    logging.info("HMAC verification successful")
    return True


# Validate sensor data
def validate_sensor(data):

    if not isinstance(data.get("sensor_id"), str):
        logging.warning("Invalid sensor ID")
        return False

    signal = data.get("signal_strength")

    if type(signal) is not int or not 0 <= signal <= 100:
        logging.warning("Invalid signal strength")
        return False

    if data.get("status") not in ["ACTIVE", "INACTIVE"]:
        logging.warning("Invalid sensor status")
        return False

    logging.info("Sensor data validated successfully")
    return True


# Read and process sensor data
try:
    with open("sensor_data.json", "r") as file:
        sensor_data = json.load(file)

    # Verify integrity before validation
    if not verify_hmac(sensor_data):
        print("SECURITY ALERT: HMAC verification failed")

    elif validate_sensor(sensor_data):
        print("VALID: Sensor data accepted")

    else:
        print("INVALID: Sensor data rejected")

except (OSError, json.JSONDecodeError) as error:
    logging.error("Failed to read sensor data: %s", error)
    print("ERROR: Cannot read sensor data")

