# VoltDocs Pinout Specification

Version: **1** (`"version": 1`)

This document specifies the JSON file an entry uses to describe a component's
pins: what each pin does, how the pins are arranged on the package, and how they
wire to common host boards. A renderer uses it to draw an interactive pinout;
an indexer may use it to make pins searchable.

It extends the [repository specification](./SPEC.md); everything not stated here
(path resolution, revisions, validation posture) follows that document.

---

## 1. Where pinouts live

A pinout is a JSON file inside the entry folder, declared from `entry.yaml`:

```yaml
pinouts:
  - id: module                    # unique within the entry
    title: Module header          # optional; shown when an entry has several
    path: pinouts/module.json     # required; resolved like a `repo` asset path
```

```
rc522-module/
├── entry.yaml
├── index.md
└── pinouts/
    ├── module.json
    └── module-art.svg            # optional board artwork (§3.3)
```

- An entry may declare **several** pinouts — one per physical form it documents
  (a module's header and its bare IC, or DIP-8 and SOIC-8 packages when they
  differ). The **first** is the default.
- Paths resolve exactly like `repo` asset paths (SPEC §3): entry-relative by
  default, `/`-prefixed for repo-root-relative, and rejected if they escape the
  repository.
- Pinouts are part of the revision they sit in. A historical revision under
  `revisions/<id>/` carries its own `pinouts:` and files (SPEC §4.1).

### 1.1 Placing a pinout in the body

A pinout is drawn where the entry's body (or one of its guides) places it,
with a fenced block whose language is `pinout` and whose content is the
pinout's `id`. An empty block places the default pinout:

````markdown
## Module pinout

```pinout
module
```
````

Anywhere plain Markdown is shown, the block still reads as a labelled
reference. Only **top-level** blocks are placed; one nested in a list or
blockquote stays an ordinary code block. A block naming an unknown id is
dropped. Pinouts the body never places are rendered in a section of their own
after it; a guide renders only the pinouts it places.

---

## 2. The file at a glance

A pinout has four parts, each answering one question:

| Key | Answers | Required |
|---|---|---|
| `pins` | What does each pin do? | yes |
| `layout` | Where is each pin on the package? | yes |
| `wiring` | Where does each pin go on a host board? | no |
| `version` | Which version of this format is it? | yes |

Meaning (`pins`) is kept apart from placement (`layout`) on purpose. The same
electrical pins can be drawn in more than one arrangement, pins can exist
without being drawn (an exposed pad), and a layout can contain positions that
have no pin (a gap in a header). Neither could be expressed if position were a
property of the pin.

A complete example, the RC522 module from the design harness:

```json
{
  "$schema": "https://voltdocs.dev/schemas/pinout-1.json",
  "version": 1,
  "pins": [
    {
      "id": "1",
      "name": "SDA / NSS / CS",
      "type": "bus",
      "direction": "bidirectional",
      "level": "3.3 V logic",
      "voltage": { "max": 3.6 },
      "functions": ["I2C SDA", "UART address"],
      "description": "SPI chip select, active low. Doubles as the I2C data line and the UART address input, depending on the interface latched at reset.",
      "notes": [
        { "severity": "danger", "text": "Driven directly from a 5 V GPIO this input can degrade. Use a level shifter or a 1 kΩ / 2 kΩ divider." }
      ]
    },
    { "id": "2", "name": "SCK", "type": "clock", "direction": "input", "level": "3.3 V logic", "description": "SPI serial clock input, up to 10 Mbit/s." },
    { "id": "3", "name": "MOSI", "type": "digital", "direction": "input", "level": "3.3 V logic", "description": "SPI data from the host." },
    { "id": "4", "name": "MISO", "type": "digital", "direction": "output", "drive": "tri-state", "level": "3.3 V logic", "description": "SPI data to the host." },
    { "id": "5", "name": "IRQ", "type": "digital", "direction": "output", "drive": "open-drain", "description": "Interrupt request output." },
    { "id": "6", "name": "GND", "type": "ground", "description": "Ground reference." },
    { "id": "7", "name": "RST", "type": "digital", "direction": "input", "level": "3.3 V logic", "description": "Reset and power-down, active low." },
    {
      "id": "8",
      "name": "3.3V",
      "type": "power",
      "direction": "power-in",
      "voltage": { "min": 2.5, "nominal": 3.3, "max": 3.6 },
      "description": "Supply input.",
      "notes": [{ "severity": "danger", "text": "Never connect to a 5 V supply — it destroys the IC." }]
    }
  ],
  "layout": {
    "package": "module",
    "sides": {
      "left": ["1", "2", "3", "4", "5", "6", "7", "8"]
    },
    "minSize": { "width": 6 },
    "art": { "path": "module-art.svg" }
  },
  "wiring": [
    {
      "id": "arduino-uno",
      "label": "Arduino Uno",
      "targetId": "board.arduino.uno",
      "pins": { "1": "D10", "2": "D13", "3": "D11", "4": "D12", "6": "GND", "7": "D9", "8": "3.3V" }
    }
  ]
}
```

