# Component Documentation Layouts

A set of markdown layouts for documenting electronic components. The goal is to
have pages that look and read the same way regardless of who wrote them, while still
leaving room for the quirks of any individual part.

These are **guidelines, not schemas**. Every layout shares a common spine so a
reader always knows where to look, but any section can be dropped, reordered, or
extended when a part demands it. Authoring hints are embedded as HTML comments
(`<!-- ... -->`) so they guide the writer without rendering on the page — delete
them or keep them, your choice.

---

## Design principles

### Write for three readers at once

Every layout is arranged so all three of these people are served by the *same*
page, just by reading different parts of it:

| Reader | What they want | Where the layout serves them |
|---|---|---|
| **The learner** | What is this, why does it exist, how do I picture it, what will bite me | Overview, plain-language pin/parameter descriptions, "Common mistakes", worked examples |
| **The reference user** | A specific value, fast, with its measurement conditions | Quick Reference block, pinout/parameter/register tables, min/typ/max columns |
| **The teacher** | A conceptual hook and something demonstrable | Overview analogies, "Typical circuits", "Common mistakes" as discussion points |

The practical consequence: **put scannable tables near the top, put prose and
examples below.** A reference user should never have to read a paragraph to find
a pin number; a learner should never hit a register map before they know what
the part does.

### One consistent spine

By default, VoltDocs structures title, summary, and other frontmatter on a sidebar,
that information doens't belong on the markdown body, but on the designated manifest.

Every page, whatever its category, follows this order. Categories add, remove,
or specialise sections — they never shuffle the ones they keep.

1. **Overview** — what it is / does / why
2. **Quick Reference** — the at-a-glance block
3. **Terminals** — pinout / polarity / contacts (whatever applies)
4. **The technical core** — the section that differs most by category
   (specifications, register map, characteristic curves, decoding…)
5. **Usage** — wiring and example circuits/code
6. **Common mistakes**
7. **Notes & further reading**

---

## Shared conventions

### Callouts

Keep the vocabulary small and consistent so readers learn to trust the symbols:

- `⚠️` **Warning** — anything that destroys the part or is unsafe (absolute
  maximum ratings, reversed polarity, missing flyback diode).
- `💡` **Tip** — a practical shortcut or gotcha-avoider.
- `📌` **Note** — context worth knowing but not urgent.

### Tables and units

- Anything tabular goes in a table, not prose.
- Always write the unit next to the value (`3.3 V`, `40 mA`, `13.56 MHz`).
- For parts a datasheet would spec across conditions, use **Min / Typ / Max**
  columns and always give the **Conditions** — a value without its test
  conditions is close to useless for a reference user.
- Use `inline code` for pin names, register names, part numbers, and signals
  (`MOSI`, `COMMAND`, `Vgs(th)`, `2N2222`).

---

## The categories

Grouping by shape gives **six specific layouts plus one generic default**:

| Layout | Covers | Why it's its own shape |
|---|---|---|
| **Module** | Breakout/sensor/comms boards (MFRC522, MPU6050, ESP32 board, L298N) | Pinout **+** a communication protocol **+** a register map. The only layout that routinely needs all three. |
| **Integrated Circuit** | Bare chips (74HC595, NE555, op-amps, drivers) | Absolute maximum ratings and min/typ/max electrical characteristics dominate; package/footprint variants matter. |
| **Transistor** | BJT, MOSFET, JFET, IGBT | Three terminals, operating regions, biasing, and characteristic curves — a shape nothing else shares. |
| **Diode & LED** | Rectifier, Schottky, Zener, TVS, LED | Polarised two-terminal, unidirectional; forward/reverse behaviour and polarity marking are the whole story. |
| **Passive** | Resistor, capacitor, inductor | Value-defined two-terminal; the core is a value + tolerance + rating + how to decode the markings. |
| **Electromechanical** | Relay, motor, switch, buzzer, connector | Has *mechanical* specs and a drive requirement alongside the electrical ones. |
| **Default** | Anything else (crystal, fuse, thermistor, antenna) | Fallback spine so a page always has somewhere to live. |

