---
area: brand/messaging
project: esphome
owner: @liam
last_reviewed: 2026-09-16
review_every: 180d
draft: true
---

# ESPHome: messaging

Derives from strategy.md. Agents copy Boilerplate verbatim; long-form builds from Key messages. Every fact traces to `truths/esphome/proof-points.md`. Drafted 2026-09-16; nothing here is confirmed.

## Key messages
One per audience in audiences.md.

### People who want a device nobody sells
Buy a board, snap a sensor onto it, and tell ESPHome what it is. It writes the code and installs it, and the device appears in Home Assistant on your own network a minute later. The ESPHome Starter Kit exists so the first one takes no soldering, no breadboard and no code at all.
(Answers the objection: this is electronics and I am not an electronics person.)

### People already running ESPHome devices
Every release ships with an upgrade checklist that names the key, the component and the release the old spelling stops working, so you can read the list before you update instead of after. New components land every month, and 2026.8.0 alone carried 348 pull requests from over 40 people.
(Answers the objection: a release that quietly changes something under me.)

### Component and platform developers
A component is Python for the configuration and C++ for the runtime, in one directory, with the developer documentation at developers.esphome.io describing the split. Your component ships to every chip family ESPHome supports, and the release post credits you by handle with your pull request number.
(Answers the objection: TODO, because audiences.md has no confirmed objection for this group.)

### People reclaiming off-the-shelf devices
The Beken, Realtek and LN882 chips inside cheap plugs and bulbs are supported chips, not exotic ones, and the documentation carries a migration path from Tasmota. The device keeps working after the vendor stops caring, on your network, answering to you.
(Answers the objection: TODO. This audience is itself a proposal.)

## Boilerplate
### One line
ESPHome turns ESP32, ESP8266, and RP2040 microcontrollers into fully-featured smart home devices.

### 50 words
ESPHome turns ESP32, ESP8266, and RP2040 microcontrollers into fully-featured smart home devices. You describe the hardware in a YAML configuration file, or pick it in the ESPHome Device Builder, and ESPHome writes and installs the code. Every device works with Home Assistant over your local network. ESPHome is a project from the Open Home Foundation.

### 100 words
ESPHome turns ESP32, ESP8266, and RP2040 microcontrollers into fully-featured smart home devices. You describe the hardware attached to a board in a YAML configuration file, or pick it in the ESPHome Device Builder, and ESPHome writes the code, builds it and installs it: over USB the first time, wirelessly after that. Every device appears in Home Assistant over your local network, with no cloud account required. Hundreds of components cover sensors, switches, lights, displays and more, across the eight platforms listed in the components index. Founded by Otto Winter and built by thousands of contributors, ESPHome is a project from the Open Home Foundation.

## Taglines
| Tagline | Use | Status |
|---|---|---|
| Smart Home Made Simple | site title and meta description (https://esphome.io/) | in use |
| Custom smart home devices, built by you | home page headline (https://esphome.io/) | in use |

## We don't say
| Avoid | Say instead | Why |
|---|---|---|
| seamless, robust, powerful, and the rest of the core list | the specific thing | they describe nothing. The home page's own microcontroller card calls the ESP32 "Powerful, budget-friendly" (https://esphome.io/); that is legacy copy, and new writing says what the chip lets you do |
| integration | component | ESPHome's own word for the same idea. Home Assistant says integration; do not carry it across. (https://esphome.io/components/) |
| ESP, EspHome, esphome in prose | ESPHome | project names are never shortened or recased (`decisions/2026-09-14-proposal-never-shorten-project-names.md`); lowercase `esphome` belongs to the command, the package and the repository |
| a competitor named critically | nothing; route to foundation voice | project voices do not criticise (`core/voices.md`) |
| announcing another project's news | link to their post | nobody announces on someone else's behalf (`core/voices.md`, Cross-promotion) |
| firmware | TODO | the OHF editorial guide wants the word avoided (`projects/home-assistant/brand/style.md`); ESPHome's documentation uses it as the core noun of the explanation. Unresolved: this row is a question for the interview, not a rule |
