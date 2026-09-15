---
area: brand/strategy
project: home-assistant
owner: Marketing Team
last_reviewed: 2026-09-14
review_every: 180d
draft: false
---

# Home Assistant: strategy

Where Home Assistant translates the shared core into its own terms. `core/story.md` and `core/pillars.md` are the source; this file is the project's reading of them. The other brand files derive from core and from this translation. Drafted from the README, home page and footer (https://github.com/home-assistant/core/blob/dev/README.rst, https://www.home-assistant.io/). Positioning and personality are proposals for the interview.

## Purpose
Home Assistant exists so that a person can automate their home from hardware they own, with their data staying in the house. The README says it in eleven words: "Open source home automation that puts local control and privacy first." Everything else is detail.

## Positioning
Home Assistant is the home automation platform for people who want their home to work for them rather than for a vendor. It runs on your own hardware, connects devices from over a thousand brands, and treats the cloud as an option you switch on, not a requirement.

(Swap test: no other platform can truthfully claim local-first, 1500+ integrations and non-profit ownership together. Confirm.)

## Personality
Attributes as decisions with contrast pairs. All three are drafted from how the project already writes; confirm or replace.

### Honest about the unglamorous
Say plainly when something was hard or overlooked. Because readers are tinkerers and can tell. Source: the 2026.9 release post opens "I'll be honest: Modbus has never been the flashiest part of Home Assistant." (https://www.home-assistant.io/blog/2026/09/02/release-20269/)
- Yes: "Modbus has never been the flashiest part of Home Assistant. This release finally makes room on the bus."
- No: "We're thrilled to announce revolutionary new Modbus capabilities."

### Makers talking to makers
Assume the reader is capable and curious, never a consumer to be sold to. Because the community is described as "tinkerers and DIY enthusiasts" (https://github.com/home-assistant/core/blob/dev/README.rst).
- Yes: "You simply pick your device in the UI like anything else in Home Assistant."
- No: "Our intuitive experience makes smart home setup effortless for everyone."

### Local first, stated plainly
State the privacy position as a fact about how the software works, not as a value statement. Because the home page section is titled "All your smart home data stays local" and follows with "no need for a cloud" (https://www.home-assistant.io/).
- Yes: "Home Assistant keeps your data local. No need for a cloud."
- No: "We deeply believe in respecting your privacy."

## Pillar translations
What Home Assistant concretely does about each belief in `core/pillars.md`.

### Privacy
Runs on hardware in your home. Data stays local by default; cloud services, including Home Assistant Cloud from Nabu Casa, are optional and opt-in. (https://www.home-assistant.io/, section "All your smart home data stays local")

### Choice
Integrates over a thousand brands through 1500+ integrations, and the project publicly campaigns for interoperability (blog: "A big win for Android interoperability", July 2026). Devices from any maker, one system. (https://www.home-assistant.io/)

### Sustainability
Home Assistant keeps hardware useful for longer, and makes hardware smart that was never meant to be. Infrared became a first-class citizen in 2026.4 and radio frequency in 2026.5, so remotes and RF devices are controlled from Home Assistant directly (https://www.home-assistant.io/blog/2026/04/01/release-20264/#infrared-becoming-a-first-class-citizen-of-home-assistant, https://www.home-assistant.io/blog/2026/05/06/release-20265/#radio-frequency-joins-infrared-as-a-first-class-citizen). Serial devices have their own panel since 2026.9, and serial proxies let you control devices over serial (https://www.home-assistant.io/blog/2026/09/02/release-20269/). It runs on a Raspberry Pi or a server you already own rather than new hardware. (Confirmed in interview 2026-09-14. The serial proxy feature is cited from the interview; its release link is an open follow-up in PROJECT.md.)
