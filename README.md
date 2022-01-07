# Vibration Analysis for Predictive Maintenance
## Predictive maintenance
Identify and predict failures in rotating machinery using high frequency vibration data to classify its behavior as normal or anomalous and generating alerts.

![dryer_3_down](docs/dryer_3_down.png)

## Goals
The goals of the project are: 

- Compare monitored values with the **ISO** standard
- Create a model using differents machine learning techniques

### ISO 10816
**ISO 10816** provides guidance for evaluating vibration velocity severity motors, pumps, fans, compressors, gear boxes, blowers, dryers, presses and other machines that operate in the 10 to 1000 Hz frequency range.

![iso10816](docs/iso10816.png)

## System Configuration
The system is composed by:
- Asynchronous motor 110 Kw, 195 A
- Engine pulley
- Fan
- Vibration sensor mounted on asynchronous motor


Every 10 minutes are acquired and stored the following measures:
- Z-Axis RMS Velocity (mm/sec)
- X-Axis RMS Velocity (mm/sec)
- Z-Axis High-Frequency RMS Acceleration (G)
- X-Axis High-Frequency RMS Acceleration (G)


## Dataset

![dryer_3_down](docs/dryer_3_down.png)

![dryer_1_up](docs/dryer_1_up.png)

![dryer_1_down](docs/dryer_1_down.png)



## Acquisition Equipment

+ Vibration and temperature sensor QM42VT2
+ Compact I/O Module for serial data transmission TBEN-S2-2COM-4DXP
