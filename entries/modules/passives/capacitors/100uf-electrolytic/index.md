## Overview

The **100µF polarized aluminum electrolytic capacitor** is the indispensable bulk reservoir component of electronic circuits. Stocked in every electronics lab and component assortment, it serves as the frontline buffer against low-frequency voltage sags, ripple, and load transients in DC power supplies.

Unlike ceramic capacitors which provide small capacitances ($< 1\ \mu\text{F}$) with near-zero ESR, aluminum electrolytics achieve massive capacitance in a compact volume by using a microscopic electrochemical dielectric layer. A coiled strip of etched high-purity aluminum foil is coated with an ultra-thin insulating film of aluminum oxide ($Al_2O_3$), soaked in a liquid or gel electrolyte, and sealed inside a cylindrical aluminum can with a safety pressure-relief vent.

In power distribution networks, the 100µF electrolytic handles heavy low-frequency current surges from motors, relays, audio amplifiers, and step-down converters. Because its internal construction creates parasitic series inductance, it is virtually always paired in parallel with a [100nF ceramic capacitor](file:///home/kaguya/Code/github/stavros-tsioulis/voltdocs-public/entries/modules/passives/capacitors/100nf-ceramic/entry.yaml) to handle high-frequency switching noise.

## Quick reference

| Parameter | Value | Notes |
|---|---|---|
| **Nominal Capacitance** | $100\ \mu\text{F} = 100,000\text{ nF} = 0.1\text{ mF}$ | Bulk energy reservoir |
| **Typical Voltage Ratings** | $16\text{V},\ 25\text{V},\ 35\text{V},\ 50\text{V}$ DC | Choose rating $\ge 1.5\times - 2\times$ rail voltage |
| **Tolerance** | $\pm 20\%$ (`M`) | Standard electrolytic tolerance |
| **Polarity** | **Polarized** (Cathode stripe / short lead) | Reverse polarity destroys the capacitor |
| **Equivalent Series Resistance (ESR)** | $0.3\ \Omega - 1.5\ \Omega$ at $100\text{ kHz}$ | Varies by voltage rating and temperature |
| **Ripple Current Rating** | $200\text{ mA} - 450\text{ mA}_{RMS}$ | Continuous AC ripple current limit |
| **Operating Temperature Range** | $-40^\circ\text{C}$ to $+85^\circ\text{C}$ or $+105^\circ\text{C}$ | $105^\circ\text{C}$ rated parts offer $4\times$ longer life |
| **Physical Package** | Radial Leaded Can: $5\text{ mm} \times 11\text{ mm}$ (typ.) | $2.0\text{ mm} / 2.5\text{ mm}$ lead spacing |

## Value & markings

Radial electrolytic capacitors are large enough that their specifications are printed directly in plain human-readable text on the plastic insulation sleeve, rather than using cryptic 3-digit numerical codes.

### Polarity identification

> [!CAUTION]
> Aluminum electrolytic capacitors are strictly **polarized**. Connecting an electrolytic capacitor backwards causes rapid reverse electrochemical breakdown, internal gas generation, and potential violent rupture or venting.

```
          +-----------------+
         /       ___         \     <-- Top safety vent (scored cross/K)
        |       |   |         |
        |  --   |100|         |    <-- Value: 100µF
        |  --   | µF|         |
        |  --   |   |         |
        |  --   |25V|         |    <-- Rated DC working voltage
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

1. **Negative Stripe:** A prominent vertical stripe (typically white, gold, or black) runs down the side of the cylindrical sleeve with clear minus signs (`-`). The terminal aligned with this stripe is the **Cathode ($-$)**.
2. **Lead Length (Uncut Leads):**
   - **Long Lead:** Anode ($+$, positive)
   - **Short Lead:** Cathode ($-$, negative)
3. **Safety Vent:** The top of the aluminum can features an embossed cross (`+`) or `K` score pattern. In the event of catastrophic overvoltage, reverse polarity, or overheating, this weakened score opens to release expanding hydrogen gas safely rather than exploding the aluminum canister.

## Key parameters

| Parameter | Typical Value | Unit | Notes |
|---|---|---|---|
| Capacitance | 100 | $\mu\text{F}$ | Measured at $120\text{ Hz}$, $25^\circ\text{C}$ |
| Rated DC Voltage ($V_R$) | 25 | V | Continuous DC working voltage |
| Surge Voltage ($V_S$) | 32 | V | Short-term transient withstand ($< 30\text{ s}$) |
| Tolerance | $\pm 20$ | % | Standard commercial grade |
| ESR ($100\text{ kHz}$) | 0.8 | $\Omega$ | Lower ESR versions available ($0.1\ \Omega - 0.3\ \Omega$) |
| Ripple Current ($100\text{ kHz}$, $105^\circ\text{C}$) | 280 | $\text{mA}_{RMS}$ | Internal self-heating limit |
| DC Leakage Current ($I_L$) | $< 25$ | $\mu\text{A}$ | After 2 minutes ($I_L \le 0.01 C V$ or $3\mu\text{A}$) |
| Dissipation Factor ($\tan \delta$) | 0.14 | — | At $120\text{ Hz}$, $20^\circ\text{C}$ |
| Endurance / Load Life | 2,000 | hours | At rated voltage and maximum temperature ($105^\circ\text{C}$) |

## Electrical characteristics & thermal lifetime

### 1. The Arrhenius 10-degree rule
The lifespan of a wet electrolytic capacitor is governed by the gradual evaporation of its liquid electrolyte through the rubber end seal. According to the Arrhenius relationship:
$$\text{Lifetime} \approx L_0 \times 2^{\frac{T_{max} - T_{actual}}{10}}$$
Where $L_0$ is the rated lifetime at maximum temperature (e.g. 2,000 hours at $105^\circ\text{C}$).
- Operating at $105^\circ\text{C}$: **2,000 hours** (~83 days continuous)
- Operating at $85^\circ\text{C}$: **8,000 hours** (~11 months)
- Operating at $65^\circ\text{C}$: **32,000 hours** (~3.6 years)
- Operating at $45^\circ\text{C}$: **128,000 hours** (~14.6 years)

Keeping electrolytics away from hot heatsinks, power transformers, and power resistors is the single most effective way to guarantee reliability.

### 2. Voltage derating
Always select an electrolytic capacitor with a rated voltage at least **$1.5\times$ to $2\times$** higher than the nominal operating voltage.
- For a **$5\text{V}$ rail:** Use a **$16\text{V}$ or $25\text{V}$** capacitor.
- For a **$12\text{V}$ rail:** Use a **$25\text{V}$ or $35\text{V}$** capacitor.
- For a **$24\text{V}$ rail:** Use a **$35\text{V}$ or $50\text{V}$** capacitor.

## Combinations

### Parallel connection (bulk expansion & ESR reduction)
Connecting multiple 100µF capacitors in parallel sums their capacitance and lowers overall ESR:
$$C_{total} = C_1 + C_2 + \dots + C_n$$
$$\text{ESR}_{total} = \frac{\text{ESR}}{n}$$

*Example:* Placing two $100\mu\text{F}$ capacitors in parallel creates a $200\mu\text{F}$ reservoir with half the ESR and double the allowable ripple current rating.

### Series connection (higher voltage rating)
$$C_{total} = \frac{C_1 \times C_2}{C_1 + C_2} = 50\mu\text{F}$$
> [!WARNING]
> Because electrolytic capacitors have uneven internal DC leakage currents, series-connected electrolytics will distribute voltage unequally. **Balancing resistors** (e.g., $100\text{ k}\Omega$ $1\%$ resistors in parallel with each capacitor) are mandatory to prevent one capacitor from exceeding its voltage rating.

## Typical circuits

### 1. Power supply bulk reservoir & linear regulator stabilization

```
    AC Transformer / Rectifier / Unregulated DC
               o------+--------------------+--------------------+---o +5V Regulated
                      |                    |                    |
                     ---                  --- [LM7805]         ---
               C1   |   | 100uF          |   |            C3  |   | 100nF
               Bulk |   | 25V             --- Bypass      Cer |   | Ceramic
                    |   |                 --- 100nF           |   |
                     ---                   |                   ---
                      |                    |                    |
               o------+--------------------+--------------------+---o GND
```

In this classic topology:
- **C1 (100µF Electrolytic):** Smooths the rectified $100\text{ Hz} / 120\text{ Hz}$ line hum and provides reservoir current during load steps.
- **C2 & C3 (100nF Ceramics):** Located immediately at the regulator's pins, suppressing high-frequency parasitic oscillation that the electrolytic's parasitic inductance cannot reach.

### 2. Audio amplifier AC coupling (DC blocking)
When feeding an audio signal into a loudspeaker or headphone driver from a single-supply amplifier, a 100µF capacitor blocks DC bias voltage while passing low-frequency bass audio:
$$f_{-3dB} = \frac{1}{2\pi R_{load} C} = \frac{1}{2\pi \times 32\Omega \times 100\mu\text{F}} \approx 49.7\text{ Hz}$$
- Connect the **Anode (+)** to the amplifier output (DC bias voltage, e.g. $+6\text{V}$).
- Connect the **Cathode (-)** to the speaker/headphone terminal (ground reference).

## Common mistakes

1. **Reverse polarity connection:**
   - *Problem:* Applying negative voltage to the positive lead dissolves the dielectric $Al_2O_3$ layer. A massive leakage current flows, boiling the electrolyte into gas and venting the capacitor.
   - *Fix:* Always align the negative stripe with circuit Ground or the most negative potential.
2. **Exceeding rated DC voltage:**
   - *Problem:* Voltage spikes break down the thin oxide layer, leading to internal arcing and dielectric short-circuit.
   - *Fix:* Derate working voltage by at least 25–50%.
3. **Neglecting high-frequency ceramic bypass:**
   - *Problem:* Because radial electrolytics have wound foil construction with $10\text{ nH} - 30\text{ nH}$ of equivalent series inductance (ESL), their impedance rises rapidly above $500\text{ kHz}$. At digital clock frequencies ($10\text{ MHz} - 100\text{ MHz}$), a 100µF electrolytic behaves like an open inductor, failing to decouple digital chips.
   - *Fix:* Always place a [100nF ceramic capacitor](file:///home/kaguya/Code/github/stavros-tsioulis/voltdocs-public/entries/modules/passives/capacitors/100nf-ceramic/entry.yaml) in parallel directly at the IC power pins.
4. **Thermal cooking next to heatsinks:**
   - *Problem:* Locating electrolytic capacitors directly against hot power MOSFET heatsinks or high-wattage power resistors dries out the liquid electrolyte within months, causing ESR to skyrocket and circuits to malfunction ("bad caps").
   - *Fix:* Maintain at least $10\text{ mm} - 20\text{ mm}$ physical clearance from heat-generating components.

## Notes

- For compact surface-mount designs, modern $100\mu\text{F}$ SMD aluminum electrolytic capacitors (vertical cylindrical "V-chip" cans) or high-capacitance $1206 / 1210$ multi-layer ceramic capacitors (MLCCs) are often used.
- When replacing capacitors in switching power supplies (motherboards, SMPS output stages), specify **Low-ESR** series (e.g. Nichicon PW/HE, Panasonic FR/FM, Rubycon ZLJ) rather than general-purpose 85°C varieties.
