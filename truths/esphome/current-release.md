---
project: esphome
topic: current-release
valid_from: 2026-09-16
review_by: 2026-09-23
source: https://esphome.io/blog/2026/08/19/esphome-2026-8/
owner: @liam
auto_updated_by: sync-truths
---

# esphome: current-release

Facts only. Each fact is something a skill may state as true until `review_by`.

**This file is about to go stale.** ESPHome's 2026 releases have landed on the third Wednesday of each month, which for September 2026 is the 16th, today. As of the source read on 2026-09-16 the documentation's `current` branch still had 2026.8.0 as the newest release. Run `sync-truths` before citing anything here.

- Version 2026.8.0, released 19 August 2026. Author of the release post: Jesse Hills.
- Headline: Bluetooth on more chips than ever.
- A new platform-neutral `ble_device_base` component moves all 39 BLE sensor platforms off their ESP32-only foundation. BLE trackers and Bluetooth Proxy now run on the Raspberry Pi Pico W, BK72xx and LN882H.
- Faster builds: ccache support on ESP8266, LibreTiny, RP2040 and host; ESP-IDF toolchain installs roughly half the size.
- Ethernet and WiFi in one configuration (multi-interface networking).
- Modbus overhaul, including the new `modbus_client` component.
- Multi-key OTA signature verification, and runtime wake word management.
- New components include the LD6002B 60 GHz presence radar and Hörmann garage door support.
- The bundled Device Builder gained faster startup, parallel uploads and one-click config migration.
- ESP32 crash reports now capture the faulting address.
- 348 pull requests from over 40 contributors.
- Fourteen entries in the upgrade checklist. Anything quoting them must quote them exactly; see `brand/voice.md`.
- Patch releases: 2026.8.1 on 24 August 2026, 2026.8.2 on 31 August 2026.

## Superseded
Previous values with the date they stopped being true, so skills can explain changes.
- none yet. This file was first filled on 2026-09-16 with 2026.8.0; there is no recorded predecessor.
