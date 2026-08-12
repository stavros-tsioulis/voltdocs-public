## Overview

The **TLC555** (commonly **TLC555IP** or **TLC555CP** in an 8-pin DIP package) is a monolithic precision timer fabricated using Texas Instruments' proprietary **LinCMOS™** process. As a CMOS drop-in alternative to the classic bipolar NE555 timer, it combines full 555 functionality with ultra-low supply current, high input impedance, and high-frequency operation.

Consuming only **$170\ \mu\text{A}$** at $5\text{ V}$ (compared to $3\text{ mA} \dots 10\text{ mA}$ for standard bipolar 555 ICs) and operating down to **$2.0\text{ V}$**, the TLC555 is ideal for battery-powered instruments, low-power microcontrollers, and high-frequency pulse generation up to **$2.1\text{ MHz}$**.

## Quick reference

| | |
|---|---|
| **Technology** | LinCMOS™ Low-Power CMOS |
| **Package** | 8-Pin DIP (Through-Hole) / SOIC-8 / TSSOP-8 |
| **Supply Voltage Range ($V_{DD}$)** | $2.0\text{ V}$ to $15.0\text{ V}$ DC |
| **Quiescent Supply Current** | $170\ \mu\text{A}$ typ at $V_{DD} = 5\text{V}$ ($360\ \mu\text{A}$ typ at $V_{DD} = 15\text{V}$) |
| **Max Switching Frequency** | Up to $2.1\text{ MHz}$ ($f_{MAX}$) |
| **Input Impedance** | $10^{12}\ \Omega$ ($1\text{ T}\Omega$) at `TRIG` / `THRES` inputs |
| **Output Sink / Source Current** | Sink: Up to $100\text{ mA}$ / Source: Up to $10\text{ mA}$ at $5\text{V}$ |

## Pinout (8-Pin DIP Package)

```
        ┌──────────┐
   GND ─│ 1      8 │─ VDD
  TRIG ─│ 2      7 │─ DISCH
   OUT ─│ 3      6 │─ THRES
 RESET ─│ 4      5 │─ CONT
        └──────────┘
```

| Pin | Name | Description |
|---|---|---|
| 1 | `GND` | Ground reference (0 V) |
| 2 | `TRIG` | Active-low trigger input (initiates timing cycle when $V_{TRIG} < \frac{1}{3} V_{DD}$) |
| 3 | `OUT` | Push-pull timer output pin |
| 4 | `RESET` | Active-low forced reset input (Low = forces OUT low & DISCH on) |
| 5 | `CONT` | Control voltage access pin to internal $\frac{2}{3} V_{DD}$ voltage divider |
| 6 | `THRES` | Threshold input (ends timing cycle when $V_{THRES} > \frac{2}{3} V_{DD}$) |
| 7 | `DISCH` | Open-drain discharge output for timing capacitor |
| 8 | `VDD` | Positive power supply (+2.0V to +15.0V DC) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage Range | $V_{DD}$ | 2.0 | 5.0 | 15.0 | V | Operational range |
| Quiescent Current | $I_{DD}$ | — | 170 | 300 | $\mu\text{A}$ | $V_{DD} = 5\text{V}, V_{TRIG} = V_{DD}$ |
| High Threshold Voltage | $V_{THRES}$ | 0.60 | 0.667 | 0.73 | $\times V_{DD}$ | Threshold level |
| Low Trigger Voltage | $V_{TRIG}$ | 0.27 | 0.333 | 0.40 | $\times V_{DD}$ | Trigger level |
| Output Low Sink Voltage | $V_{OL}$ | — | 0.4 | 0.75 | V | $V_{DD} = 5\text{V}, I_{SINK} = 10\text{mA}$ |
| Maximum Frequency | $f_{MAX}$ | 1.2 | 2.1 | — | MHz | $V_{DD} = 5\text{V}$, Astable mode |

## Astable Oscillator Circuit ($50\%$ Duty Cycle)

```
        +V_DD (2.0V - 15V Input)
          │
         [R_A]
          │
          ├─── Pin 7: DISCH
          │
         [R_B]
          │
          ├─── Pin 6: THRES
          ├─── Pin 2: TRIG
          │
         [C_1]
          │
         GND
```

$$ f = \frac{1.44}{(R_A + 2 R_B) \times C_1} $$

## Common mistakes

- **Expecting 200mA sourcing current like NE555:** Standard bipolar NE555 timer output can source up to 200mA. The CMOS TLC555 can sink 100mA but can only source ~10mA at 5V. Use a driver transistor when driving heavy loads.
- **Leaving supply decoupling off high-frequency designs:** Because the TLC555 operates up to 2.1MHz, place a $100\text{ nF}$ ceramic decoupling capacitor right next to Pin 8 (`VDD`) to prevent supply noise.

## Notes

- **TLC555 vs NE555:** TLC555 uses 20x less quiescent current ($170\ \mu\text{A}$ vs $3\text{mA}$), runs down to 2V (vs 4.5V), and switches faster ($2.1\text{ MHz}$ vs $500\text{ kHz}$).
