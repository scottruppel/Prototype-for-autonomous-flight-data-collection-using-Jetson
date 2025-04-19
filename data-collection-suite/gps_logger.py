
import pandas as pd
import time
import os

# === CONFIG ===
GPS_FILE = 'data-collection-suite/mock_data/mock_gps_log.csv'
IMU_FILE = 'data-collection-suite/mock_data/mock_imu_log.csv'
OUTPUT_FILE = 'data-collection-suite/synced_log.csv'

# === LOAD MOCK DATA ===
gps_df = pd.read_csv(GPS_FILE)
imu_df = pd.read_csv(IMU_FILE)

# Simulate timestamps — assuming they were captured at 1Hz
gps_df['timestamp'] = pd.date_range(start='2025-01-01 12:00:00', periods=len(gps_df), freq='1s')
imu_df['timestamp'] = pd.date_range(start='2025-01-01 12:00:00', periods=len(imu_df), freq='1s')

# === SYNC & MERGE ===
synced_df = pd.merge_asof(gps_df.sort_values('timestamp'),
                          imu_df.sort_values('timestamp'),
                          on='timestamp',
                          direction='nearest')

# === WRITE OUTPUT ===
os.makedirs('data-collection-suite', exist_ok=True)
synced_df.to_csv(OUTPUT_FILE, index=False)

print("✅ Synced data saved to:", OUTPUT_FILE)
print(synced_df.head())
