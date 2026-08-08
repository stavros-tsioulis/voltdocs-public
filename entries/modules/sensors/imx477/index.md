## Overview

The **IMX477** is a $1/2.3\text{"}$ 12.3-megapixel back-illuminated stacked CMOS image sensor manufactured by Sony. Equipped with large **$1.55\ \mu\text{m} \times 1.55\ \mu\text{m}$** pixels (nearly double the area of IMX219 pixels), an internal 12-bit ADC, and a 2-lane MIPI CSI-2 interface, it powers the **Raspberry Pi High Quality (HQ) Camera**.

Designed for high-end optical performance, the IMX477 module incorporates an integrated aluminum C/CS-mount lens socket with an adjustable back-focus ring and trip-mount thread. Delivering exceptional low-light sensitivity, $4056 \times 3040$ pixel RAW stills, 4K30 video, and 1080p60 high-speed video, it is used in professional machine vision, astrophotography, industrial inspection, and high-resolution time-lapse recording.

## Quick reference

| | |
|---|---|
| **Optical format** | 1/2.3-inch ($7.9\text{ mm}$ diagonal active area) |
| **Active pixel array** | $4056 \text{ (H)} \times 3040 \text{ (V)}$ (~12.3 Megapixels) |
| **Pixel size** | $1.55\ \mu\text{m} \times 1.55\ \mu\text{m}$ (large area for high SNR) |
| **Lens compatibility** | C-mount and CS-mount lenses (adapter ring included) |
| **Output interface** | 2-Lane MIPI CSI-2 (up to 1.5 Gbps per lane) |
| **Control interface** | $I^2C$ CCI control bus (`0x1A`) |
| **IR cut filter** | Integrated 650 nm IR cut filter |
| **Video modes** | 4K30, 1080p60, 720p120 |

## Connector & Physical Features

- **Interface Connector:** 15-pin 1.0 mm pitch FPC ribbon cable (standard Pi CSI connector).
- **Mount Thread:** 1/4"-20 tripod mounting socket.
- **Lens Mount:** CS-mount ($12.5\text{ mm}$ back-focal length); includes $6\text{ mm}$ C-mount adapter ring ($17.526\text{ mm}$ back-focal length).

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Analog Supply Voltage | $V_{ANA}$ | 2.6 | 2.8 | 3.0 | V | Sensor analog core |
| Digital Supply Voltage| $V_{DIG}$ | 1.0 | 1.05 | 1.15 | V | Sensor digital core |
| I/O Supply Voltage | $V_{IO}$ | 1.7 | 1.8 | 1.9 | V | Interface logic |
| Max Frame Rate (12.3MP)| $FPS_{12M}$| — | 10 | 10 | fps | $4056 \times 3040$ full 12-bit RAW |
| Max Frame Rate (4K) | $FPS_{4K}$ | — | 30 | 30 | fps | $3840 \times 2160$ 16:9 crop |
| Max Frame Rate (1080p)| $FPS_{1080p}$| — | 60 | 60 | fps | $1920 \times 1080$ $2 \times 2$ binning |
| Max Frame Rate (720p) | $FPS_{720p}$ | — | 120 | 120 | fps | $1332 \times 990$ $3 \times 3$ binning |
| Dynamic Range | $DR$ | — | 70 | — | dB | High dynamic range |

## Supported Video Modes

| Mode | Resolution | Aspect Ratio | Max Frame Rate | Binning / Cropping |
|---|---|---|---|---|
| 0 | $4056 \times 3040$ | 4:3 | 10 fps | Full resolution RAW |
| 1 | $2028 \times 1520$ | 4:3 | 40 fps | $2 \times 2$ full FOV binning |
| 2 | $2028 \times 1080$ | 16:9 | 50 fps | $2 \times 2$ cropped binning |
| 3 | $1332 \times 990$ | 4:3 | 120 fps | $3 \times 3$ full FOV binning |

## Wiring

Connect the 15-pin FPC ribbon cable directly to the Raspberry Pi board's CSI port:

- Ensure the **contacts face the HDMI connector** on Raspberry Pi 4 models.
- Rotate the back-focus adjustment ring to calibrate focus when swapping between C-mount and CS-mount lenses.

## Example (Python `libcamera` / `picamera2`)

```python
from picamera2 import Picamera2
import time

picam2 = Picamera2()

# Configure for full 12.3MP resolution still capture
still_config = picam2.create_still_configuration(main={"size": (4056, 3040)})
picam2.configure(still_config)

picam2.start()
print("High Quality Camera online. Focusing...")
time.sleep(2)

# Capture uncompressed high-resolution photo
picam2.capture_file("hq_photo.jpg")
print("12.3MP photo saved to hq_photo.jpg")

picam2.stop()
```

## Common mistakes

- **Forgetting the C-mount adapter ring:** Attaching a C-mount lens directly to the CS-mount socket without installing the included $6\text{ mm}$ extension ring prevents the lens from reaching infinity focus.
- **Unfocused back-focus ring:** If images remain blurry despite adjusting the lens focus ring, loosen the small back-focus locking screw and rotate the knurled metal housing ring to align the focal plane.

## Notes

- **IMX477 vs IMX219:** IMX477 has a larger $1/2.3\text{"}$ sensor area ($1.55\ \mu\text{m}$ pixels vs $1.12\ \mu\text{m}$ pixels), interchangeable optical lenses, superior low-light SNR, and higher resolution ($12.3\text{ MP}$ vs $8.0\text{ MP}$).
