## Overview

The **IMX219** (specifically the IMX219PQ) is a $1/4\text{"}$ 8.08-megapixel back-illuminated stacked CMOS image sensor manufactured by Sony. Equipped with Exmor R technology, a $1.12\ \mu\text{m} \times 1.12\ \mu\text{m}$ square pixel array, an internal 10-bit A/D converter, and a 2-lane MIPI CSI-2 high-speed serial output interface, it powers the official **Raspberry Pi Camera Module v2**.

Capable of capturing full-resolution $3280 \times 2464$ pixel still images and streaming 1080p30, 720p60, or 640x480p90 video, the IMX219 is widely used in Raspberry Pi and NVIDIA Jetson computer vision pipelines (OpenCV, OpenCV-CUDA, picamera2, libcamera), AI object detection, and robotics vision.

## Quick reference

| | |
|---|---|
| **Optical format** | 1/4-inch ($3.674\text{ mm} \times 2.760\text{ mm}$ active area) |
| **Active pixel array** | $3280 \text{ (H)} \times 2464 \text{ (V)}$ (~8.08 Megapixels) |
| **Pixel size** | $1.12\ \mu\text{m} \times 1.12\ \mu\text{m}$ |
| **Color filter array** | Bayer RGB pattern |
| **Output interface** | 2-Lane MIPI CSI-2 (up to 755 Mbps per lane) |
| **Control interface** | $I^2C$ CCI control bus (`0x10`) |
| **Video modes** | 1080p30, 720p60, 640x480p90 |
| **Connector** | 15-pin 1.0 mm pitch FPC ribbon cable (standard Pi CSI connector) |

## Connector Pinout (Raspberry Pi 15-Pin CSI Ribbon)

```
        Pin 1 (GND) ────────────────────── Pin 15 (GND)
        [ 1  2  3  4  5  6  7  8  9 10 11 12 13 14 15 ]
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground reference (0 V) |
| 2 | `CAM_D0_N` | MIPI Output | MIPI CSI Data Lane 0 (-) |
| 3 | `CAM_D0_P` | MIPI Output | MIPI CSI Data Lane 0 (+) |
| 4 | `GND` | Power | Ground |
| 5 | `CAM_D1_N` | MIPI Output | MIPI CSI Data Lane 1 (-) |
| 6 | `CAM_D1_P` | MIPI Output | MIPI CSI Data Lane 1 (+) |
| 7 | `GND` | Power | Ground |
| 8 | `CAM_CLK_N` | MIPI Output | MIPI CSI Clock Lane (-) |
| 9 | `CAM_CLK_P` | MIPI Output | MIPI CSI Clock Lane (+) |
| 10 | `GND` | Power | Ground |
| 11 | `CAM_GPIO` / `SHUTDOWN` | Digital Input | Camera enable / LED control |
| 21 | `SCL` | Digital Input | $I^2C$ Clock |
| 13 | `SDA` | Digital Input / Output | $I^2C$ Data |
| 14 | `3V3` | Power | +3.3 V Power supply |
| 15 | `GND` | Power | Ground |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Analog Supply Voltage | $V_{ANA}$ | 2.6 | 2.8 | 3.0 | V | Sensor analog core |
| Digital Supply Voltage| $V_{DIG}$ | 1.1 | 1.2 | 1.3 | V | Sensor digital core |
| I/O Supply Voltage | $V_{IO}$ | 1.7 | 1.8 | 1.9 | V | Interface logic |
| Max Frame Rate (8MP) | $FPS_{8M}$ | — | 30 | 30 | fps | $3280 \times 2464$ full resolution |
| Max Frame Rate (1080p)| $FPS_{1080p}$| — | 47 | 60 | fps | $1920 \times 1080$ cropped |
| Max Frame Rate (720p) | $FPS_{720p}$ | — | 90 | 90 | fps | $1280 \times 720$ binned |
| Sensitivity | $S_{sens}$ | — | 214 | — | mV/lux-sec | Green channel |
| Dynamic Range | $DR$ | — | 67 | — | dB | Max dynamic range |

## Supported Video Modes

| Mode | Resolution | Aspect Ratio | Max Frame Rate | FOV | Binning / Cropping |
|---|---|---|---|---|---|
| 0 | $3280 \times 2464$ | 4:3 | 30 fps | Full | None (Full sensor array) |
| 1 | $1920 \times 1080$ | 16:9 | 30 / 60 fps | Partial | Partial crop ($1080\text{p}$) |
| 2 | $1280 \times 720$ | 16:9 | 60 / 90 fps | Partial | $2 \times 2$ binning |
| 3 | $640 \times 480$ | 4:3 | 90 fps | Partial | $4 \times 4$ binning |

## Wiring

The IMX219 camera module connects directly to the 15-pin MIPI CSI-2 connector on Raspberry Pi single-board computers via a flexible flat cable (FFC):

- Orient the cable so the **blue plastic stiffener faces away from the Ethernet / USB ports** (contacts facing towards the HDMI port) on standard Pi 4 boards.
- Push the collar latch down firmly to secure the ribbon cable.

## Example (Python `libcamera` / `picamera2` on Raspberry Pi OS)

```python
from picamera2 import Picamera2
import time

picam2 = Picamera2()

# Configure for 1920x1080 30fps stream
camera_config = picam2.create_preview_configuration(main={"size": (1920, 1080)})
picam2.configure(camera_config)

picam2.start()
print("Streaming video... capturing image in 2 seconds.")
time.sleep(2)

picam2.capture_file("test_image.jpg")
print("Image saved to test_image.jpg")

picam2.stop()
```

## Common mistakes

- **Inserting FFC ribbon cable backwards:** Connecting the ribbon cable with contacts facing the wrong side results in camera detection failure (`No camera detected`).
- **Attempting to interface via GPIO SPI pins:** The IMX219 outputs raw MIPI CSI-2 differential signals (up to 755 Mbps). It **cannot be connected to standard SPI GPIO pins** or 8-bit microcontrollers (Arduino).

## Notes

- **IMX219 vs OV5647 vs IMX477:** OV5647 was the original 5MP Camera v1; IMX219 is the 8MP Camera v2; IMX477 is the 12.3MP High Quality Camera featuring interchangeable C/CS mount lenses.
