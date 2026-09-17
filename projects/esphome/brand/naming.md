---
area: brand/naming
project: esphome
owner: @liam
last_reviewed: 2026-09-16
review_every: 180d
draft: false
---

# ESPHome: naming

Drafted 2026-09-16 from the site, the README and the changelog that recorded the rename.

## Canonical
- Full name: ESPHome. One word. Capital E, S, P and H, the rest lowercase. Never a space, never a hyphen.
- Short name: none. Project names are never shortened in public writing (`decisions/2026-09-14-proposal-never-shorten-project-names.md`).
- Capitalisation in a sentence: "ESPHome 2026.8.0 brings Bluetooth to more chips than ever." The name never changes case for position in a sentence.
- Lowercase `esphome` is correct in exactly three places and nowhere else: the command line tool, the Python package, and repository and URL paths (`esphome/esphome`, `ghcr.io/esphome/esphome`, `esphome logs /config/esphome`). Confirmed as a rule 2026-09-16. The boundary is drawn from usage across the install documentation rather than from a statement by the project; ESPHome has never written this down, and it is a rule here from now on.
- The name is historical: the project was called esphomeyaml, with a C++ library called esphomelib, until the v1.10.0 rename to ESPHome and ESPHome Core. "The name esphomelib and esphomeyaml were too technical" (https://esphome.io/changelog/v1.10.0/). Both old names are dead; never revive either.

## Feature naming
- First-party things are named with ESPHome in front and Title Case after it: ESPHome Device Builder, ESPHome Starter Kit, ESPHome Desktop App. **Written in full on first mention in a piece**, shortened freely after that ("the kit", "the Device Builder"). Confirmed as a rule 2026-09-16. Observed in the Starter Kit announcement, which names the kit in full and then shortens it three times; turned into a rule here rather than left as a tendency.
- Ready-Made Projects: Title Case, hyphenated, plural, as the documentation writes it (https://esphome.io/projects/).
- Components are named by their configuration key, lowercase with underscores, in backticks: `modbus_client`, `esp32_ble_tracker`, `deep_sleep`. Component documentation page titles use Title Case for the human name ("Modbus Client", "Deep Sleep"), so a sentence gives the human name and the key together on first mention: "the new Modbus Client component (`modbus_client`)".
- Chips and boards take the vendor's capitalisation, never the project's: ESP32, ESP32-C6, ESP8266, RP2040, RP2350, BK72xx, RTL87xx, LN882H, nRF52.

## Forbidden variants
| Do not write | Write instead | Why |
|---|---|---|
| ESP Home, Esphome, EspHome, ESPhome | ESPHome | one word, and only the H is internally capitalised |
| esphome (in prose) | ESPHome | lowercase belongs to the command, the package and repository paths |
| ESP | ESPHome | ESP is Espressif's chip family, not this project; using it for the project makes the sentence wrong as well as short |
| esphomeyaml, esphomelib | ESPHome | retired at the v1.10.0 rename (https://esphome.io/changelog/v1.10.0/) |
| the ESPHome dashboard | the ESPHome Device Builder | officially retired in 2026.6.0 (https://esphome.io/blog/2026/07/02/unbox-your-creativity-with-the-esphome-device-builder/) |
| ESPHome integration | ESPHome component | see `brand/style.md` glossary; integration is Home Assistant's word |

## Attribution
Conforms to the core co-branding standard. Two forms are in use and both are approved as they stand:
- Site footer, verbatim: "ESPHome is a project from the Open Home Foundation", set beside the foundation lockup (https://esphome.io/).
- README badge, verbatim: "ESPHome - A project from the Open Home Foundation" (https://github.com/esphome/esphome/blob/dev/README.md).

Short form for press and partner contexts: "ESPHome, an Open Home Foundation project". Never "owned by" or "a product of".

The short form is not ESPHome's own wording; no ESPHome source uses it. It is the organisation's pattern, confirmed for Home Assistant by the marketing team on 2026-09-14 (`projects/home-assistant/brand/naming.md`, `draft: false`) and ruled on 2026-09-16 to apply across projects with the name swapped. Worth noting this is the same shape as the question deferred in round 1: a rule confirmed for one project, living in that project's directory, being applied to others. Deferring it once is fine; the third time a project needs this form, it should be in `core/`.

Note for the interview: `core/standards/website.md` requires footer attribution that names the foundation as a non-profit and states its three principles, the way home-assistant.io does. The ESPHome footer names the foundation and shows its lockup but carries neither the word non-profit nor the principles. Either the footer changes or the standard records ESPHome's form as an accepted variant. Recorded as a deviation in `standards/website.md`.

Apollo Automation is named as the designer and producer of the ESPHome Starter Kit, and as "the Open Home Foundation's second commercial partner" (https://esphome.io/blog/2026/08/12/the-esphome-starter-kit-is-here/). Never as the owner of anything ESPHome.
