## Overview

The **RDA5807M** (and variants RDA5807FP, RDA5807NN) is a single-chip CMOS stereo FM broadcast radio receiver IC manufactured by RDA Microelectronics. Sold as an ultra-compact 10-pin RRD-102 breakout module, it tunes FM radio frequencies from **50 MHz to 108 MHz** (covering US, European, and Japanese FM broadcast bands).

Integrating a fully digital synthesizer, IF selectivity, digital automatic gain control (AGC), RDS/RBDS radio text demodulator, programmable bass boost, and internal $32.768\text{ kHz}$ clock driver, the RDA5807M outputs analog stereo audio capable of directly driving $32\ \Omega$ headphones or audio power amplifiers over an $I^2C$ bus. It is widely used in DIY FM radio receivers, alarm clocks, and retro boombox projects.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 2.7 V to 3.6 V DC (3.3 V nominal) |
| **Interface** | $I^2C$ (up to 400 kHz) |
| **Direct Register Address** | `0x11` (Random access register mode) |
| **Sequential Register Address** | `0x10` (Legacy TEA5767 backward compatibility mode) |
| **FM frequency range** | 50.0 MHz to 108.0 MHz (Worldwide FM) |
| **Channel spacing** | 25 kHz, 50 kHz, 100 kHz, or 200 kHz |
| **Audio features** | Stereo/Mono mode, Digital Volume (0–15), Bass Boost, Mute |
| **Data decoding** | Integrated RDS / RBDS (Radio Data System text & station ID) |
| **Direct headphone drive** | Onboard driver outputs $32\ \Omega$ headphone audio |

## Pinout (RRD-102 Module 10-Pin Header)

```
        ┌───────────────────┐
        │  [RDA5807M IC]   │
        │  [32.768kHz XTAL] │
        └─┬─┬─┬─┬─┬─┬─┬─┬─┬─┘
          1 2 3 4 5 6 7 8 9 10
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `SDA` | Digital Input / Output | $I^2C$ Serial Data |
| 2 | `SCL` | Digital Input | $I^2C$ Serial Clock |
| 3 | `GND` | Power | Ground reference (0 V) |
| 4 | `NC` | Unused | No connection |
| 5 | `VCC` | Power | Power supply input (+2.7 V to +3.6 V DC) |
| 6 | `GND` | Power | Ground reference (0 V) |
| 7 | `ROUT` | Analog Output | Right channel audio output |
| 8 | `LOUT` | Analog Output | Left channel audio output |
| 9 | `GND` | Power | Audio ground reference |
| 10 | `ANT` | Analog Input | FM Antenna connection (connect a 75 cm wire antenna) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage | $V_{CC}$ | 2.7 | 3.3 | 3.6 | V | DC |
| Active Supply Current | $I_{CC}$ | — | 20 | 25 | mA | $V_{CC} = 3.3\text{ V}$, volume max |
| Power-Down Current | $I_{pd}$ | — | 5 | 15 | µA | Shutdown mode |
| Sensitivity | $S_{sens}$ | — | 1.5 | 2.0 | µV | $S/N = 26\text{ dB}$ |
| Audio Output Voltage | $V_{audio}$| — | 100 | 150 | mV RMS| $32\ \Omega$ load |
| Channel Separation | $CS$ | 30 | 35 | — | dB | Stereo separation |
| Signal-to-Noise Ratio | $SNR$ | 55 | 60 | — | dB | Measured across 50–108 MHz |

## $I^2C$ Register Access Modes

The RDA5807M supports two distinct $I^2C$ communication modes:

1. **Direct Mode (`0x11` Address):** Allows reading and writing specific 16-bit registers (such as `0x02` for basic control, `0x03` for frequency channel tune, `0x05` for volume and bass boost).
2. **Sequential Mode (`0x10` Address):** Backward compatible with the legacy TEA5767 FM chip. Writes start at Register `0x02` and automatically increment.

### Frequency Calculation (Channel Register `0x03`)

$$ \text{Frequency (MHz)} = \text{Bottom\_Freq} + \left( \text{CHAN} \times \text{Channel\_Space} \right) $$

For standard US/European tuning ($\text{Bottom\_Freq} = 87.0\text{ MHz}$, $\text{Space} = 100\text{ kHz}$):

$$ \text{CHAN} = (\text{Target\_Freq\_MHz} - 87.0) \times 10 $$

## Wiring

| RDA5807 Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| 5 (`VCC`) | | 3.3V | 3.3V | **Do not connect to 5V** |
| 3, 6, 9 (`GND`)| | GND | GND | Shared system ground |
| 1 (`SDA`) | | A4 | GPIO 21 | $I^2C$ Data |
| 2 (`SCL`) | | A5 | GPIO 22 | $I^2C$ Clock |
| 10 (`ANT`)| | 75 cm Wire | 75 cm Wire | Extend 1/4 wavelength wire antenna |
| 7, 8 (`ROUT/LOUT`)| | 3.5mm Headphone Jack / PAM8403 Amp Input | Audio output pins |

## Example (Arduino Radio Library)

```cpp
#include <Wire.h>
#include <radio.h>
#include <RDA5807M.h>

#define FIX_BAND RADIO_BAND_FM
#define FIX_STATION 10150 // 101.5 MHz FM

RDA5807M radio;

void setup() {
  Serial.begin(9600);
  Wire.begin();

  Serial.println("Initializing RDA5807M FM Radio...");
  
  if (!radio.initWire(Wire)) {
    Serial.println("RDA5807M not responding!");
    while(1);
  }

  radio.setBand(FIX_BAND);
  radio.setFrequency(FIX_STATION);
  radio.setVolume(10); // 0 to 15
  radio.setMono(false); // Enable Stereo
  radio.setBassBoost(true); // Enable Bass Boost

  Serial.print("Tuned to "); Serial.print(FIX_STATION / 100.0); Serial.println(" MHz FM");
}

void loop() {
  // Read RDS Radio Text if available
  char buffer[32];
  radio.formatFrequency(buffer, sizeof(buffer));
  delay(2000);
}
```

## Common mistakes

- **Connecting `VCC` to 5V:** The maximum supply rating is 3.6V. Supplying 5V destroys the chip.
- **Forgetting an antenna wire:** Operating without an antenna wire on pin 10 results in heavy static noise and inability to lock onto FM stations. Connect a $75\text{ cm}$ (~30 inch) length of insulated copper wire.

## Notes

- **RDA5807 vs TEA5767 vs SI4703:** RDA5807 is cheaper, includes integrated RDS decoding, and directly drives $32\ \Omega$ headphones without needing external op-amps.
