## Overview

The **MBI6001** (MBI6001-N1N) is an offline high-voltage constant-current LED driver IC manufactured by Macroblock. Designed specifically for mains-powered LED lighting fixtures (such as GU10/E27 LED bulbs, T8 LED tubes, downlights, and architectural LED strips), it operates directly from rectified AC mains power.

Handling input DC voltages up to **$500\text{ Volts}$** (from rectified $85\text{V} \dots 265\text{V}$ AC mains), the MBI6001 delivers constant current outputs up to **$350\text{ mA}$** with high electrical efficiency ($> 90\%$). Output current is set precisely using an external current sense resistor ($R_{EXT}$).

## Quick reference

| | |
|---|---|
| **Input DC Voltage Limit (`HV`)**| Up to $500\text{ V}$ DC |
| **AC Mains Input Range** | $85\text{ V}$ to $265\text{ V}$ AC (50/60 Hz) |
| **Output Current Capability** | Adjustable up to $350\text{ mA}$ (Set by external resistor $R_{EXT}$) |
| **System Efficiency** | $> 90\%$ typical |
| **Protection Features** | Thermal Foldback, Open-LED Protection, Short-LED Protection |
| **Dimming** | Compatible with TRIAC line-voltage dimmers and PWM dimming inputs |
| **Package** | 8-pin SOP / DIP-8 |

## Pinout (SOP-8 Package)

```
             ┌───┴───┐
        GND 1│ 1   8 │ HV (High Voltage Input up to 500V)
       REXT 2│       │ 7 NC
        PWM 3│MBI6001│ 6 DRAIN (Internal Power MOSFET Drain)
       VDD  4│       │ 5 CS (Current Sense Input)
             └───────┘
```

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `GND` | Power | Ground reference (0 V) |
| 2 | `REXT` | Input | Constant Current Programming Pin (Connect resistor $R_{EXT}$ to GND) |
| 3 | `PWM` | Input | PWM Dimming Control Input (Pull HIGH for 100% brightness) |
| 4 | `VDD` | Power | Internal Low Voltage Supply Output |
| 5 | `CS` | Input | Peak Current Sense Input |
| 6 | `DRAIN` | Output | Internal High-Voltage Power MOSFET Drain Connection |
| 7 | `NC` | Unused | No Connection (High-voltage clearance pin) |
| 8 | `HV` | Power | High-Voltage Rectified DC Input (+100V to +500V DC) |

## Output Current Formula

The output constant current ($I_{OUT}$) is programmed via external resistor $R_{EXT}$ connected to Pin 2:

$$ I_{OUT} = \frac{V_{REXT}}{R_{EXT}} \times K_I \approx \frac{1.20\text{V}}{R_{EXT}} \times 250 $$

## Safety & High-Voltage Warning

> [!CAUTION]
> High Voltage Danger!
> Circuits utilizing the MBI6001 connect directly to non-isolated **$120\text{V} / 230\text{V}$ AC Mains voltage**. Touching any portion of the PCB while powered poses severe electrical shock hazards. Always use an isolation transformer and protective enclosures during testing.

## Common mistakes

- **Omitting input EMI filter and surge varistor:** Rectified mains spikes easily exceed $500\text{V}$ during power-on transients. Always include a MOV (metal oxide varistor) and EMI choke at the AC input.

## Notes

- **MBI6001 vs HV9910:** MBI6001 incorporates internal thermal foldback protection that automatically reduces current if the LED heatsink temperature exceeds safe thresholds.
