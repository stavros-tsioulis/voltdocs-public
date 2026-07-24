This walkthrough wires an RC522 breakout to an ESP32 over SPI and reads the UID
of a MIFARE Classic card, using ESP-IDF and the register interface directly —
no Arduino framework.

> [!WARNING]
> The MFRC522 runs at 2.5–3.6 V. Several clone boards silkscreen the supply pin
> as "5V"; connecting 5 V there will permanently damage the reader.

## Wiring

The module hardwires the IC to SPI, so only the four bus signals plus reset are
needed. `IRQ` can be left unconnected — the driver below polls instead.

| RC522 | ESP32 (VSPI) | Notes |
|:------|:-------------|:------|
| SDA   | GPIO 5       | Chip select, active low |
| SCK   | GPIO 18      | Up to 10 MHz |
| MOSI  | GPIO 23      | |
| MISO  | GPIO 19      | |
| RST   | GPIO 22      | Held high in normal operation |
| 3.3V  | 3V3          | Never 5 V |
| GND   | GND          | |

## Addressing registers over SPI

The address byte is not the register number. Bit 7 selects the direction and
bits 6–1 carry the address, so a register read is `(addr << 1) | 0x80` and a
write is `(addr << 1) & 0x7E`.

```c
static esp_err_t rc522_write(spi_device_handle_t dev, uint8_t reg, uint8_t val) {
    uint8_t tx[2] = { (uint8_t)((reg << 1) & 0x7E), val };
    spi_transaction_t t = { .length = 16, .tx_buffer = tx };
    return spi_device_polling_transmit(dev, &t);
}

static uint8_t rc522_read(spi_device_handle_t dev, uint8_t reg) {
    uint8_t tx[2] = { (uint8_t)(((reg << 1) & 0x7E) | 0x80), 0x00 };
    uint8_t rx[2] = { 0 };
    spi_transaction_t t = { .length = 16, .tx_buffer = tx, .rx_buffer = rx };
    spi_device_polling_transmit(dev, &t);
    return rx[1];
}
```

## Bringing the reader up

A soft reset settles in roughly 37.74 µs, so poll `CommandReg` rather than
guessing at a delay. The antenna is off after reset and must be enabled
explicitly.

```c
void rc522_init(spi_device_handle_t dev) {
    rc522_write(dev, 0x01, 0x0F);              // CommandReg: SoftReset
    while (rc522_read(dev, 0x01) & 0x10) { }   // wait for the reset to clear

    rc522_write(dev, 0x2A, 0x8D);              // TModeReg
    rc522_write(dev, 0x2B, 0x3E);              // TPrescalerReg
    rc522_write(dev, 0x15, 0x40);              // TxASKReg: force 100 % ASK
    rc522_write(dev, 0x11, 0x3D);              // ModeReg: CRC preset 0x6363

    uint8_t tx = rc522_read(dev, 0x14);        // TxControlReg
    if (!(tx & 0x03)) rc522_write(dev, 0x14, tx | 0x03);  // antenna on
}
```

> Verify the version register (`0x37`) reads `0x91` or `0x92`. A value of `0x00`
> or `0xFF` almost always means the wiring or the chip select is wrong.

## Where to go next

Anticollision and authentication build on the same two primitives. The command
set and the full register map are in the reference documentation for this part.