---

## 3. Schema

The normative shape, in TypeScript notation (`?` marks an optional key):

```ts
interface Pinout {
  $schema?: string;               // editor hint only; never fetched
  version: 1;
  pins: Pin[];
  layout: Layout;
  wiring?: Wiring[];
}
```

### 3.1 `pins`

```ts
interface Pin {
  id: string;                     // the pin's designator: "1", "A7", "EP"
  name: string;                   // primary signal name
  type: PinType;
  direction?: Direction;
  drive?: Drive;                  // only meaningful for outputs
  level?: string;                 // human-readable signal level, e.g. "3.3 V logic"
  voltage?: { min?: number; nominal?: number; max?: number };  // volts
  functions?: string[];           // alternate functions, in priority order
  description?: string;           // inline Markdown
  notes?: Note[];
}

type PinType =
  | 'power' | 'ground'            // supply rails
  | 'digital' | 'analog'          // general-purpose signals
  | 'bus'                         // a data or select line of SPI, I2C, UART, …
  | 'clock'                       // a clock line, including a bus clock
  | 'nc'                          // not connected
  | 'other';

type Direction = 'input' | 'output' | 'bidirectional' | 'passive' | 'power-in' | 'power-out';
type Drive = 'push-pull' | 'open-drain' | 'open-collector' | 'tri-state';

interface Note {
  severity: 'danger' | 'warning' | 'info';
  text: string;                   // inline Markdown
}
```

- **`id`** is a string, not a number, so a single scheme covers header positions
  (`"1"`), ball grids (`"A7"`) and special pads (`"EP"`, `"MH1"`). It is
  unique within the file and is what `layout` and `wiring` refer to. It is
  also the label printed on the pad.
- **Order matters.** The order of `pins` is the order a renderer lists and steps
  through them. Author them in designator order.
- **`type`** chooses the colour group and the filter. It describes the pin's
  *primary* role; a GPIO that can also be an ADC input is `digital`, with
  `"ADC1_4"` among its `functions`. A pin that is both a bus line and a clock
  (SPI `SCK`) is `clock`.
- **`direction`/`drive`** follow the electrical pin types EDA tools use, so a
  pinout can be generated from a schematic symbol. `drive` is ignored unless
  `direction` is `output` or `bidirectional`.
- **`level` vs `voltage`.** `level` is what a reader sees; `voltage` is for
  machines (filtering "5 V tolerant", or checking wiring). Both are optional
  and they don't need to match word for word. `voltage.max` is the highest
  voltage the pin tolerates in operation, not the absolute maximum rating.
- **`notes`** carry cautions and tips. `danger` is for mistakes that damage
  hardware, `warning` for ones that cause malfunction, `info` for helpful
  context. A renderer shows them in the order given.

### 3.2 `layout`

```ts
interface Layout {
  package: 'module' | 'ic';
  sides: {
    left?: (string | null)[];
    right?: (string | null)[];
    top?: (string | null)[];
    bottom?: (string | null)[];
  };
  label?: string;                 // marking printed at the centre of the body
  minSize?: { width?: number; height?: number };  // in pitches
  art?: { path: string };         // board artwork, SVG (§3.3)
}
```

- **`package`** picks the drawing. `module` is a breakout PCB with pads on
  header strips inside the board edge; `ic` is a bare package body with pads
  as legs outside it.
- **`sides`** place pins, by `id`, on each edge of the body. **Each array is
  in visual reading order**: top→bottom for `left`/`right`, left→right for
  `top`/`bottom`, as seen from above with the package unrotated. This is
  *not* the counter-clockwise order in which ICs are numbered. A DIP-8 is:

  ```json
  "sides": { "left": ["1", "2", "3", "4"], "right": ["8", "7", "6", "5"] }
  ```

  and a QFP runs its `right` and `top` sides in descending order. Visual order
  keeps the renderer simple and makes the file read like the drawing. The
  numbering direction is a fact of the part, not of this format, so the file
  doesn't encode it.
