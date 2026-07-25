## Overview

The MFRC522 is a highly integrated 13.56 MHz contactless communication card reader/writer IC designed by NXP Semiconductors, most commonly sold on low-cost **RC522** breakout modules. It provides full support for ISO/IEC 14443 A protocol standards and MIFARE card families (including MIFARE Mini, 1K, 4K, Ultralight, and DESFire).

The chip directly drives an onboard PCB loop antenna using high-frequency magnetic field modulation (13.56 MHz) with no external active driver circuitry required. It communicates with nearby passive RFID tags and smart cards via electromagnetic induction, exchanging framed commands and responses.

Host microcontrollers communicate with the module primarily over SPI (up to 10 Mbit/s), though I2C (up to 3.4 Mbit/s) and UART (up to 1228.8 kBd) interface modes are also supported by the underlying silicon. The module features an internal 64-byte FIFO buffer, hardware CRC engine, and programmable interrupt capabilities to offload timing-critical RFID transactions from the host MCU.

> [!NOTE] NXP lists the underlying MFRC522 silicon as *Not Recommended for New Designs*; the suggested replacement family is the CLRC663 Plus (`CLRC66303HN`). However, the low-cost RC522 module remains widely used across educational and maker projects.

## Quick reference

| | |
|---|---|
| **Operating voltage** | 2.5 V – 3.6 V (3.3 V nominal) |
| **Logic level** | 3.3 V (not 5 V tolerant) |
| **Interface** | SPI (default on RC522 module), I2C, UART |
| **Default address** | SPI: Active-low Chip Select (`SDA`/`NSS`); I2C: 0x28 (configurable via `EA`/`D1`–`D7`) |
| **Current draw** | 13 mA – 26 mA (operating), 10 µA (hard power-down) |
| **Key spec** | 13.56 MHz ISO/IEC 14443 A & MIFARE support with ~50 mm read range |

## Pinout

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `SDA` / `NSS` / `CS` | Bus | SPI Chip Select (active low) / I2C Data / UART address input |
| 2 | `SCK` | Clock | SPI Serial Clock input |
| 3 | `MOSI` | Digital I/O | SPI Master Out Slave In data input |
| 4 | `MISO` | Digital I/O | SPI Master In Slave Out data output |
| 5 | `IRQ` | Digital I/O | Interrupt Request output (active low or high, programmable; typically unconnected) |
| 6 | `GND` | Power | Ground (0 V) reference |
| 7 | `RST` | Digital I/O | Reset and Power-Down input (active low; pull high for normal operation) |
| 8 | `3.3V` | Power | Power supply input (2.5 V to 3.6 V DC) |

> [!TIP] For direct IC integration in HVQFN32 package, pins 25–31 are multiplexed between SPI, I2C, and UART modes depending on the `I2C` and `EA` logic levels latched at reset.

## Specifications

| Parameter | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|
| Supply voltage (`VCC`) | 2.5 | 3.3 | 3.6 | V | Normal operation |
| Operating current | 13 | 20 | 26 | mA | RF field active, 13.56 MHz |
| Idle current | 10 | 13 | 15 | mA | CommandReg = Idle mode |
| Hard power-down current | — | 1.0 | 5.0 | µA | `NRSTPD` = 0 V |
| Soft power-down current | — | 10.0 | — | µA | `PowerDown` bit set in `CommandReg` |
| Carrier frequency | — | 13.56 | — | MHz | Crystal frequency = 27.12 MHz |
| SPI clock frequency | 0 | — | 10 | Mbit/s | SPI mode |
| Operating temperature | −25 | +25 | +85 | °C | Ambient temperature |
| Read distance | 0 | 50 | 80 | mm | Dependent on antenna geometry & card tuning |

## Communication

- **Protocol:** SPI Mode 0 (CPOL = 0, CPHA = 0), MSB first. Also supports I2C (up to 3.4 Mbit/s) and UART (up to 1228.8 kBd) when enabled on the IC.
- **Max clock:** 10 Mbit/s (SPI).
- **Frame format:** Each SPI transfer consists of an address byte followed by one or more data bytes:
  - **Address byte format:**
    - Bit 7 (MSB): Read / Write flag (`1` = Read, `0` = Write).
    - Bits 6:1: Register address (6-bit offset `0x00`–`0x3F`).
    - Bit 0 (LSB): Reserved, must always be `0`.
  - **SPI Write framing:** `(Address << 1) & 0x7E` followed by data byte(s).
  - **SPI Read framing:** `(Address << 1) | 0x80` followed by clocking dummy bytes to read response byte(s).

