---
area: brand/audiences
project: esphome
owner: @liam
last_reviewed: 2026-09-16
review_every: 180d
draft: true
---

# ESPHome: audiences

One section per audience. Key messages in messaging.md mirror these headings. Drafted 2026-09-16 from who the site, the documentation sidebar and the release posts address. Objections are inferred from the copy that answers them and are the weakest part of this file; the interview should replace them with what maintainers actually hear.

## People who want a device nobody sells
**Cares about:** getting one thing working: a motion sensor by the front door, a button that closes the blinds. Whether they need to solder. Whether they need to code. What to buy first.
**Found on:** the home page, the Starter Kit page, the Get Started guide, YouTube, search. (https://esphome.io/, https://esphome.io/install/getting-started/)
**Comes to us from:** a store shelf with nothing on it that does the job, or a Home Assistant setup they want to extend.
**Objections:** that this is electronics and they are not an electronics person. The home page answers it directly ("no soldering, breadboarding, or coding required") and the Starter Kit exists to answer it in hardware. Confirm at interview.

## People already running ESPHome devices
**Cares about:** what breaks in this release, new components for parts they own, build times, chip support, the upgrade checklist.
**Found on:** the release blog, the changelog, the components index, the device list at https://devices.esphome.io, Discord.
**Comes to us from:** last month's release.
**Objections:** a release that silently changes a key and costs them an evening. The upgrade checklist is the standing answer. Confirm at interview.

## Component and platform developers
**Cares about:** how to add a component, the C++ and Python split, API changes between releases, review turnaround, CI.
**Found on:** GitHub, https://developers.esphome.io, the Documentation channel in Discord, GitHub Discussions for feature requests. (https://github.com/esphome/esphome/blob/dev/CONTRIBUTING.md)
**Comes to us from:** a chip or sensor they own that nothing supports yet.
**Objections:** needing the physical hardware. You cannot write or test a component for a device you do not own, so contributing is conditional on having already bought the thing (ruling 2026-09-16). Note this is a different barrier from Home Assistant's, where the objection is the size of the project and not knowing where to start.

## People reclaiming off-the-shelf devices
**Cares about:** whether their plug, bulb or relay has a chip ESPHome supports, and whether they can get their own software onto it without the vendor's cloud.
**Found on:** the LibreTiny component pages, the Tasmota migration guide, the device list, Discord. (https://esphome.io/guides/migrate_sonoff_tasmota/, https://esphome.io/components/libretiny/)
**Comes to us from:** a vendor app they no longer want, or a product whose maker stopped shipping updates.
**Objections:** TODO. Confirmed as an audience in its own right on 2026-09-16, on the grounds that it carries the sustainability pillar and has its own documentation path. Its objection is still unwritten and needs a person; no public source frames these people as a group, so there is nothing to draft it from.