- **`null`** is an empty position: the renderer keeps the pitch but draws no
  pad. Use it for missing header pins, or to line up two headers of different
  lengths.
- Pins that appear in no side are **unplaced**. They are still listed and
  described, just not drawn. That's the right treatment for an exposed thermal
  pad, mounting holes, or pins on the underside.
- **`minSize`** is a lower bound on the body's *interior*, measured in
  **pitches** (the spacing between adjacent pins). Using pitches instead of
  pixels keeps a layout correct however the renderer scales its drawing. The
  body always grows to fit its pins, so `minSize` is only needed to make it
  larger than that: to give a board realistic proportions or room for its
  artwork.
- Layout says nothing about pixel sizes, colours or label placement. Those are
  up to the renderer, which MUST keep labels from overlapping each other or the
  body.

### 3.3 Board artwork — `layout.art`

`art.path` points to an SVG file, resolved relative to the pinout file. It is
drawn scaled to fit the body's interior, and is decoration only; it never
carries pins.

The artwork is drawn inline so it can follow the site theme, so **a renderer
MUST sanitise it** before inlining. Sanitising should keep an allowlist of plain
drawing elements and presentation attributes, rather than try to block known
threats. At minimum it removes:

- `<script>`, `<foreignObject>`, animation elements and event-handler attributes
- `<style>`, whose rules would apply to the whole page, not just the drawing
- any `href` or `url()` that is not a same-document fragment

It should also prefix ids, so two drawings on one page can't resolve each
other's gradients or clip paths. Artwork may colour itself with these CSS
custom properties, which the renderer defines for both light and dark themes:

| Property | Use |
|---|---|
| `--pinout-trace` | copper traces, antenna coils |
| `--pinout-edge` | component outlines |
| `--pinout-ic` | IC and module bodies |
| `--pinout-crystal` | secondary components |
| `--pinout-marking` | silkscreen text |

### 3.4 `wiring`

```ts
interface Wiring {
  id: string;                     // unique within the file
  label: string;                  // host name, e.g. "Arduino Uno"
  targetId?: string;              // the host board's entry id, if it has one
  pins: Record<string, string>;   // pin id → host pin label
}
```

- Each entry in `wiring` is one host board the part is commonly wired to. A
  renderer shows a pin's host label in place of its type while that host is
  selected, and lets the reader switch between hosts.
- `pins` may be partial; a pin left out (IRQ above) has no connection to that
  host.
- **`targetId`** links the host to its own entry, the same way `references`
  link entries (SPEC §4.2). A renderer MAY link to it.

---

## 4. Validation

Pinouts are validated defensively, like entry manifests. A problem that
affects part of the file drops only that part.

| Check | On failure |
|---|---|
| `version` is `1` | The file is rejected. Unknown versions are not guessed at. |
| `pins` is non-empty and every `id` is unique | The file is rejected. |
| Every `type` and `direction` is a known value | The value is treated as `other` or omitted, with a warning. |
| Every id in `layout.sides` exists in `pins` | The position is treated as `null`, with a warning. |
| Each pin is placed at most once | Later placements become `null`, with a warning. |
| Every key in `wiring[].pins` exists in `pins` | The mapping is dropped, with a warning. |
| `layout.art.path` resolves to an SVG | The artwork is omitted, with a warning. |
| Unknown keys | Ignored, so later minor additions don't break older readers. |

---

## 5. Out of scope for version 1

Called out so they are not designed out:

- **Grid packages (BGA, LGA).** These would be a `"package": "grid"` layout
  that places ids at row/column coordinates. The string `id` (`"A7"`) already
  supports this.
- **Pin-compatible variants.** Several entries sharing one pinout file through
  a repo-root path (`/pinouts/…`) works today. A dedicated sharing mechanism
  would come later, if needed.
- **Localisation.** `name` stays untranslated. `description` and `notes` would
  take the same per-locale approach as entry bodies (SPEC §4.2).
- **Pin search.** An indexer MAY index `name` and `functions` (to answer
  "which parts expose SDA?"). Nothing in the format is required for that.

---

## 6. Conformance checklist

A pinout conforms to version 1 when:

1. It is a JSON object with `"version": 1`, and is declared from an entry's
   `pinouts:` list at a path inside the repository.
2. `pins` is a non-empty array of unique `id`s, each with a `name` and a known
   `type`.
3. Every id in `layout.sides` names a pin, and no pin is placed twice.
4. Every key in each `wiring[].pins` names a pin.
5. `layout.art`, if present, points to an SVG inside the repository.
