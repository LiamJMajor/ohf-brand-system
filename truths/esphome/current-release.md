---
project: esphome
topic: current-release
valid_from: 2026-09-16
review_by: 2026-10-21
source: https://esphome.io/blog/2026/09/16/esphome-2026-9/
owner: @liam
auto_updated_by: sync-truths
---

# esphome: current-release

Facts only. Each fact is something a skill may state as true until `review_by`.

- Version 2026.9.0, released 16 September 2026. Author of the release post: Jesse Hills.
- Headline: faster builds and encrypted updates.
- Noise (ChaCha20-Poly1305) encryption for OTA updates, using the same key that already secures the link to Home Assistant. Encryption's flash cost cut by close to half on every platform.
- PlatformIO installs parallelised end to end; the package phase drops from 36% of build time to 25% on CI benchmarks.
- Scaffolding for a native ESP8266 toolchain lands across eight infrastructure pull requests.
- 211 conditional log string literals moved off ESP8266 RAM into flash, across a sweep of 60 files.
- Improv Serial extended beyond WiFi, so Ethernet-only boards can report status and web server URL to setup tools.
- WiFi provisioning shuts down the access point and captive portal when the window closes.
- Infrared transmission on the BK7238 and RTL8720C rewritten to run from a hardware timer interrupt rather than a busy-wait.
- Modbus overhaul continues: heap-free write path, consolidated range-join option, continuous polling.
- Out-of-memory hardening: no reboot when the heap runs out during WiFi scans, stalled API writes, or OTA verification.
- Six new components: `ds1603l`, `d01`, `sfa40`, `mk2pvrouter`, `snapshot`, `noise`. Around twenty feature additions to existing components.
- Device Builder masks credentials in the YAML diff view, boots ESP32-C6 boards after a browser flash, and recovers from a paired build server changing address.
- 275 pull requests from over 40 contributors.
- Eleven entries in the upgrade checklist. Anything quoting them must quote them exactly; see `brand/voice.md`.
- No patch releases yet as of 2026-09-17.

## Register note
This release is the first to open with a plain-language section, "Short on time? Here's the quick version", ahead of the technical write-up. It names the three changes that affect a typical configuration in ordinary words, then says plainly that a typical setup needs nothing else. It is evidence that ESPHome is already moving in the direction the accessibility ruling of 2026-09-16 set, and the strongest example currently available of that register. Worth harvesting.

## Superseded
Previous values with the date they stopped being true, so skills can explain changes.
- 2026.8.0, released 19 August 2026, with patch releases 2026.8.1 on 24 August and 2026.8.2 on 31 August (until 2026-09-16).
