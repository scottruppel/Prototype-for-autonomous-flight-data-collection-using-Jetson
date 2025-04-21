
import csv
import random
from datetime import datetime

# Output file
output_file = 'data-collection-suite/mock_data/mock_imu_log.csv'

# Generate mock IMU data
def generate_mock_imu():
    return {
        'timestamp': datetime.utcnow().isoformat(),
        'accel_x': round(random.uniform(-2.0, 2.0), 3),
        'accel_y': round(random.uniform(-2.0, 2.0), 3),
        'accel_z': round(random.uniform(-2.0, 2.0), 3),
        'gyro_x': round(random.uniform(-250.0, 250.0), 3),
        'gyro_y': round(random.uniform(-250.0, 250.0), 3),
        'gyro_z': round(random.uniform(-250.0, 250.0), 3),
        'pitch': round(random.uniform(-90.0, 90.0), 2),
        'roll': round(random.uniform(-180.0, 180.0), 2),
        'yaw': round(random.uniform(0.0, 360.0), 2),
    }

# Save to CSV
with open(output_file, 'w', newline='') as csvfile:
    fieldnames = [
        'timestamp', 'accel_x', 'accel_y', 'accel_z',
        'gyro_x', 'gyro_y', 'gyro_z',
        'pitch', 'roll', 'yaw'
    ]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for _ in range(100):  # Generate 100 rows of mock data
        row = generate_mock_imu()
        writer.writerow(row)
        print(f"Logged IMU data: {row}")