The layouts follow.

---

## Layout: Module

The richest layout, and the one your notes will lean on most. A module is a
board that wraps one or more chips with support circuitry and breaks the useful
signals out to a header. Readers arrive wanting to wire it up and talk to it, so
this layout leads with the pinout and the interface, and reserves a full
**register map** for the common case where you write to addresses to configure
the thing.

````markdown
# <Module name>

> What it is and what it's for.
<!-- e.g. "13.56 MHz RFID reader/writer breakout, controlled over SPI." -->

## Overview

<!-- learner + teacher: what it does, why you'd reach for it, the mental model.
     2–4 short paragraphs, no jargon that isn't defined. -->

## Quick reference

<!-- reference: the values someone checks before wiring. Keep it tiny. -->

| | |
|---|---|
| **Operating voltage** | |
| **Logic level** | |
| **Interface** | |
| **Default address** | <!-- I2C address, or SPI note --> |
| **Current draw** | |
| **Key spec** | <!-- the one number that defines this part --> |

## Pinout

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` | Power | |
| 2 | `GND` | Power | |
| 3 | | | |

<!-- Type = Power / Ground / Digital I/O / Analog / Clock / Bus. Describe each
     pin in plain language — the learner reads this column, the reference user
     reads the name column. -->

## Specifications

| Parameter | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|
| Supply voltage | | | | V | |
| Operating current | | | | mA | |
| Operating temperature | | | | °C | |

## Communication

<!-- reference + learner: the protocol, how to address the device, framing,
     clock speeds, byte order. Enough that someone could write a driver. -->

- **Protocol:**
- **Max clock:**
- **Frame format:**

## Register map

<!-- Omit this whole section for modules with no programmable registers.
     Summary table first, then expand only the registers worth explaining. -->

| Address | Register | Access | Reset | Description |
|---|---|---|---|---|
| `0x00` | | R/W | `0x00` | |
| `0x01` | | R | — | |

### `0xNN` — `REGISTER_NAME`

| Bit(s) | Field | Access | Reset | Description |
|---|---|---|---|---|
| 7 | | R/W | 0 | |
| 6:4 | | R/W | 000 | |
| 3:0 | | R | 0000 | |

<!-- Add a detail block like this only for registers a reader will actually
     configure. Leave the rest in the summary table. -->

## Wiring

<!-- learner + teacher: a concrete hookup to one common MCU. A table or a short
     list beats a paragraph. -->

| Module | → | MCU (e.g. Arduino Uno) |
|---|---|---|
| `VCC` | | 3.3 V |
| `GND` | | GND |
| `SCK` | | 13 |

> ⚠️ <!-- voltage/level warnings, e.g. "Not 5 V tolerant." -->

## Example

```cpp
// Minimal working example — read one value / do one thing.
```

## Common mistakes

<!-- learner + teacher. Real ones, phrased as "if X, check Y". -->

- 
- 

## Notes

- 
````

---

## Layout: Integrated Circuit

For bare chips rather than boards. The centre of gravity shifts from "how do I
wire it" to "what are its limits and exact characteristics". **Absolute maximum
ratings** get their own prominent, warning-flagged section because exceeding
them destroys the part, and electrical characteristics are spec'd across
conditions the way a datasheet would. Package variants matter here in a way they
don't for modules.

````markdown
# <IC name / part number>

> One sentence: function and family.
<!-- e.g. "8-bit serial-in, parallel-out shift register." -->

## Overview

<!-- learner + teacher: the function in plain terms, common use, block-level
     mental model. -->

## Quick reference

| | |
|---|---|
| **Function** | |
| **Supply range** | |
| **Logic family** | <!-- TTL / CMOS / ... --> |
| **Packages** | <!-- DIP-8, SOIC-8, ... --> |
| **Key spec** | |

## Pin configuration

<!-- reference: pinout per package. An ASCII pin diagram helps learners; the
     table serves everyone. -->

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | | | |

## Functional description

<!-- learner + teacher: the internal blocks / modes of operation and how they
     interact. This is where the "how it works" lives. -->

## Absolute maximum ratings

> ⚠️ Stresses beyond these values cause permanent damage. These are limits, not
> operating conditions.

| Parameter | Rating | Unit |
|---|---|---|
| Supply voltage | | V |
| Input voltage | | V |
| Operating temperature | | °C |

## Electrical characteristics

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| | | | | | | |

<!-- Split into DC and AC/timing sub-tables if the part warrants it. -->

## Register map

<!-- Only for programmable/digital ICs. Same structure as the Module layout:
     summary table, then per-register bitfield detail for the important ones.
     Delete for analog / logic parts. -->

## Timing

<!-- reference + teacher: timing diagram (described, ASCII, or linked) plus the
     numbers — setup, hold, propagation delay — with conditions. Omit if none. -->

## Typical application

```
<!-- A minimal, correct schematic-in-text or code snippet. Note decoupling,
     pull-ups, and anything a first-time user forgets. -->
