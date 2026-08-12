## Overview

The **LM2587** (LM2587T-ADJ / LM2587S-ADJ) is a 5A step-up (boost), flyback, and forward converter voltage regulator IC manufactured by Texas Instruments. Part of the **SIMPLE SWITCHER** family, it is the higher-power upgrade to the LM2577, operating at nearly double the switching frequency (**100 kHz**) and featuring an internal **5.0A NPN power switch**.

Operating over an input voltage range of **4.0V to 40.0V DC**, the LM2587 is widely used in high-power DC-DC boost modules, isolated flyback power supplies, automotive power adapters, and battery charging step-up regulators.

## Quick reference

| | |
|---|---|
| **Input Supply Voltage (`VIN`)** | 4.0 V to 40.0 V DC |
| **Output Switch Voltage (`VOUT`)**| Up to $60.0\text{ V}$ DC (Internal switch rated for 65V breakdown) |
| **Internal Switch Current** | $5.0\text{ A}$ continuous switch limit |
| **Switching Frequency** | $100\text{ kHz}$ internal fixed oscillator |
| **Feedback Voltage (`VFB`)** | $1.23\text{ V}$ reference |
| **Available Versions** | Fixed 12V (`LM2587-12`), Fixed 15V (`LM2587-15`), Adjustable (`LM2587-ADJ`) |
| **Special Feature** | Built-in Soft-Start & Under-Voltage Lockout (UVLO) |
| **Package** | TO-220-5 (Through-hole) / TO-263-5 DDPAK (SMD) |

## Pinout (TO-220-5 Package)

Looking at the **front labeled face** of the 5-lead package with leads pointing down:

```
        ┌─────────────┐
        │   O   [TAB] │  (Metal Mounting Tab = GROUND / GND)
        ├─────────────┤
        │   LM2587T   │  (Front Package Face)
        └─┬─┬─┬─┬─┬───┘
          1 2 3 4 5
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `COMP` | Input | Frequency Compensation Input (Connect $R_C + C_C$ network to GND) |
| 2 | `FB` | Input | Feedback Voltage Sense Input ($1.23\text{V}$ reference to GND) |
| 3 | `GND` | Power | Ground Reference (0 V; Connected internally to Metal Tab!) |
| 4 | `SW` | Output | Internal NPN Power Switch Collector Output (Connect to Inductor / Transformer & Schottky Diode) |
| 5 | `VIN` | Power | Unregulated Supply Input (+4.0V to +40V DC) |

## Output Voltage Formula (Adjustable Version)

$$ V_{OUT} = 1.23\text{V} \times \left(1 + \frac{R_1}{R_2}\right) $$

Where $R_1$ is connected between `VOUT` and `FB`, and $R_2$ is connected between `FB` and `GND`.

## Common mistakes

- **Inadequate heatsink for 5A loads:** Switching $5.0\text{ A}$ generates significant internal heat in the TO-220 package ($V_{SAT} \times 5\text{A} \approx 4\text{ W}$). Bolt the package tab securely to a large metal heatsink.
- **Using undersized inductors:** A 5A boost converter requires a heavy-duty toroidal power inductor rated for $\ge 6.0\text{ A}$ saturation current to avoid magnetic core saturation.

## Notes

- **LM2587 vs LM2577:** LM2587 handles $5.0\text{ A}$ current (vs $3.0\text{ A}$ on LM2577) and operates at $100\text{ kHz}$ (vs $52\text{ kHz}$ on LM2577), allowing smaller inductors.
