---
conforms_to: website
project: esphome
owner: @liam
last_reviewed: 2026-09-16
review_every: 180d
draft: true
---

# ESPHome: website

The standard is `core/standards/website.md`. Rows below are its Required elements, checked against esphome.io on 2026-09-16 via the site source at `esphome/esphome-docs@current`, commit `1f91cc2`. The standard's own last two required elements are still TODO in the standard, so they cannot be checked here.

## Conformance

| Required element | Location | Status | Deviation |
|---|---|---|---|
| Foundation attribution in the footer, approved wording, naming the non-profit and its three principles | footer: "ESPHome is a project from the Open Home Foundation" beside the OHF lockup, linking to openhomefoundation.org | partial | names the foundation and links it, but carries neither "non-profit" nor privacy, choice, and sustainability. Home Assistant's footer carries the full sentence. Either the footer changes or the standard admits this shorter form |
| One-line boilerplate visible on the home page, verbatim from `brand/messaging.md` | site description: "Smart Home Made Simple. ESPHome turns ESP32, ESP8266, and RP2040 microcontrollers into fully-featured smart home devices." Home page headline is "Custom smart home devices, built by you" | present | the boilerplate is in the page metadata and title, not in the visible hero. The visible hero is a different line. `brand/messaging.md` takes the metadata sentence as the One line, so the two agree, but the standard says visible |
| Entry points to every community space in `marketing/channels.md` | home page "Join our community" section; footer Community column; header social links. Discord, GitHub, Home Assistant forum | present | all three lists agree, which is why the absence of any social account is treated as a finding rather than an oversight |
| Entry points to release notes or changelog, and to the blog | sidebar "Keeping Up" (Blog, Changelog); footer Resources column (Changelog) | present | the blog is in the sidebar but not in the footer columns |
| Privacy-respecting analytics, provider named on the site | footer: "This website uses privacy-first analytics", linking the Plausible announcement and the public dashboard at plausible.openhomefoundation.org/esphome.io | present | exceeds the requirement: the dashboard is public |
| Required top-level navigation and its order | current nav: Getting Started, ESPHome Starter Kit, Components, Automations, Guides, Cookbook, Keeping Up, Changelog | unknown | the standard leaves this TODO; recorded so it can be checked when the standard is written |
| Required legal pages (privacy, terms, trademark) | none found on esphome.io | unknown | the standard leaves this TODO. No privacy or trademark page was found on the site; if the standard comes to require one, this becomes missing |

## Rules checked
- **Product on the project site, cause on the foundation site.** Holds. Advocacy arrives only as crossposts that redirect to openhomefoundation.org, which keeps the voices separate by construction.
- **Commercial partners are named as partners.** Holds. Apollo Automation is named as designer and producer of the Starter Kit and as the foundation's second commercial partner, never as an owner.
- **Never: a competitor named critically.** Holds in everything read. The Tasmota migration guide is a migration path, not a comparison.
