## Overview

The **DS1302** is a classic trickle-charge real-time clock (RTC) chip manufactured by Maxim Integrated (Analog Devices). Included in low-cost Elegoo, SunFounder, and Keyes Arduino starter kits, it is packaged as a compact 5-pin breakout module featuring an onboard $32.768\text{ kHz}$ tuning fork crystal and a CR2032 coin cell battery holder.

Communicating over a simple **3-wire synchronous serial interface (`CE`, `I/O`, `SCLK`)**, the DS1302 maintains full BCD timekeeping registers (seconds, minutes, hours, date, month, day-of-week, and year with leap-year compensation up to 2100) along with **31 bytes of battery-backed static RAM**.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC2`)** | 2.0 V to 5.5 V DC (3.3 V or 5.0 V nominal) |
| **Primary backup voltage (`VCC1`)**| 2.0 V to 5.5 V DC (CR2032 3V coin cell battery) |
| **Interface** | 3-Wire Serial Interface (`CE` / `RST`, `I/O` / `DAT`, `SCLK` / `CLK`) |
| **Crystal frequency** | $32.768\text{ kHz}$ |
| **Backup power draw** | $< 0.3\ \mu\text{A}$ at $V_{CC1} = 2.0\text{V}$ |
| **Static RAM** | 31 bytes battery-backed SRAM for user data storage |
| **Timekeeping format** | BCD (Seconds, Minutes, 12/24-Hour, Date, Month, Day, Year) |
| **Trickle Charger** | Software-selectable charging diode & resistor network for rechargeable batteries |

## Pinout

Breakout module 5-pin 0.1" (2.54 mm) connector header:

```
        ┌───────────────────────────────┐
        │  [DS1302 IC]  [32.768kHz]     │
        │  [CR2032 Coin Cell Holder]    │
        └─┬─────┬─────┬─────┬─────┬─────┘
         VCC   GND   CLK   DAT   RST
          1     2     3     4     5
```

| Pin | Module Label | Name | Type | Description |
|---|---|---|---|---|
| 1 | `VCC` | `VCC2` | Power | Main system power supply input (+2.0 V to +5.5 V DC) |
| 2 | `GND` | `GND` | Power | Ground reference (0 V) |
| 3 | `CLK` | `SCLK` | Digital Input | Serial Clock input pin |
| 4 | `DAT` | `I/O` | Digital Input / Output | Bi-directional Serial Data line |
| 5 | `RST` | `CE` | Digital Input | Active-High Chip Enable / Reset control line |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Main Supply Voltage | $V_{CC2}$ | 2.0 | 3.3 / 5.0 | 5.5 | V | System operating power |
| Backup Battery Voltage | $V_{CC1}$ | 2.0 | 3.0 | 3.5 | V | CR2032 coin cell input |
| Active Supply Current | $I_{CC2}$ | — | 0.3 | 1.0 | mA | SPI serial data transfer active |
| Backup Current | $I_{CC1}$ | — | 0.3 | 1.0 | µA | Main power off, $V_{CC1}=3.0\text{V}$ |
| Clock Transfer Speed | $f_{SCLK}$| 0 | — | 2.0 | MHz | At $V_{CC2} = 5.0\text{V}$ |
| Internal SRAM | $RAM$ | — | 31 | — | Bytes | Battery-backed non-volatile RAM |

## 3-Wire Serial Timing Protocol

- **Chip Enable (`CE` / `RST`):** Drive `CE` High before initiating serial transfers. Drive `CE` Low to end a transaction.
- **Clock (`SCLK`):** Input data bits on `I/O` are sampled on the **rising edge of `SCLK`**; output data bits on `I/O` change on the **falling edge of `SCLK`**.
- **Data (`I/O`):** First byte sent is the Command Byte ($R/\bar{W}$ bit, Register Address, and Magic Bit 7 High).

```
 Command Byte Read:  [ 1 | A6 | A5 | A4 | A3 | A2 | A1 | R/W=1 ]
 Command Byte Write: [ 1 | A6 | A5 | A4 | A3 | A2 | A1 | R/W=0 ]
```

## Wiring

| DS1302 Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `CLK` | | Digital D6 | GPIO 18 | `SCLK` clock line |
| `DAT` | | Digital D7 | GPIO 19 | `I/O` bi-directional data line |
| `RST` | | Digital D8 | GPIO 5 | `CE` active-high chip enable |

## Example (Arduino `RtcByMakuna` Library)

```cpp
#include <ThreeWire.h>  
#include <RtcDS1302.h>

// Pins: DAT (IO), CLK (SCLK), RST (CE)
ThreeWire myWire(7, 6, 8); 
RtcDS1302<ThreeWire> Rtc(myWire);

void setup() {
  Serial.begin(115200);
  Rtc.Begin();

  if (!Rtc.IsDateTimeValid()) {
    Serial.println("RTC lost confidence in the DateTime!");
    // Set compilation time
    RtcDateTime compiled = RtcDateTime(__DATE__, __TIME__);
    Rtc.SetDateTime(compiled);
  }

  if (Rtc.GetIsWriteProtected()) {
    Rtc.SetIsWriteProtected(false);
  }

  if (!Rtc.GetIsRunning()) {
    Rtc.SetIsRunning(true);
  }
}

void loop() {
  RtcDateTime now = Rtc.GetDateTime();

  char datestring[20];
  snprintf_P(datestring, 
             countof(datestring),
             PSTR("%02u/%02u/%04u %02u:%02u:%02u"),
             now.Month(), now.Day(), now.Year(),
             now.Hour(), now.Minute(), now.Second());

  Serial.println(datestring);
  delay(1000);
}
```

## Common mistakes

- **Enabling trickle charger with primary CR2032 lithium batteries:** The DS1302 includes a software-selectable trickle charger circuit. **Do not enable the trickle charger when using standard non-rechargeable CR2032 batteries**, as charging non-rechargeable lithium cells causes coin cell swelling and explosion hazards.
- **Confusing 3-wire serial with SPI or $I^2C$:** The DS1302 uses a custom 3-wire protocol with active-high `CE`. Standard hardware SPI libraries or $I^2C$ scanners cannot communicate with the DS1302.

## Notes

- **DS1302 vs DS1307 vs DS3231:** DS1302 uses a 3-wire serial interface; DS1307 uses $I^2C$; DS3231 includes an internal TCXO crystal for $\pm 2\text{ ppm}$ precision.
