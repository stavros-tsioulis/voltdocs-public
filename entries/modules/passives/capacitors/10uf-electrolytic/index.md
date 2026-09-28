## Overview

The **10µF polarized aluminum electrolytic capacitor** is a universal intermediate reservoir component found across power supplies, linear regulator output stages, analog audio circuits, and RC timing blocks.

Offering a convenient compromise between physical miniature size (typically a compact $4\text{ mm} \times 7\text{ mm}$ or $5\text{ mm} \times 11\text{ mm}$ aluminum cylinder) and substantial charge storage ($10,000\text{ nF}$), it fills the gap between sub-microfarad ceramic bypass capacitors and bulky $100\mu\text{F} - 1000\mu\text{F}$ power reservoirs.

Importantly, its moderate Equivalent Series Resistance (typically $1\ \Omega - 3\ \Omega$) is not merely a parasitics byproduct, but an **essential stability requirement** for dozens of classic linear regulators (e.g. LM317, LM7805, AMS1117, LP2950). In these circuits, the capacitor's internal ESR creates a stabilizing "zero" in the control feedback loop, preventing phase lag that would otherwise lead to oscillation with ultra-low-ESR modern MLCC ceramic capacitors.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Nominal Capacitance** | $10\ \mu\text{F} = 10,000\text{ nF}$ | Intermediate bulk reservoir |
| **Typical Voltage Ratings** | $16\text{V},\ 25\text{V},\ 50\text{V}$ DC | Choose rating $\ge 1.5\times - 2\times$ rail voltage |
| **Tolerance** | $\pm 20\%$ (`M`) | Standard commercial tolerance |
| **Polarity** | **Polarized** (Cathode stripe / short lead) | Reverse polarity destroys the component |
| **Equivalent Series Resistance (ESR)** | $1.0\ \Omega - 3.0\ \Omega$ at $100\text{ kHz}$ | Ideal for linear regulator loop stability |
| **Ripple Current Rating** | $60\text{ mA} - 120\text{ mA}_{RMS}$ | Internal self-heating limit |
| **Operating Temperature Range** | $-40^\circ\text{C}$ to $+85^\circ\text{C}$ or $+105^\circ\text{C}$ | $105^\circ\text{C}$ parts provide superior longevity |
| **Physical Package** | Radial Leaded Miniature Can ($4\times 7\text{ mm}$ or $5\times 11\text{ mm}$) | $2.0\text{ mm} / 2.5\text{ mm}$ lead spacing |

## Value & markings

Miniature radial electrolytic capacitors print their nominal specifications directly on the outer insulating sleeve:

### Polarity identification

> [!CAUTION]
> Aluminum electrolytic capacitors are strictly **polarized**. Applying reverse DC voltage causes internal electrochemical breakdown, boiling of the electrolyte, gas buildup, and component venting or rupture.

```
          +-----------------+
         /       ___         \     <-- Top safety vent (embossed score)
        |       |   |         |
        |  --   | 10|         |    <-- Value: 10µF
        |  --   | µF|         |
        |  --   |   |         |
        |  --   |50V|         |    <-- Rated DC working voltage
        |  --   |   |         |
        |  --   |105|         |    <-- Max operating temperature (105°C)
         \     -------       /
          +--------+--------+
                   |
             +-----+-----+
             |           |
             |           |
             |           |
             -           +
          Cathode      Anode
         (Negative)  (Positive)
        [Short lead] [Long lead]
```

1. **Negative Stripe:** A prominent vertical stripe down the side of the sleeve bearing minus signs (`-`) denotes the **Cathode ($-$)** pin.
2. **Lead Length (Uncut Leads):**
   - **Long Lead:** Anode ($+$, positive)
   - **Short Lead:** Cathode ($-$, negative)
3. **Safety Vent:** Miniature cans often include a relief score on the top or rubber bottom plug designed to vent internal pressure before catastrophic shell rupture.

## Key parameters

| Parameter | Typical Value | Unit | Notes |
|---|---|---|---|
| Capacitance | 10 | $\mu\text{F}$ | Measured at $120\text{ Hz}$, $25^\circ\text{C}$ |
| Rated Working Voltage ($V_R$) | 50 | V | Continuous DC working voltage |
| Surge Voltage ($V_S$) | 63 | V | Short-term transient rating ($< 30\text{ s}$) |
| Tolerance | $\pm 20$ | % | Standard commercial grade |
| ESR ($100\text{ kHz}$) | 1.8 | $\Omega$ | Measured at $20^\circ\text{C}$ |
| Ripple Current ($100\text{ kHz}$, $105^\circ\text{C}$) | 95 | $\text{mA}_{RMS}$ | Continuous AC ripple rating |
| DC Leakage Current ($I_L$) | $< 5$ | $\mu\text{A}$ | After 2 minutes ($I_L \le 0.01 C V$ or $3\mu\text{A}$) |
| Dissipation Factor ($\tan \delta$) | 0.12 | — | At $120\text{ Hz}$, $20^\circ\text{C}$ |
| Endurance / Load Life | 2,000 | hours | At rated voltage and $105^\circ\text{C}$ |

