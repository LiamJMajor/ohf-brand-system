---
area: brand/strategy
project: esphome
owner: @liam
last_reviewed: 2026-09-16
review_every: 180d
draft: false
---

# ESPHome: strategy

The source every other brand file derives from. `core/story.md` and `core/pillars.md` are the shared material; this file is ESPHome's reading of them. Drafted 2026-09-16 from the home page, the Get Started guide, the 2026.8.0 release post and the Starter Kit announcement. Positioning and personality are proposals for the interview.

## Purpose
ESPHome exists so that the smart home device you want can be built by you when nobody sells it. The home page puts the case in one sentence: "When you can't find the smart home device you need in a store, build it yourself!" (https://esphome.io/, `src/components/Homepage/Hero.astro`). You describe the hardware in YAML, or pick it in the Device Builder; ESPHome writes the code that runs on the chip.

## Positioning
ESPHome is how a person builds the smart home device nobody sells them. You describe the hardware attached to an inexpensive microcontroller, in YAML or by picking it in the Device Builder, and ESPHome writes and installs the software that runs it, with no C++ and no cloud account in the middle. The finished device runs on your own network and speaks open standards, so it works with the smart home system you already have.

Confirmed 2026-09-17. The position is building smart home devices. Compatibility with Home Assistant is a benefit of the finished device and is never the position itself: the goal is to work with every smart home system, and ESPHome's own copy already says so twice. The home page: the chip "can then 'talk' directly to Home Assistant or any other smart home system that supports it". The Starter Kit announcement: it can "talk to Home Assistant or any other smart home platform that supports it", and the kit "uses the same open standards as the rest of your smart home" (https://esphome.io/, https://esphome.io/blog/2026/08/12/the-esphome-starter-kit-is-here/).

Naming Home Assistant in the position would also breach `core/voices.md`: it would make one Open Home Foundation project's pitch depend on another's, which is not how the projects relate.

(Swap test: no other configuration-first device builder covers that spread of chips, ships a monthly release with a written upgrade checklist, and is stewarded by a non-profit.)

## Personality
Attributes as decisions with contrast pairs. Reviewed 2026-09-16.

Two attributes, not three. This section previously restated rules that belong elsewhere, because stage 2 drafted the brand files in parallel rather than deriving them from this one, so the voice rulings of 2026-09-16 did not reach here. "No code required, and the code is right there" was removed: it was ruled a messaging rule and lives in `brand/messaging.md` under Message rules. What remains is character that is not already a rule in another file.

### Exact about what you have to change, where exactness is what the reader needs
**Scoped to change notes** (ruling 2026-09-16). When something breaks, say which key, in which component, and which release removes the old one. Because the reader has a configuration file open and a device that will not compile. Elsewhere, this precision is a barrier rather than a service, and release notes and social aim for accessibility instead. Source: the 2026.8.0 upgrade checklist, fourteen entries, every one of them an instruction (https://esphome.io/blog/2026/08/19/esphome-2026-8/).
- Yes: "If you set `esp32_ble_id` explicitly on any BLE sensor platform, rename it to `ble_hub_id` (the old key warns until 2027.2.0)."
- No: "Some Bluetooth configuration keys have been updated. Please review your configuration."

### The contributors are named
A feature belongs to the person who sent the pull request, by handle, with the number. Because 348 pull requests from over 40 people is what a release is (https://esphome.io/blog/2026/08/19/esphome-2026-8/). Confirmed 2026-09-16, and it holds in every register: the Starter Kit announcement credits Apollo Automation's founders by name and quotes one of them at length, which is the same instinct without the handles.
- Yes: "Led by [@Bl00d-B0b](https://github.com/Bl00d-B0b) across dozens of PRs, the shared BLE advertisement layer moved into a new platform-neutral `ble_device_base` component ([#17150](https://github.com/esphome/esphome/pull/17150))."
- No: "We rebuilt the Bluetooth stack this release."

## Pillar translations
What ESPHome concretely does about each belief in `core/pillars.md`.

### Privacy
The device runs on your own network. The home page states it as a property of the software, not a promise: "Run your devices on your own network, without the cloud" (https://esphome.io/). There is no ESPHome account, because there is no ESPHome service to have an account with, and nothing is routed through anyone's server on the way to whatever system you control it from.

### Choice
Choice of hardware and choice of system, both. Hundreds of components across eight chip platforms, including the Beken, Realtek and LN882 chips found inside off-the-shelf plugs and bulbs, and the Host platform that runs components on a computer with no board attached (https://esphome.io/components/). And the finished device speaks open standards rather than a private protocol, so it "can talk directly to Home Assistant or any other smart home system that supports it" (https://esphome.io/). A device you build is not tied to a vendor's app, because there is no vendor, and not tied to one smart home system either.

### Sustainability
Two directions. ESPHome puts new software on hardware you already own, including hardware whose maker has moved on: the documentation ships a migration guide from Tasmota and supports the chips in cheap retail devices (https://esphome.io/guides/migrate_sonoff_tasmota/). And the Starter Kit was designed against the same belief: "One of the foundation's principles is sustainability. So, this isn't something that you just buy, learn, and then put in a drawer or the trash never to be seen again. You can make real usable products out of this at the end." (Trevor Schirmer, Apollo Automation, https://esphome.io/blog/2026/08/12/the-esphome-starter-kit-is-here/)