## Register map

| Address | Register | Access | Reset | Description |
|---|---|---|---|---|
| `0x01` | `CommandReg` | R/W | `0x20` | Starts/stops command execution and soft power-down |
| `0x02` | `ComIEnReg` | R/W | `0x80` | Interrupt enable control bits for communication events |
| `0x04` | `ComIrqReg` | R/W | `0x14` | Communication interrupt request flags |
| `0x06` | `ErrorReg` | R | `0x00` | Error status flags for last executed command |
| `0x07` | `Status1Reg` | R | `0x21` | CRC and FIFO status flags |
| `0x08` | `Status2Reg` | R/W | `0x00` | Receiver and crypto (MIFARE) status flags |
| `0x09` | `FIFODataReg` | R/W | `0x00` | 64-byte FIFO buffer input/output port |
| `0x0A` | `FIFOLevelReg` | R/W | `0x00` | Number of bytes currently stored in FIFO |
| `0x0D` | `BitFramingReg` | R/W | `0x00` | Bit-oriented frame adjustment (last bits transmission) |
| `0x0E` | `CollReg` | R/W | `0x80` | Bit position of first detected collision |
| `0x11` | `ModeReg` | R/W | `0x3B` | General mode control (CRC preset, polarity) |
| `0x12` | `TxModeReg` | R/W | `0x00` | Transmitter speed and framing settings |
| `0x13` | `RxModeReg` | R/W | `0x00` | Receiver speed and framing settings |
| `0x14` | `TxControlReg` | R/W | `0x80` | Controls RF output drivers TX1 and TX2 |
| `0x15` | `TxASKReg` | R/W | `0x00` | Forces 100% ASK modulation |
| `0x26` | `RFCfgReg` | R/W | `0x48` | Configures receiver gain (`RxGain`) |
| `0x2A` | `TModeReg` | R/W | `0x00` | Timer prescaler upper bits and auto-timer control |
| `0x2B` | `TPrescalerReg` | R/W | `0x00` | Timer prescaler lower bits |
| `0x2C` | `TReloadRegH` | R/W | `0x00` | Timer reload value (High byte) |
| `0x2D` | `TReloadRegL` | R/W | `0x00` | Timer reload value (Low byte) |
| `0x37` | `VersionReg` | R | `0x91`/`0x92` | Silicon version identifier (`0x91` = v1.0, `0x92` = v2.0) |

### `0x01` — `CommandReg`

| Bit(s) | Field | Access | Reset | Description |
|---|---|---|---|---|
| 7 | Reserved | R | 0 | Reserved |
| 6 | `PowerDown` | R/W | 0 | Soft power-down mode (1 = powered down, oscillator off) |
| 5 | `RcvOff` | R/W | 1 | Analog receiver status (1 = receiver off) |
| 3:0 | `Command` | R/W | 0000 | Command code (`0x00`: Idle, `0x01`: Mem, `0x02`: Generate RandomID, `0x03`: CalcCRC, `0x04`: Transmit, `0x0C`: Transceive, `0x0E`: MFAuthent, `0x0F`: SoftReset) |

### `0x14` — `TxControlReg`

| Bit(s) | Field | Access | Reset | Description |
|---|---|---|---|---|
| 7:2 | Reserved | R/W | 100000 | Reserved |
| 1 | `Tx2RFEn` | R/W | 0 | Enables TX2 antenna output driver (1 = 13.56 MHz carrier on) |
| 0 | `Tx1RFEn` | R/W | 0 | Enables TX1 antenna output driver (1 = 13.56 MHz carrier on) |

### `0x26` — `RFCfgReg`

| Bit(s) | Field | Access | Reset | Description |
|---|---|---|---|---|
| 7 | Reserved | R/W | 0 | Reserved |
| 6:4 | `RxGain` | R/W | 100 | Receiver gain factor (`011`: 33 dB, `100`: 38 dB default, `110`: 43 dB, `111`: 48 dB max) |
| 3:0 | Reserved | R/W | 1000 | Reserved |

### `0x37` — `VersionReg`

| Bit(s) | Field | Access | Reset | Description |
|---|---|---|---|---|
| 7:4 | `ChipType` | R | 1001 | Always `0x9` for MFRC522 family |
| 3:0 | `Version` | R | 0001 / 0010 | Silicon revision (`0x1` = v1.0 [`0x91`], `0x2` = v2.0 [`0x92`]) |

