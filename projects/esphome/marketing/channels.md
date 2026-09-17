---
area: marketing/channels
project: esphome
owner: @liam
last_reviewed: 2026-09-16
review_every: 90d
draft: true
---

# ESPHome: channels

Classes from `core/channels.md`. Drafted 2026-09-16 from the site footer, the documentation sidebar's "Keeping Up" section, the home page community section and the Starlight social configuration. Owners TODO throughout.

**ESPHome appears to own no social accounts.** Three independent places on its own site list where to find the project (footer, header social links, home page community section) and all three list the same three destinations: Discord, GitHub, and the Home Assistant community forum. No X, Mastodon, Bluesky, Facebook, Instagram, YouTube or newsletter is linked from anywhere on esphome.io. Either they do not exist, or they exist and the project's own site does not point at them, and both are findings. Until the interview settles it, no skill should assume a social destination for ESPHome output.

| Channel | Purpose | Register | Cadence | Handle | Owner |
|---|---|---|---|---|---|
| Blog | product announcements, release posts | Medium and High | monthly release plus announcements | https://esphome.io/blog/ | TODO |
| Changelog | the full per-release record | Medium | monthly, plus patch releases | https://esphome.io/changelog/ | TODO |
| Documentation | components, guides, cookbook, automations | quiet, technical | continuous | https://esphome.io/ | TODO |
| Discord | chat, support, the Documentation channel for doc corrections | conversational | continuous | https://esphome.io/chat (https://discord.gg/KhAMKrd) | TODO |
| Community forum | questions, project sharing | conversational | continuous | https://community.home-assistant.io/c/esphome/ (Home Assistant's forum, ESPHome category) | TODO |
| GitHub | development, issues | quiet, technical | continuous | https://github.com/esphome/esphome | TODO |
| GitHub Discussions | feature requests | quiet, technical | continuous | https://github.com/orgs/esphome/discussions | TODO |
| Blog comments | per-post discussion, via Discourse embed | conversational | per post | Discourse embed on blog posts | TODO |
| Developer docs | contributing, component APIs | quiet, technical | continuous | https://developers.esphome.io | TODO |
| Device list | which hardware works | quiet, technical | continuous | https://devices.esphome.io | TODO |
| Livestream | release parties and events | High | per event | LivestreamCard on the home page, slug `esphome` | TODO: which YouTube channel it resolves to |
| Social | none found | | | none | TODO: confirm whether any exist |
| Newsletter | none found | | | none | TODO: the foundation manages email preferences per project (`core/channels.md`); confirm whether ESPHome has a scope there |

## Notes for the interview
- ESPHome's community forum is a category inside Home Assistant's forum, not its own. That is a real dependency on another project's channel and worth a deliberate answer rather than an inherited one.
- The blog opened in July 2026 and was introduced as a deliberate second register: "We usually share our updates through raw, engineering-focused changelogs. While that technical documentation isn't going anywhere, we want to make our milestone releases more digestible for everyone in the community" (https://esphome.io/blog/2026/07/02/unbox-your-creativity-with-the-esphome-device-builder/). Blog and changelog are two channels, not one, and `brand/voice.md` treats them that way.
- Blog posts can be crossposts from the foundation, carried with a canonical link and an immediate redirect (the Plausible analytics post is one). Amplification, not authorship: confirm who decides what gets crossposted.
