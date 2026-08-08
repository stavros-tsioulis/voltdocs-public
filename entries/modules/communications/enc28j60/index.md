## Overview

The **ENC28J60** is a standalone 10BASE-T Ethernet controller manufactured by Microchip Technology. Packaged as a 28-pin IC or a compact PCB breakout module equipped with an integrated HR911105A RJ45 MagJack connector (with internal isolation magnetics and status LEDs), it enables microcontrollers to connect to wired LAN networks over an SPI interface.

Integrating a fully compliant IEEE 802.3 MAC (Media Access Control) layer, 10 Mbps physical layer transceiver (PHY), programmable hardware packet filtering, and an 8 KB dual-port RAM transmit/receive buffer, the ENC28J60 is a classic hardware solution for adding wired Ethernet connectivity to Arduino Uno, ESP32, STM32, and Raspberry Pi Zero projects.

## Quick reference

| | |
|---|---|
| **Operating voltage (`VCC`)** | 3.3 V to 5.0 V DC (breakout module with 3.3V LDO) |
| **IC supply voltage (`VDD`)** | 3.1 V to 3.6 V DC (3.3 V nominal) |
| **Ethernet standard** | IEEE 802.3 10BASE-T (10 Mbps half/full duplex) |
| **Interface** | SPI (up to 20 MHz) |
| **Internal packet buffer** | 8 KB dual-port SRAM (transmit and receive FIFO) |
| **I/O tolerance** | 5V tolerant SPI inputs (`CS`, `SCK`, `SI`) |
| **Connector** | RJ45 MagJack with built-in isolation transformer & status LEDs |
| **Operating current** | $160\text{ mA}$ typical transmit / $2\ \mu\text{A}$ standby |

## Pinout

Standard 10-pin or 12-pin double-row 0.1" (2.54 mm) breakout module header:

| Pin | Name | Type | Description |
|---|---|---|---|
| 1 | `VCC` / `3.3V` | Power | Power supply input (+3.3 V to +5.0 V DC) |
| 2 | `GND` | Power | Ground reference (0 V) |
| 3 | `CS` / `SS` | Digital Input | Active-Low SPI Chip Select |
| 4 | `SCK` / `CLK` | Digital Input | SPI Serial Clock |
| 5 | `SI` / `MOSI` | Digital Input | SPI Serial Data Input |
| 6 | `SO` / `MISO` | Digital Output | SPI Serial Data Output |
| 7 | `WOL` | Digital Output | Wake-On-LAN signal output (optional) |
| 8 | `INT` | Digital Output | Active-Low interrupt output pin |
| 9 | `RST` / `RESET`| Digital Input | Active-Low hardware reset pin |
| 10 | `CLKOUT` | Digital Output | Programmable clock output pin (default 6.25 MHz) |

## Specifications

| Parameter | Symbol | Min | Typ | Max | Unit | Conditions |
|---|---|---|---|---|---|---|
| Supply Voltage (Module) | $V_{CC}$ | 3.3 | 3.3 / 5.0 | 5.5 | V | Power rail with 3.3V LDO |
| Transmit Current | $I_{tx}$ | — | 160 | 180 | mA | 10BASE-T active transmission |
| Receive Current | $I_{rx}$ | — | 120 | 140 | mA | Receiving Ethernet packets |
| SPI Clock Frequency | $f_{SPI}$ | 0 | 14 | 20 | MHz | SPI Mode 0,0 ($CPOL=0, CPHA=0$) |
| SRAM Buffer Memory | $RAM$ | — | 8192 | — | Bytes | Configurable Rx/Tx buffer split |
| Transmission Speed | $Speed$ | — | 10 | — | Mbps | 10BASE-T Ethernet |

## Software Architecture & Software TCP/IP Stack

Unlike the WIZnet W5500 (which features a hardware-implemented TCP/IP stack on chip), the ENC28J60 handles only Layer 1 (PHY) and Layer 2 (MAC) Ethernet frames in hardware:

- **Ethernet Packet Buffering:** Incoming Ethernet frames are stored in the 8 KB internal SRAM buffer.
- **Software TCP/IP Stack:** The host microcontroller (Arduino/ESP32) must run a software TCP/IP stack—such as **UIP**, **EtherCard**, or **EthernetENC**—to process IP, ARP, ICMP (ping), UDP, and TCP packets.

## Wiring

| ENC28J60 Pin | → | Arduino Uno | ESP32 | Notes |
|---|---|---|---|---|
| `VCC` / `3.3V`| | 3.3V / 5V | 3.3V | **Requires up to 180 mA current** |
| `GND` | | GND | GND | System ground |
| `SCK` | | Digital D13 | GPIO 18 | SPI Clock |
| `SO` (MISO) | | Digital D12 | GPIO 19 | SPI MISO |
| `SI` (MOSI) | | Digital D11 | GPIO 23 | SPI MOSI |
| `CS`  | | Digital D10 | GPIO 5 | SPI Chip Select |
| `RESET` | | Digital D8 | GPIO 16 | Hardware Reset (optional) |

> [!WARNING]
> High Current Supply Hazard:
> - The ENC28J60 draws up to **180 mA** during Ethernet frame transmission. Connecting `VCC` to weak 3.3V regulator pins (such as the 3.3V pin on old FTDI USB-to-serial adapters or early Arduino boards) causes voltage dips and connection resets. Always connect to a high-current 3.3V rail capable of $\ge 250\text{ mA}$.

## Example (Arduino `EthernetENC` Web Server)

```cpp
#include <SPI.h>
#include <EthernetENC.h>

// MAC address for controller
byte mac[] = { 0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED };
IPAddress ip(192, 168, 1, 177);

EthernetServer server(80);

void setup() {
  Serial.begin(9600);
  
  // Initialize Ethernet with Chip Select pin 10
  Ethernet.init(10);
  Ethernet.begin(mac, ip);

  server.begin();
  Serial.print("ENC28J60 Web Server online at IP: ");
  Serial.println(Ethernet.localIP());
}

void loop() {
  EthernetClient client = server.available();
  if (client) {
    Serial.println("New HTTP client connected");
    boolean currentLineIsBlank = true;

    while (client.connected()) {
      if (client.available()) {
        char c = client.read();
        if (c == '\n' && currentLineIsBlank) {
          // Send HTTP response header
          client.println("HTTP/1.1 200 OK");
          client.println("Content-Type: text/html");
          client.println("Connection: close");
          client.println();
          client.println("<!DOCTYPE HTML>");
          client.println("<html><h1>VoltDocs ENC28J60 Ethernet Server</h1></html>");
          break;
        }
        if (c == '\n') {
          currentLineIsBlank = true;
        } else if (c != '\r') {
          currentLineIsBlank = false;
        }
      }
    }
    delay(1);
    client.stop();
  }
}
```

## Common mistakes

- **Powering from weak 3.3V sources:** Under-powering the module causes network dropouts or inability to establish a link with network switches.
- **Conflating ENC28J60 and W5500 libraries:** ENC28J60 requires libraries like `EthernetENC` or `EtherCard`; standard W5500 `Ethernet.h` libraries will fail to initialize the chip.

## Notes

- **ENC28J60 vs W5500:** ENC28J60 is 10 Mbps and requires a software TCP/IP stack; W5500 is 100 Mbps and implements a full hardware TCP/IP stack offloading MCU RAM.
