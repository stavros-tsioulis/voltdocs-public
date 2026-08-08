## Overview

The **MAX31865** is a high-precision 15-bit resistance-to-digital converter manufactured by Maxim Integrated (Analog Devices). Designed specifically to interface with **Platinum Resistance Temperature Detectors (PT100 and PT1000 RTDs)**, it replaces complex analog instrumentation op-amp circuits with a single digital SPI IC.

Supporting **2-wire, 3-wire, and 4-wire RTD configurations**, the MAX31865 achieves an ultra-fine resolution of **$0.03125^\circ\text{C}$** ($0.0009765625\ \Omega$ per LSB) across extreme temperature ranges (**$-200^\circ\text{C}$ to $+850^\circ\text{C}$**). It incorporates built-in fault detection (detecting open RTD elements, short circuits to ground/$V_{CC}$, and over-range temperatures).

## Quick reference

| | |
|---|---|
| **Operating voltage (`VIN`)** | 3.3 V to 5.0 V DC (breakout includes 3.3V LDO regulator) |
| **IC supply voltage (`VDD`)** | 3.0 V to 3.6 V DC (3.3 V nominal) |
| **Interface** | SPI (Mode 1 or Mode 3, up to 5 MHz) |
| **Supported RTD types** | PT100 ($100\ \Omega$ nominal at $0^\circ\text{C}$) & PT1000 ($1000\ \Omega$ nominal at $0^\circ\text{C}$) |
| **Wiring modes** | 2-Wire, 3-Wire, and 4-Wire RTD probe connections |
| **ADC resolution** | 15-bit Delta-Sigma ADC ($0.03125^\circ\text{C}$ LSB) |
| **Temperature accuracy** | $\pm 0.5^\circ\text{C}$ total accuracy (over full $-200^\circ\text{C} \dots +850^\circ\text{C}$ range) |
| **Fault detection** | Detects open RTD wire, short to GND, short to VCC, and out-of-range thresholds |
| **Reference resistor ($R_{REF}$)** | $400\ \Omega$ or $430\ \Omega$ for PT100 ($4000\ \Omega$ or $4300\ \Omega$ for PT1000) |

## Pinout

Breakout module header & Terminal Block:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VIN` | Power | Supply power input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `3V3` | Power Output | Regulated 3.3V power output pin |
| 4 | `SDO` / `MISO` | Digital Output | SPI Master Input Slave Output |
| 5 | `SDI` / `MOSI` | Digital Input | SPI Master Output Slave Input |
| 6 | `CS` | Digital Input | Active-Low SPI Chip Select |
| 7 | `CLK` / `SCLK` | Digital Input | SPI Serial Clock |
| 8 | `RDY` | Digital Output | Active-Low Data Ready interrupt output pin |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{VIN}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Active Current | $I_{CC}$ | — | 2.0 | 3.5 | mA | Active conversion mode |
| Shutdown Current | $I_{sd}$ | — | 1.0 | 10.0 | µA | Software shutdown |
| ADC Resolution | $Res_{ADC}$| — | 15 | — | bits | 2's complement 15-bit word |
| Nominal Resistance (PT100) | $R_0$ | — | 100 | — | Ω | Resistance at $0^\circ\text{C}$ |
| Reference Resistor (PT100) | $R_{REF}$| 400 | 430 | 430 | Ω | Precision $0.1\%$ reference resistor |
| Conversion Time | $t_{conv}$ | 21 | 52 | 62 | ms | 50 Hz / 60 Hz rejection mode |

## RTD Resistance & Temperature Calculation Math

1. **Calculate RTD Resistance ($R_{RTD}$):**

$$ R_{RTD} = \left( \frac{\text{15-bit Raw ADC Register Value}}{32768} \right) \times R_{REF} $$

2. **Callendar-Van Dusen Equation ($T \ge 0^\circ\text{C}$):**

$$ R_{RTD}(T) = R_0 \cdot \left( 1 + A \cdot T + B \cdot T^2 \right) $$

Where $A = 3.9083 \times 10^{-3}\ ^\circ\text{C}^{-1}$ and $B = -5.775 \times 10^{-7}\ ^\circ\text{C}^{-2}$.

$$ T (^\circ\text{C}) = \frac{-A + \sqrt{A^2 - 4B \left( 1 - \frac{R_{RTD}}{R_0} \right)}}{2B} $$

## Wiring (3-Wire PT100 Probe)

| MAX31865 Pin | → | Arduino / MCU | ESP32 | Notes |
|---|---|---|---|---|
| `VIN` | | 5V / 3.3V | 3.3V | Power rail |
| `GND` | | GND | GND | System ground |
| `CS`  | | Digital D10 | GPIO 5 | SPI Chip Select |
| `SDI` (MOSI) | | Digital D11 | GPIO 23 | SPI MOSI |
| `SDO` (MISO) | | Digital D12 | GPIO 19 | SPI MISO |
| `CLK` (SCLK) | | Digital D13 | GPIO 18 | SPI Clock |

> [!IMPORTANT]
> Solder Jumper Configuration (2-Wire / 3-Wire / 4-Wire):
> - **3-Wire RTD Probe (Most Common):** Cut the thin trace between the `24` solder pads, solder the `3` pad closed, and solder the `2/3 Wire` jumper pad closed. Connect 2 matching wires to `RTD+`/`F+` and 1 wire to `RTD-`.
> - **2-Wire RTD Probe:** Solder the `24` jumper pad closed and short terminal `F+` to `RTD+` and `F-` to `RTD-`.

## Example (Adafruit_MAX31865 Library)

```cpp
#include <Adafruit_MAX31865.h>

// Use hardware SPI with CS pin 10
Adafruit_MAX31865 thermo = Adafruit_MAX31865(10);

// Set Reference Resistor (430 ohms for PT100)
#define RREF 430.0
// Set Nominal 0°C Resistance (100 ohms for PT100)
#define RNOMINAL 100.0

void setup() {
  Serial.begin(115200);
  Serial.println("Adafruit MAX31865 PT100 RTD Test");

  thermo.begin(MAX31865_3WIRE); // Configured for 3-wire PT100
}

void loop() {
  uint16_t rtd = thermo.readRTD();
  float ratio = rtd / 32768.0;
  float resistance = RREF * ratio;
  float temp = thermo.temperature(RNOMINAL, RREF);

  Serial.print("RTD Raw ADC: "); Serial.print(rtd);
  Serial.print(" | Resistance: "); Serial.print(resistance); Serial.print(" Ω");
  Serial.print(" | Temperature: "); Serial.print(temp); Serial.println(" °C");

  // Check for faults
  uint8_t fault = thermo.readFault();
  if (fault) {
    Serial.print("Fault 0x"); Serial.println(fault, HEX);
    thermo.clearFault();
  }

  delay(1000);
}
```

## Common mistakes

- **Mismatched $R_{REF}$ value in software:** Standard Adafruit/generic breakout boards use a **$430\ \Omega$ reference resistor ($R_{REF}=430.0$)** for PT100. Setting $R_{REF}=400.0$ in code introduces a $+7^\circ\text{C}$ measurement error.
- **Selecting wrong wire jumpers:** Failing to configure 2-wire / 3-wire PCB solder jumpers to match the connected physical PT100 probe triggers constant `RTD INLOW` or `RTD INHIGH` fault flags.

## Notes

- **MAX31865 vs MAX31855:** MAX31865 interfaces with RTDs (PT100/PT1000); MAX31855 interfaces with Thermocouples (K-Type).
