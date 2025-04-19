# Prototype-for-autonomous-flight-data-collection-using-Jetson
Prototype for autonomous flight data collection using Jetson
## Repository Structure

- `data-collection-suite/`: Scripts for collecting GPS, IMU, audio, and video data
- `data-platform/`: Code for managing data storage (MicroSD, SSD, cloud upload)
- `data-processing-pipeline/`: Scripts to process, clean, and analyze collected data
- `docs/`: System diagrams, setup guides, and other documentation
- `test/`: Unit tests for validating data collection scripts

### Getting Started
To simulate data in development:
```bash
cd data-collection-suite
python utils/mock_data_generator.py
