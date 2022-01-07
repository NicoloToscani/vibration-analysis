# Vibration Analysis for Predictive Maintenance
## Predictive maintenance
The goal is to identify and predict failures in rotating machinery using high frequency vibration data to classify its behavior as normal or anomalous and generating alerts.

## Goal

In order for the application to work, it is necessary to insert some elements inside your WinCC Unified project, including :

- **"EdgeSentronTags"** Table Variables;

### Load App on Unified Comfort Panels

1. Copy the downloaded ```sentron-edge_x.x.x.app``` file to your Developer PC.
2. Open the Industrial Edge Management Web Page of UCP on ```https://<ucp-address>```
3. Import the .app file using the *Import Offline* button
4. Wait until App is installed

## WinCC Unified Configuration

In order for the application to work, it is necessary to insert some elements inside your WinCC Unified project, including :

- **"EdgeSentronTags"** Table Variables;

![dryer_3_down](docs/dryer_3_down.png)

![dryer_1_up](docs/dryer_1_up.png)

![dryer_1_down](docs/dryer_1_down.png)

![iso10816](docs/iso10816.png)

## Equipment Compatibility

This module has been developed and tested on:
+ Vibration and temperature sensor QM42VT2
+ Compact I/O Module for serial data transmission TBEN-S2-2COM-4DXP
