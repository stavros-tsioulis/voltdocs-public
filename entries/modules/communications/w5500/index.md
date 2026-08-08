## Overview

The **W5500** is a hardwired TCP/IP embedded Ethernet controller manufactured by WIZnet. Communicating over an 80 MHz high-speed SPI bus, it offloads full network protocol processing (TCP, UDP, IPv4, ICMP, ARP, IGMP, and PPPoE) into dedicated silicon hardware.

Unlike MAC/PHY-only controllers (like the ENC28J60) that require microcontrollers to run software TCP/IP stacks in MCU RAM, the W5500 incorporates **8 independent hardware sockets** and a **32 KB internal TX/RX packet buffer**. It allows resource-constrained microcontrollers (such as Arduino, ESP32, STM32, and RP2040) to maintain stable 100BASE-TX Ethernet connectivity with minimal MCU overhead.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (module includes 3.3V LDO regulator) |
| **IC supply voltage (`VDD`)** | 2.97 V to 3.63 V DC (3.3 V nominal) |
| **Ethernet standard** | 10Base-T / 100Base-TX (Auto-negotiation half/full duplex) |
| **Hardware TCP/IP stack** | TCP, UDP, ICMP, IPv4, ARP, IGMP, PPPoE |
| **Hardware sockets** | 8 independent simultaneous sockets |
| **Internal buffer memory** | 32 KB internal SRAM (allocated across 8 sockets) |
| **Interface** | High-Speed SPI (up to 80 MHz, SPI Mode 0 & Mode 3) |
| **I/O tolerance** | 5V tolerant SPI pins (`CS`, `SCLK`, `MOSI`, `MISO`) |

## Pinout

Standard 10-pin 0.1" (2.54 mm) breakout module header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` / `3V3` | Power | Supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `MISO` / `SO` | Digital Output | SPI Master Input Slave Output |
| 4 | `MOSI` / `SI` | Digital Input | SPI Master Output Slave Input |
| 5 | `SCLK` / `CLK` | Digital Input | SPI Serial Clock Input (up to 80 MHz) |
| 6 | `SCS` / `CS`  | Digital Input | Active-Low SPI Chip Select |
| 7 | `RST` / `RSTn` | Digital Input | Active-Low hardware reset pin |
| 8 | `INT` / `INTn` | Digital Output | Active-Low interrupt output (triggers on socket events) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with LDO |
| Transmit Current | $I_{tx}$ | — | 132 | 160 | mA | 100BASE-TX active transmission |
| Standby Current | $I_{sb}$ | — | 13 | 20 | mA | Power-down mode |
| SPI Clock Speed | $f_{SPI}$ | 0 | 33 | 80 | MHz | Fast SPI bus operation |
| Auto-Negotiation | — | 10/100 | — | — | Mbps | 10Base-T / 100Base-TX |
| Operating Temperature | $T_{opr}$ | -40 | — | 85 | °C | Industrial temperature rating |

## Hardware Sockets & Buffer Allocation

The 32 KB internal SRAM is shared dynamically between the 8 hardware sockets (Sockets 0 through 7). Each socket can be configured with **1 KB, 2 KB, 4 KB, 8 KB, or 16 KB** buffer sizes for TX and RX:

- **Default Assignment:** 2 KB TX + 2 KB RX per socket across all 8 sockets ($8 \times 4\text{ KB} = 32\text{ KB}$).
- **High-Throughput Single Socket Assignment:** 16 KB TX + 16 KB RX for Socket 0 ($32\text{ KB}$ dedicated to a single socket for maximum throughput).

## Wiring

| W5500 Pin | → | Arduino Uno | ESP32 | Raspberry Pi Pico | Notes |
|---|---|---|---|---|---|
| `VCC` | | 5V / 3.3V | 3.3V | 3.3V | Connect to 3.3V rail |
| `GND` | | GND | GND | GND | Shared ground |
| `SCLK`| | Digital D13 | GPIO 18 | GP18 (SPI0 SCK) | SPI Clock |
| `MISO`| | Digital D12 | GPIO 19 | GP16 (SPI0 RX) | SPI MISO |
| `MOSI`| | Digital D11 | GPIO 23 | GP19 (SPI0 TX) | SPI MOSI |
| `SCS` | | Digital D10 | GPIO 5 | GP17 (SPI0 CS) | Active-Low CS |
| `RST` | | Digital D9 | GPIO 16 | GP20 | Hardware Reset |

## Example (Arduino Official `Ethernet.h` Library)

```cpp
#include <SPI.h>
#include <Ethernet.h>

// MAC address for controller
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };

EthernetServer server(80);

void setup() {
  Serial.begin(115200);
  while (!Serial);

  // Initialize W5500 Chip Select pin (Digital D10)
  Ethernet.init(10);

  Serial.println("Connecting to network via DHCP...");
  if (Ethernet.begin(mac) == 0) {
    Serial.println("Failed to configure Ethernet using DHCP");
    while (1);
  }

  server.begin();
  Serial.print("W5500 Web Server online at IP: ");
  Serial.println(Ethernet.localIP());
}

void loop() {
  EthernetClient client = server.available();
  if (client) {
    Serial.println("New client connected");
    boolean currentLineIsBlank = true;

    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        if (c == '\n' && currentLineIsBlank) {
          // Send HTTP 200 OK header
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println("Connection: close");
          client.println();
          client.println("<!DOCTYPE HTML><html><h1>VoltDocs W5500 Ethernet Online!</h1></html>");
          break;
        }
        if (c == '\n') currentLineIsBlank = true;
        else if (c != '\r') currentLineIsBlank = false;
      }
    }
    delay(1);
    client.stop();
  }
}
```

## Common mistakes

- **Using slow SPI speeds:** W5500 supports up to 80 MHz SPI. Running SPI at slow default speeds (1 MHz) bottlenecks network throughput. Set SPI clock to 14–33 MHz on microcontrollers.
- **Forgetting hardware reset line:** If `RST` is left floating, spurious noise on power-up can lock the W5500 internal state machine. Connect `RST` to a digital GPIO pin or pull High to 3.3V with a $10\text{ k}\Omega$ resistor.

## Notes

- **W5500 vs W5100 vs ENC28J60:** W5500 features 8 sockets, 32KB RAM, 80MHz SPI, and 100Mbps speed; W5100 has 4 sockets, 16KB RAM, and slower SPI; ENC28J60 has no hardware TCP/IP stack.
