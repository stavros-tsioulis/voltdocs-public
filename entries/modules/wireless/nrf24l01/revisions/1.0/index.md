## Overview

The original **nRF24L01** (revision 1.0) introduced Nordic's Enhanced ShockBurst hardware protocol engine and QFN20 footprint.

### Key differences from nRF24L01+ (v2.0)

- **Air Data Rates:** Supports 1 Mbps and 2 Mbps only. Does **not** support the 250 kbps low-rate long-range mode.
- **RF Sensitivity:** -85 dBm @ 1 Mbps / -82 dBm @ 2 Mbps (compared to -94 dBm @ 250 kbps on nRF24L01+).
- **SPI Speed:** Max 8 MHz SPI clock (upgraded to 10 MHz on nRF24L01+).
- **Missing Features:** Lacks Received Power Detector (RPD) register (`0x09`), dynamic payload length (`DYNPD`), and selective ACK features.

Superseded by current [revision 2.0 (nRF24L01+)](../../index.md).