```

## Package & footprint

<!-- reference: package options, pin pitch, footprint notes. -->

## Common mistakes

- 

## Notes

- 
````

---

## Layout: Transistor

Three-terminal active devices — BJTs and every flavour of FET. This layout's
distinctive core is the trio of **terminal identification** (learners get the
legs wrong constantly), **operating regions / biasing**, and **characteristic
curves**. It splits the two main jobs — switching and amplifying — because a
reader almost always shows up wanting one or the other.

````markdown
# <Part number>

> One sentence: type, polarity, and headline use.
<!-- e.g. "Logic-level N-channel MOSFET for low-side switching." -->

## Overview

<!-- learner + teacher: switch vs. amplifier framing. The one-paragraph mental
     model ("a valve controlled by the gate/base"). -->

## Quick reference

| | |
|---|---|
| **Type** | <!-- NPN / N-channel / ... --> |
| **Max V** | <!-- Vce / Vds --> |
| **Max I** | <!-- Ic / Id --> |
| **Control threshold** | <!-- hFE range / Vgs(th) --> |
| **Package** | |

## Terminal identification

<!-- all readers, learner especially. Which physical leg is which, per package.
     A pin diagram earns its place here. -->

| Pin | Terminal | |
|---|---|---|
| 1 | | |
| 2 | | |
| 3 | | |

> 💡 <!-- e.g. "TO-92 flat side facing you, legs down: E-B-C." -->

## Key parameters

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Collector–emitter voltage | Vce | | | | V | |
| Continuous collector current | Ic | | | | A | |
| DC current gain | hFE | | | | | at Ic = … |

<!-- For FETs swap in Vds, Id, Vgs(th), Rds(on) — Rds(on) with its Vgs is the
     number people care about most for switching. -->

## Operating regions

<!-- learner + teacher: cutoff / active(saturation for FET) / saturation.
     What each region means and what puts the device there. -->

## Characteristic curves

<!-- teacher + reference: transfer curve and output curves — described, sketched
     in ASCII, or linked. Note the key inflection points. -->

## Typical circuits

### As a switch
```
<!-- Base/gate resistor, load, flyback diode if inductive. -->
```

### As an amplifier
```
<!-- Bias network, the operating point. Omit if the part is switch-only. -->
```

## Selection & substitutes

<!-- reference: comparable parts and what changes if you swap. -->

## Common mistakes

- <!-- e.g. "Standard MOSFETs need >4.5 V on the gate; won't fully turn on from
       a 3.3 V pin — use a logic-level part." -->
- <!-- "No gate/base resistor", "flyback diode missing on inductive loads" -->

## Notes

- 
````

---

## Layout: Diode & LED

Polarised, two-terminal, one-way devices. Everything hinges on **polarity** and
on **forward vs. reverse behaviour**, so those lead. The same layout covers
rectifiers, Schottky, Zener, TVS, and LEDs via a "variants" section and a couple
of type-specific optional rows (a Zener adds `Vz`; an LED adds colour and
luminous intensity).

````markdown
# <Part number>

> One sentence: type and use.

## Overview

<!-- learner + teacher: the one-way-valve model; for a Zener, the "clamps at Vz"
     idea; for an LED, "current through it, light out". -->

## Quick reference

| | |
|---|---|
| **Type** | |
| **Forward voltage** `Vf` | |
| **Max forward current** `If` | |
| **Reverse voltage** `Vr` | |
| **Zener voltage** `Vz` | <!-- Zener only, else delete row --> |

## Polarity

<!-- all readers, learner especially. How to find the cathode: the band,
     the flat, the short leg. This is the #1 thing beginners get wrong. -->

> 💡 The band / flat / shorter leg marks the **cathode** (−).

## Key parameters

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Forward voltage | Vf | | | | V | at If = … |
| Forward current | If | | | | mA | |
| Reverse voltage | Vr | | | | V | |

## Forward & reverse characteristics

<!-- learner + reference: the I–V behaviour each way, and where it breaks down /
     conducts. -->

## Variants

<!-- reference: the family and when to pick each (Schottky for low Vf/fast,
     TVS for transient protection, ...). Delete if a single part. -->

## Typical circuits

```
<!-- Rectification, flyback/freewheeling, indicator with series resistor,
     Zener reference. Pick what applies. -->
