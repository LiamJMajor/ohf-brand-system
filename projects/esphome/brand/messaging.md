---
area: brand/messaging
project: esphome
owner: @liam
last_reviewed: 2026-09-16
review_every: 180d
draft: false
---

# ESPHome: messaging

Derives from strategy.md. Agents copy Boilerplate verbatim; long-form builds from Key messages. Every fact traces to `truths/esphome/proof-points.md`.

**Home Assistant is a benefit, never the pitch** (ruling 2026-09-17). ESPHome's position is building smart home devices. Compatibility is stated as open standards working with the system the reader already has, naming Home Assistant as one of them rather than as the destination. Copy that makes Home Assistant the point has drifted off position.

## Key messages
One per audience in audiences.md.

### People who want a device nobody sells
Buy a board, snap a sensor onto it, and tell ESPHome what it is. It writes the code and installs it, and the device turns up on your own network a minute later, in whichever smart home system you run. The ESPHome Starter Kit exists so the first one takes no soldering, no breadboard and no code at all.
(Answers the objection: this is electronics and I am not an electronics person.)

### People already running ESPHome devices
Every release ships with an upgrade checklist that names the key, the component and the release the old spelling stops working, so you can read the list before you update instead of after. New components land every month, and 2026.8.0 alone carried 348 pull requests from over 40 people.
(Answers the objection: a release that quietly changes something under me.)

### Component and platform developers
A component is Python for the configuration and C++ for the runtime, in one directory, with the developer documentation at developers.esphome.io describing the split. You need the device in your hands to write and test one, which is the real barrier: the `host` platform runs components on your computer with no board attached, and the device list at devices.esphome.io shows what is already covered before you buy anything. Your component ships to every chip platform ESPHome supports, and the release post credits you by handle with your pull request number.
(Answers the objection: you cannot write or test a component for a device you do not own.)

### People reclaiming off-the-shelf devices
Check the device list at devices.esphome.io before you do anything else: if someone has already put ESPHome on your exact plug or bulb, the hard part is done and the teardown is written down. The Beken, Realtek and LN882 chips inside cheap retail devices are supported chips, not exotic ones, and the documentation carries a migration path from Tasmota. Getting in usually means opening the case once; after that every update is wireless. What you lose is the vendor's app, and what you get back is a device that keeps working after the vendor stops caring, on your network, answering to you.
(Answers all four objections in audiences.md: is my chip supported, will I brick it, do I have to open it, what do I lose. The device list answers the first and is deliberately the opening move.)

## Message rules
Ruled a messaging rule rather than a voice rule on 2026-09-16, and moved here from `brand/voice.md`.

### Both halves of the promise, in the same breath
No code required, and the YAML is right there. Never one without the other. Because the beginner needs permission to start and the veteran needs proof they are not being fenced out. Source: the home page (https://esphome.io/).
- Yes: "Its intuitive Device Builder replaces code with simple visual choices [...] And for experienced users who prefer writing code manually, YAML is always there if you need it."
- No: "ESPHome now handles everything for you, so you never need to see a configuration file again."

## Boilerplate
### One line
ESPHome turns ESP32, ESP8266, and RP2040 microcontrollers into fully-featured smart home devices.

### 50 words
ESPHome turns ESP32, ESP8266, and RP2040 microcontrollers into fully-featured smart home devices. You describe the hardware in a YAML configuration file, or pick it in the ESPHome Device Builder, and ESPHome writes and installs the code. Every device runs on your own network and works with Home Assistant or any other smart home system that supports it. ESPHome is a project from the Open Home Foundation.

### 100 words
ESPHome turns ESP32, ESP8266, and RP2040 microcontrollers into fully-featured smart home devices. You describe the hardware attached to a board in a YAML configuration file, or pick it in the ESPHome Device Builder, and ESPHome writes the code, builds it and installs it: over USB the first time, wirelessly after that. Every device runs on your own network and talks to Home Assistant or any other smart home system that supports it, with no cloud account required. Hundreds of components cover sensors, switches, lights, displays and more, across the eight platforms listed in the components index. Founded by Otto Winter and built by thousands of contributors, ESPHome is a project from the Open Home Foundation.

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
| firmware | the software ESPHome builds; the code that runs on the chip | ruled avoided everywhere on 2026-09-16, per the OHF editorial guide. ESPHome's home page and Get Started guide both use it today, so new copy diverges from published copy here until that is corrected |