## Wiring

| Module (RC522) | → | MCU (e.g. Arduino Uno) | Notes |
|---|---|---|---|
| `3.3V` | | `3.3V` | **Never connect to 5V power supply!** |
| `RST` | | `D9` | Configurable reset pin |
| `GND` | | `GND` | Common ground |
| `IRQ` | | — | Unconnected (optional interrupt pin) |
| `MISO` | | `D12` | SPI Master In Slave Out |
| `MOSI` | | `D11` | SPI Master Out Slave In (via level shifter if 5V MCU) |
| `SCK` | | `D13` | SPI Serial Clock (via level shifter if 5V MCU) |
| `SDA` (`SS`) | | `D10` | SPI Chip Select (via level shifter if 5V MCU) |

> [!WARNING] **Not 5 V tolerant!** The MFRC522 operates strictly at 3.3 V logic. When connecting to 5 V microcontrollers (such as Arduino Uno or Nano), use active logic level shifters or resistor voltage dividers (e.g. 1 kΩ / 2 kΩ) on `SCK`, `MOSI`, `SDA`, and `RST` lines. The `MISO` output line can be connected directly to 5 V MCUs because 3.3 V high logic meets the 5 V MCU threshold.

## Example

```cpp
#include <SPI.h>
#include <MFRC522.h>

#define RST_PIN  9
#define SS_PIN   10

MFRC522 mfrc522(SS_PIN, RST_PIN); // Create MFRC522 instance

void setup() {
  Serial.begin(9600);
  while (!Serial);
  
  SPI.begin();           // Init SPI bus
  mfrc522.PCD_Init();    // Init MFRC522 reader
  
  // Verify SPI communication by reading VersionReg
  byte v = mfrc522.PCD_ReadRegister(mfrc522.VersionReg);
  Serial.print(F("MFRC522 Version: 0x"));
  Serial.println(v, HEX);
}

void loop() {
  // Look for new RFID card
  if (!mfrc522.PICC_IsNewCardPresent()) return;
  
  // Select one of the cards
  if (!mfrc522.PICC_ReadCardSerial()) return;
  
  // Print UID to Serial Monitor
  Serial.print(F("Card UID:"));
  for (byte i = 0; i < mfrc522.uid.size; i++) {
    Serial.print(mfrc522.uid.uidByte[i] < 0x10 ? " 0" : " ");
    Serial.print(mfrc522.uid.uidByte[i], HEX);
  }
  Serial.println();
  
  // Halt PICC and stop crypto on PCD
  mfrc522.PICC_HaltA();
  mfrc522.PCD_StopCrypto1();
}
```

## Common mistakes

- **If reader fails to initialize (`VersionReg` returns `0x00` or `0xFF`):** Check wiring, especially `3.3V` power and `GND`. Verify SPI pin assignments (`MOSI`, `MISO`, `SCK`, `CS`) and ensure power supply voltage is stable.
- **If module dies or behaves erratically after connecting to Arduino Uno:** Check logic levels. Direct 5 V GPIO signals on `SCK`, `MOSI`, `SDA`, or `RST` can degrade or burn out the MFRC522 inputs. Add level shifters.
- **If card detection range is short (< 10 mm) or intermittent:** Check antenna tuning and receiver gain. Verify `RFCfgReg` (`RxGain`) is set to `0x48` (38 dB) or `0x70` (48 dB), and ensure no metal objects or noise sources are near the PCB antenna.
- **If SPI bus conflicts occur when using multiple devices:** Check MISO output. Some cheap RC522 clone modules fail to properly tri-state `MISO` when `SDA`/`CS` is high. Add a tri-state buffer or dedicated SPI bus.
- **If MIFARE read/write operations fail after card detection:** Check authentication sequence. MIFARE Classic cards require executing `PCD_Authenticate` with Key A or Key B (default `0xFF 0xFF 0xFF 0xFF 0xFF 0xFF`) before accessing data blocks.

## Notes

- **Silicon Revisions:** Revision 1.0 (`MFRC52201HN1`, returns `0x91` in `VersionReg`) vs Revision 2.0 (`MFRC52202HN1`, returns `0x92` in `VersionReg`). Revision 2.0 improves RF receiver stability and fixes CRC calculation when `RxMultiple` is set.
- **NRND Notice:** NXP lists MFRC522 as *Not Recommended for New Designs*. For new commercial designs, NXP recommends the CLRC663 Plus family (`CLRC66303HN`).

