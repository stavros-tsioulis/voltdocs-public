## Overview

The **1N4148** is the classic fast small-signal silicon switching diode. It lives in nearly every hobbyist parts bin next to the 1N400x family: where the 1N4007 is a slow 1 A power rectifier, the 1N4148 is a **high-speed, low-current** diode for logic clamping, steering, freewheeling on small inductors, and RF/signal work.

Rated for **100 V** peak reverse voltage and roughly **200 mA** continuous forward current, its defining number is the **~4 ns reverse recovery time** — fast enough that it stays useful well into MHz switching, unlike power rectifiers.

## Quick reference

| | |
|---|---|
| **Type** | Silicon small-signal switching diode |
| **Package** | DO-35 (DO-204AH) axial glass |
| **Cathode marking** | Black / painted band = cathode (−) |
| **Peak reverse voltage** `VR` | 100 V |
| **Average forward current** `IF` | 200 mA |
| **Forward voltage** `Vf` | ≤ 1.0 V at 10 mA |
| **Reverse recovery** `trr` | 4 ns max |
| **Junction capacitance** | 4 pF typ at 0 V, 1 MHz |

## Polarity

> [!INFO] The band on the glass body marks the **cathode** (−). Forward current flows anode → cathode when the anode is ~0.6–0.7 V above the cathode.

```
   Anode (+)              Cathode (−)
                     (band)
      ────────┤├────────
```

## Key parameters

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Breakdown / reverse voltage | `VR` | 100 | — | — | V | `IR` = 100 µA |
| Forward voltage | `Vf` | — | — | 1.0 | V | `IF` = 10 mA |
| Forward voltage | `Vf` | — | — | 1.0 | V | `IF` = 100 mA (1N4448 class) |
| Reverse leakage | `IR` | — | — | 5.0 | µA | `VR` = 75 V, `TA` = 25 °C |
| Reverse recovery time | `trr` | — | — | 4 | ns | `IF` = 10 mA, `VR` = 6 V, `Irr` = 1 mA |
| Capacitance | `CT` | — | — | 4 | pF | `VR` = 0 V, `f` = 1 MHz |
| Average rectified current | `IF(AV)` | — | — | 200 | mA | |
| Peak surge current | `IFSM` | — | — | 1.0 | A | pulse |

## Forward & reverse characteristics

- **Forward:** Conducts when `Vanode − Vcathode` exceeds ~0.6–0.7 V; voltage rise is steeper than a Schottky but recovery is much faster than a 1N400x.
- **Reverse:** Blocks up to 100 V with microamp-level leakage at room temperature; leakage rises strongly with junction temperature.

## Variants

| Part | Notes |
|---|---|
| `1N4148` | Default DO-35 hobbyist stock part |
| `1N914` | Closely related / often co-documented with 1N4148 |
| `1N4448` | Same family; slightly different `Vf` / current binning |
| SOD-323 / SOD-523 SMT | Surface-mount “WS” style equivalents (e.g. 1N4148WS) |

## Typical circuits

```
Logic clamp / input protection:

  MCU GPIO ──┬──>|-- 1N4148 ── +3.3 V / +5 V
             │     (cathode toward rail)
             └──>|-- 1N4148 ── GND
                   (anode toward GND)

Steering / OR-ing two open-collector signals:

  SIG_A ──>|--┐
              ├── OUT
  SIG_B ──>|--┘
```

## Common mistakes

- **Using a 1N4007 where speed matters:** A 1N400x has microsecond-class recovery and large capacitance — wrong for fast logic edges or RF. Use the 1N4148 (or a Schottky) instead.
- **Expecting 1 A capability:** Continuous rating is ~200 mA. For motor/relay flyback at higher currents, use a 1N400x or a proper catch diode sized for the load.
- **Reversed band in a clamp:** Band (cathode) must face the positive rail in a high-side clamp; reverse it and you short the supply through the diode.

## Notes

- Electrically interchangeable with most “1N914-class” glass signal diodes in hobby circuits; check `Vf` / `trr` only when matching a precision timing or RF design.
- Datasheet cited is onsemi’s combined **1N914 / 1N4148 / 1N4448** family PDF.