```

## Common mistakes

- <!-- "LED with no current-limiting resistor", "diode fitted backwards" -->

## Notes

- 
````

---

## Layout: Passive

Resistors, capacitors, and inductors share one shape: they're defined by a
**value**, a **tolerance**, and a **rating**, and they have **markings you have
to decode**. This single layout parameterises across all three; capacitor- and
inductor-specific fields (polarity, voltage rating, saturation current) are
optional blocks. If you'd rather split them into three pages, this same spine
works for each — the differences are a handful of rows.

````markdown
# <Component / series name>

> One sentence: what it does in a circuit.

## Overview

<!-- learner + teacher: the role (limit current / store charge / oppose current
     change). Keep it to the mental model. -->

## Quick reference

| | |
|---|---|
| **Value / range** | |
| **Tolerance** | |
| **Rating** | <!-- power (W) / voltage (V) / current (A) --> |
| **Type** | |
| **Polarised?** | <!-- capacitors/inductors: yes/no --> |

## Value & markings

<!-- all readers. How to read this part: resistor colour bands, EIA codes,
     3-digit capacitor codes. A decode table is gold for reference users and a
     lifeline for learners. -->

| Marking | Meaning |
|---|---|
| | |

> 💡 <!-- e.g. "3-digit cap code: first two digits + number of zeros, in pF.
       104 = 100000 pF = 100 nF." -->

## Key parameters

| Parameter | Value | Unit | Notes |
|---|---|---|---|
| Tolerance | | % | |
| Power / voltage / current rating | | | |
| Temperature coefficient | | ppm/°C | |
| ESR | | Ω | <!-- capacitors; delete otherwise --> |
| Saturation current | | A | <!-- inductors; delete otherwise --> |

## Types

<!-- reference + learner: the family and trade-offs (carbon vs metal film;
     ceramic vs electrolytic vs film; ...). -->

## Combinations

<!-- learner + teacher: the series/parallel rules — the everyday formulas. -->

- **Series:**
- **Parallel:**

## Typical uses

<!-- teacher + learner: pull-up/-down, decoupling, timing, filtering, ... -->

## Common mistakes

- <!-- "exceeding power/voltage rating", "electrolytic fitted backwards",
       "ignoring inductor saturation" -->

## Notes

- 
````

---

## Layout: Electromechanical

Relays, motors, switches, buzzers, connectors — anything with moving parts or a
physical action. What sets this layout apart is that it carries **mechanical**
specifications alongside electrical ones, and it almost always has a **drive
requirement** (a relay coil or motor can't be driven straight off an MCU pin).
That drive section is warning-flagged because getting it wrong is a classic
board-killer.

````markdown
# <Part name>

> One sentence: what it does mechanically.

## Overview

<!-- learner + teacher: the physical action (a coil pulls a contact / a coil
     spins a shaft) and where you'd use it. -->

## Quick reference

| | |
|---|---|
| **Type** | |
| **Coil / drive voltage** | |
| **Contact / load rating** | |
| **Actuation** | <!-- momentary / latching / continuous --> |

## Terminals & contacts

<!-- all readers. Terminal arrangement — for a relay, COM/NO/NC and the pole
     count (SPDT, DPDT). For a motor, the leads. -->

| Terminal | Function |
|---|---|
| | |

## Electrical specifications

| Parameter | Value | Unit | Notes |
|---|---|---|---|
| Coil voltage | | V | |
| Coil current / resistance | | | |
| Contact rating | | A @ V | |

## Mechanical specifications

<!-- reference: dimensions, mounting, actuation force/travel, shaft/gearing.
     The part of the spec sheet other layouts never need. -->

| Parameter | Value | Unit |
|---|---|---|
| Dimensions | | mm |
| Mounting | | |
| Actuation force / travel | | |

## Drive requirements

> [!WARNING] <!-- The safety-critical part. e.g. "Do not drive the coil directly from an
> MCU pin. Use a transistor and a flyback diode across the coil." -->

<!-- learner + teacher: the interface circuit needed to control it safely. -->

## Wiring

```
<!-- Concrete hookup including the drive circuit above. -->
```

## Lifetime & ratings

<!-- reference: mechanical and electrical life, duty cycle. Omit if trivial. -->

## Common mistakes

- <!-- "driven straight from a GPIO pin", "no flyback diode", "contact rating
       exceeded by inrush current" -->

## Notes

- 
````

---

## Layout: Default

The fallback. When a part doesn't fit any category above — a crystal, a fuse, a
thermistor, an antenna — it still gets a home with the shared spine and open
sections. Keep whatever applies, delete the rest. If you find yourself repeatedly
filling the default layout the same way for a kind of part, that's the signal to
promote it into its own layout.

````markdown
# <Component name>

> One sentence: what it is and what it's for.

## Overview

<!-- learner + teacher: what it does and why. -->

## Quick reference

| | |
|---|---|
| **Type** | |
| **Key spec** | |
| **Rating** | |

## Terminals

<!-- If it has pins/leads/polarity, describe them. Delete if not applicable. -->

## Specifications

| Parameter | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|
| | | | | | |

## Usage

<!-- Typical circuit / wiring / code. -->

## Common mistakes

- 

## Notes & further reading

- 
````

---

## Using these layouts

- **Start from a stub.** A page with frontmatter, a title, and a one-line
  summary is a legitimate, mergeable page. Fill the rest as you learn the part.
  The `status` field (`stub → draft → reviewed → complete`) tells readers how far
  to trust it.
- **Delete freely, reorder rarely.** Dropping a section that doesn't apply keeps
  the page honest. Reordering the shared spine breaks the muscle memory that
  makes the corpus scannable — avoid it.
- **Keep the tables near the top.** If you only enforce one rule, enforce this:
  values that a reference user checks go above prose a learner reads.
- **Promote patterns.** If the default layout keeps growing the same limbs for
  the same kind of part, that part has earned its own layout.

The frontmatter block is deliberately uniform across all seven layouts, which
means the whole corpus stays queryable — you can list every `category: module`
with a `spi` interface, or every page still at `status: stub`, without touching
the page bodies.
