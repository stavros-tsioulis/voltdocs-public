## Overview

The **PA1010D** is an ultra-compact 99-channel multi-GNSS (GPS, GLONASS, GALILEO, QZSS) receiver module manufactured by GlobalTop and popularized by Adafruit on STEMMA QT breakout boards. Measuring just $12\text{ mm} \times 12\text{ mm}$, it integrates a high-sensitivity MediaTek MTK3333 GNSS chipset and an internal ceramic patch antenna.

Unlike traditional GPS modules (such as the NEO-6M) that communicate strictly over UART, the PA1010D supports both standard **TTL UART (9,600 bps)** and **$I^2C$ (`0x10`)**, allowing microcontrollers without spare hardware serial ports to read NMEA-0183 GPS sentences easily. With $-165\text{ dBm}$ tracking sensitivity and up to 10 Hz position update rates, it is ideal for compact wearable trackers, drone telemetry, and high-altitude balloon payloads.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout includes 3.3V LDO regulator) |
| **IC supply voltage (`VDD`)** | 3.0 V to 4.3 V DC (3.3 V nominal) |
| **Interfaces** | $I^2C$ (Default address `0x10`) & TTL UART (9,600 bps default) |
| **Channels** | 99 search / 33 tracking channels (MTK3333 chipset) |
| **Supported constellations** | GPS, GLONASS, GALILEO, QZSS, SBAS (WAAS/EGNOS/MSAS) |
| **Tracking sensitivity** | $-165\text{ dBm}$ |
| **Horizontal position accuracy**| 2.5 meters CEP |
| **Update rate** | 1 Hz default (configurable up to 10 Hz) |
| **Antenna** | Integrated $10 \times 10\text{ mm}$ ceramic patch antenna |

## Pinout

STEMMA QT / Qwiic 4-pin connector & 0.1" header pins:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` | Power | Power supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `SCL` / `RX` | Digital Input | $I^2C$ Serial Clock / UART Receive input |
| 4 | `SDA` / `TX` | Digital Output | $I^2C$ Serial Data / UART Transmit output |
| 5 | `PPS` | Digital Output | Pulse-Per-Second precision time-sync output (1 Hz pulse) |
| 6 | `RST` | Digital Input | Active-Low hardware reset pin |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Tracking Current | $I_{track}$ | — | 25 | 30 | mA | Acquisition & tracking |
| Standby Current | $I_{sb}$ | — | 30 | — | µA | Backup battery mode |
| Cold Start Time | $t_{cold}$ | — | 35 | 45 | s | Open sky initial lock |
| Hot Start Time | $t_{hot}$ | — | 1 | 2 | s | Warm restart with RTC backup |
| Altitude Limit | $Alt_{max}$| — | 18000 | 50000 | m | High altitude balloon mode |
| Velocity Limit | $Vel_{max}$| — | 515 | — | m/s | Maximum speed |

## $I^2C$ NMEA Streaming Protocol

When interfaced over $I^2C$ (`0x10`), the PA1010D continuously streams standard ASCII **NMEA-0183 sentences** (`$GPRMC`, `$GPGGA`, `$GPGSA`, `$GPGSV`):

- Reading from address `0x10` returns available NMEA characters.
- If no new data is ready, the module returns `0x0A` (`\n` newline).

```
$GPRMC,123519.00,A,4807.038,N,01131.000,E,022.4,084.4,230326,003.1,W*6A
$GPGGA,123519.00,4807.038,N,01131.000,E,1,08,0.9,545.4,M,46.9,M,,*47
```

## Wiring

| PA1010D Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VIN` | | 5V / 3.3V | 3.3V | Module includes 3.3V LDO |
| `GND` | | GND | GND | System ground |
| `SCL` | | A5 | GPIO 22 | $I^2C$ Clock |
| `SDA` | | A4 | GPIO 21 | $I^2C$ Data |
| `PPS` | | Digital D2 | GPIO 4 | Optional 1 Hz pulse for precise timing |

## Example (Arduino Adafruit_GPS over $I^2C$)

```cpp
#include <Adafruit_GPS.h>

// Initialize I2C GPS instance
Adafruit_GPS GPS(&Wire);

void setup() {
  Serial.begin(115200);
  while (!Serial) delay(10);

  Serial.println("Adafruit PA1010D I2C GPS Test");

  // 0x10 is default I2C address for PA1010D
  GPS.begin(0x10);

  // Request RMC and GGA NMEA sentences and 1 Hz update rate
  GPS.sendCommand(PMTK_SET_NMEA_OUTPUT_RMCGGA);
  GPS.sendCommand(PMTK_SET_NMEA_UPDATE_1HZ);

  delay(1000);
}

void loop() {
  // Read NMEA data from I2C bus
  char c = GPS.read();
  if (GPS.newNMEAreceived()) {
    if (!GPS.parse(GPS.lastNMEA())) return;

    if (GPS.fix) {
      Serial.print("Location: ");
      Serial.print(GPS.latitudeDegrees, 4); Serial.print(", ");
      Serial.print(GPS.longitudeDegrees, 4);
      Serial.print(" | Altitude: "); Serial.print(GPS.altitude); Serial.println(" m");
    } else {
      Serial.println("Searching for satellite lock...");
    }
  }
}
```

## Common mistakes

- **Testing indoors:** GPS signals (1575.42 MHz) cannot penetrate concrete ceilings or metallic roofs. Always test initial satellite acquisition outdoors under clear sky.
- **Occluding the ceramic patch antenna:** Mount the PA1010D board horizontally with the square ceramic patch antenna facing **upwards towards the sky**. Do not cover with copper shields or batteries.

## Notes

- **PA1010D vs Ultimate GPS (MTK3339):** PA1010D is significantly smaller ($12 \times 12\text{ mm}$ vs $16 \times 16\text{ mm}$), supports GLONASS in addition to GPS, and includes built-in $I^2C$ support.
