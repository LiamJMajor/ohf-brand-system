---
project: esphome
topic: proof-points
valid_from: 2026-09-16
review_by: 2026-10-16
source: multiple; see table
owner: @liam
---

# esphome: proof points

A proof point is specific, verifiable and traceable to a source. Skills copy Approved phrasing verbatim and cite this file by path. A row with Verified empty or "Never" is not usable.

Verified 2026-09-16 during onboarding stage 2. The Source column names the published URL. esphome.io was unreachable from the drafting environment, so each row was checked against the file that publishes it: the documentation site source at `esphome/esphome-docs@current` commit `1f91cc2`, or `esphome/esphome@dev` for the README and LICENSE. Anyone re-verifying should hit the URL directly.

| Claim | Canonical figure | Source | Pillar | Approved phrasing | Verified |
|---|---|---|---|---|---|
| Chip coverage | eight platforms: ESP32, ESP8266, RP2 (RP2040 and RP2350), BK72xx, RTL87xx, LN882x, nRF52, Host | https://esphome.io/components/ | choice | works with ESP32, ESP8266, RP2040 and RP2350, and the Beken, Realtek, Nordic and LN882 chips found inside off-the-shelf devices | 2026-09-16 |
| Component breadth | hundreds of components | https://esphome.io/ | choice | hundreds of components | 2026-09-16 |
| Local control | devices run on your own network, no cloud service | https://esphome.io/ | privacy | Run your devices on your own network, without the cloud | 2026-09-16 |
| Home Assistant arrival | device appears automatically over the local network | https://esphome.io/ | privacy | Your new device automatically pops up in Home Assistant over your local network: no cloud accounts or external servers required | 2026-09-16 |
| Wireless updates | first install over USB, every update after that over the air | https://esphome.io/, https://esphome.io/install/getting-started/ | sustainability | the first install goes over a USB cable; every update after that can happen wirelessly | 2026-09-16 |
| Contributors | over 2,300 people listed (2,377 entries counted 2026-09-16) | https://esphome.io/guides/supporters/ | all | built by thousands of contributors | 2026-09-16 |
| Scale of a release | 348 pull requests from over 40 contributors in 2026.8.0 | https://esphome.io/blog/2026/08/19/esphome-2026-8/ | all | 2026.8.0 carried 348 pull requests from over 40 contributors | 2026-09-16 |
| Release cadence | monthly, calendar-versioned since 2021.8.0; 2026 releases landed 21 Jan, 18 Feb, 18 Mar, 15 Apr, 20 May, 17 Jun, 15 Jul, 19 Aug | https://esphome.io/changelog/, https://esphome.io/changelog/2021.8.0/ | all | a new release every month | 2026-09-16 |
| Founder | Otto Winter (@OttoWinter) | https://esphome.io/guides/supporters/ | all | ESPHome was originally founded by Otto Winter | 2026-09-16 |
| Licence | GPLv3 for C++ and runtime code, MIT for the Python code and everything else | https://github.com/esphome/esphome/blob/dev/LICENSE | choice | open source, under GPLv3 for the runtime and MIT for the rest | 2026-09-16 |
| Ownership | a project from the Open Home Foundation; transfer date not established | https://esphome.io/, https://github.com/esphome/esphome/blob/dev/README.md | all | ESPHome is a project from the Open Home Foundation | 2026-09-16 (wording verified; the date ESPHome joined is not sourced, so no sentence may give one) |
| Analytics | Plausible, with a public dashboard | https://plausible.openhomefoundation.org/esphome.io | privacy | the site uses privacy-first analytics, and anyone can see the data | 2026-09-16 |
| Starter Kit hardware | ESP32-C6 board, four modules: motion, temperature and humidity, notification, button | https://esphome.io/blog/2026/08/12/the-esphome-starter-kit-is-here/ | choice | an ESP32-C6 board and four snap-apart modules: motion, temperature and humidity, notification, and button | 2026-09-16 |
| Starter Kit partner | designed and produced by Apollo Automation, the Open Home Foundation's second commercial partner | https://esphome.io/blog/2026/08/12/the-esphome-starter-kit-is-here/ | all | designed and produced by Apollo Automation, the Open Home Foundation's second commercial partner | 2026-09-16 |
| Starter Kit funds the foundation | majority of profit from every kit | https://esphome.io/blog/2026/08/12/the-esphome-starter-kit-is-here/ | all | the majority of profit from every kit goes straight to the Open Home Foundation | 2026-09-16 |
| Device Builder | replaced the retired dashboard in 2026.6.0 | https://esphome.io/blog/2026/07/02/unbox-your-creativity-with-the-esphome-device-builder/ | choice | the ESPHome Device Builder replaced the old dashboard in 2026.6.0 | 2026-09-16 |
| Desktop App | Windows, macOS and Linux | https://esphome.io/blog/2026/08/04/simplify-your-esphome-setup-with-the-new-desktop-app/, https://esphome.io/install/ | choice | the ESPHome Desktop App runs on Windows, macOS, and Linux | 2026-09-16 |

## Not yet usable
Facts an agent will reach for and must not state, because no source was found.
- The year ESPHome was founded, and the year it joined the Open Home Foundation.
- Any count of devices running ESPHome, or of installs.
- GitHub stars or fork counts. The GitHub API was not reachable from the drafting environment; a figure here would have been copied from memory, which is how a wrong number enters a system and never leaves.