## Voltage regulator loop stability (the ESR sweet spot)

One of the most important engineering aspects of the 10µF electrolytic capacitor is its interaction with classic linear voltage regulators:

```
        Unregulated DC                     Regulated DC
             +Vin o----+------[ LDO ]------+---------o +Vout
                       |      Regulator    |
                      ---                 ---
                      --- C_in            --- C_out (10µF Electrolytic)
                       |  (100nF Cer)      |  ESR = 1.0 - 2.0 Ohms
                       |                   |  Provides feedback zero!
                      GND                 GND
```

Many popular low-dropout (LDO) regulators (such as AMS1117, LM1117, LP2950, LM2931) rely on the capacitor's Equivalent Series Resistance (ESR) to introduce an internal phase-lead zero:
$$f_Z = \frac{1}{2\pi \times \text{ESR} \times C_{out}}$$

If an engineer replaces the recommended 10µF electrolytic capacitor with a modern 10µF multi-layer ceramic capacitor (MLCC) with an ESR of $5\text{ m}\Omega$, this stabilizing zero shifts to an extremely high frequency. As a result, the regulator's phase margin degrades to near zero, causing the output voltage to oscillate uncontrollably with high-amplitude AC ripple. The 10µF electrolytic operates naturally inside the regulator's required stability "tunnel" ($0.2\ \Omega < \text{ESR} < 2\ \Omega$).

## Combinations

### Parallel connection (capacity scaling)
Connecting capacitors in parallel sums their capacitance:
$$C_{total} = C_1 + C_2 = 10\mu\text{F} + 10\mu\text{F} = 20\mu\text{F}$$
Total ESR is halved, and ripple current capability doubles.

### Series connection (voltage scaling)
$$C_{total} = \frac{C_1 \times C_2}{C_1 + C_2} = 5\mu\text{F}$$
> [!WARNING]
> Parallel balancing resistors (e.g. $220\text{ k}\Omega$) across each capacitor are required to prevent unequal DC voltage distribution caused by differential leakage currents.

## Typical circuits

### 1. Audio preamplifier DC blocking (AC signal coupling)
When routing analog audio between single-supply amplifier stages, a 10µF electrolytic capacitor isolates the DC bias voltage while passing audible frequencies down to bass level:

```
    Stage 1                      Stage 2
    Output (Bias = 4.5V)         Input (Bias = 2.5V)
           o-------+||------------o
                  C1 (10uF)
                (+)      (-)
```
For a typical $10\text{ k}\Omega$ input impedance:
$$f_{-3dB} = \frac{1}{2\pi \times R_{in} \times C} = \frac{1}{2\pi \times 10,000\Omega \times 10\mu\text{F}} \approx 1.59\text{ Hz}$$
This passes the entire audible audio band ($20\text{ Hz} - 20\text{ kHz}$) with flat frequency response and zero phase distortion.
*(Always connect the Anode (+) to the node with the higher positive DC bias voltage).*

### 2. RC timing & delay generation
In 555 timers and reset delay generators:
$$t_{delay} \approx 1.1 \times R \times C$$
With $R = 100\text{ k}\Omega$ and $C = 10\mu\text{F}$, a delay of approximately $1.1\text{ seconds}$ is produced.

## Common mistakes

1. **Connecting in reverse polarity:**
   - *Problem:* Reverse voltage dissolves the dielectric oxide film, generating heat and hydrogen gas, causing the rubber bottom plug to pop out or the can to rupture.
   - *Fix:* Verify polarity markings carefully; cathode stripe indicates negative terminal.
2. **Inappropriate substitution with low-ESR ceramic caps:**
   - *Problem:* Blindly swapping a 10µF electrolytic on an AMS1117 or LM1117 regulator with a 10µF ceramic cap causes severe voltage oscillation and system crashes.
   - *Fix:* Keep the 10µF electrolytic, or add a $0.5\ \Omega - 1.0\ \Omega$ series resistor if using a ceramic capacitor.
3. **Exceeding temperature limits:**
   - *Problem:* Placing the capacitor against hot power transistors drops its operational lifetime by half for every $10^\circ\text{C}$ rise in temperature.
   - *Fix:* Provide ventilation and maintain spacing from heat sinks.
4. **Using for high-frequency bypass without ceramic companions:**
   - *Problem:* At frequencies above $1\text{ MHz}$, parasitic inductance dominates the impedance.
   - *Fix:* Always place a [100nF ceramic capacitor](file:///home/kaguya/Code/github/stavros-tsioulis/voltdocs-public/entries/modules/passives/capacitors/100nf-ceramic/entry.yaml) in parallel for high-frequency noise suppression.

## Notes

- Modern miniature SMD electrolytic capacitors (cylindrical "can" style with flat solder base) share the same electrical specifications and polarity conventions as radial through-hole parts.
- When circuit size is constrained and ceramic is desired, modern LDOs specifically designated "ceramic capacitor stable" should be chosen.
