---
area: brand/style
project: esphome
owner: @liam
last_reviewed: 2026-09-16
review_every: 180d
draft: true
---

# ESPHome: style

Mechanics. The things agents get wrong most often. Drafted 2026-09-16 from `CONTRIBUTING.md` and `AGENTS.md` in the documentation repository, and from measuring the 2026 blog posts. Each rule is marked with where it traces: (docs) the documentation contributing guide, which is authoritative for documentation only; (observed) counted in published copy; (house) the organisation ruling in `decisions/2026-09-15-ohf-house-style.md`.

Two guides sit above this file and have not been reconciled with it: the OHF Editorial Style Guide and, where it is silent, the Microsoft Writing Style Guide (see `projects/home-assistant/brand/style.md`). ESPHome has its own documentation guide as well, and it disagrees with both on headings. The interview needs to say which governs ESPHome's blog, because the answer changes every heading the project writes.

## Spelling and grammar
- Spelling convention: US English (house). Published blog copy agrees: across the 2026 posts, 122 US forms ("optimizations", "behavior", "color") and zero UK forms. Documentation pages are mixed and contain UK spellings ("recognised" in the Get Started guide); trust the rule, not the page in front of you.
- Serial comma: yes (house). Observed in the project's own copy: "no soldering, breadboarding, or coding required" (https://esphome.io/).
- Contractions: yes, in every register, including release posts. "It's", "don't", "you've" appear throughout (observed, 30 in the 2026 posts).
- Present tense, active voice (docs).
- Line length: wrap source at 120 characters (docs). Applies to anything committed to the documentation or blog repositories.
- Em dashes: **do not use them.** Banned outright, every register, every surface, across every project and the foundation. Confirmed org-wide on 2026-09-16, which closes the question `decisions/2026-09-15-social-register-and-tells.md` left open. Recorded loudly because an agent reaches for one about every second paragraph. **Known gap in existing copy:** ESPHome's published 2026 posts contain 52 em dashes and 20 en dashes. New copy complies; correcting the archive is a separate decision nobody has funded.

## Capitalisation
- Headings in documentation and release posts: Title Case (docs, and observed: "Release Overview", "Upgrade Checklist", "New Components", "Thank You, Contributors").
- Headings on the home page and in product announcements: sentence case (observed: "How ESPHome works", "Begin here", "What's in the box?", "Three things to try with the ESPHome Starter Kit"). The split is real and consistent. Do not normalise one to the other.
- Product and feature names: see naming.md.
- Component names in prose: lowercase, exactly as the configuration key is spelled, in backticks: `modbus_client`, `esp32_ble_tracker`, `deep_sleep`.
- Chip and board names take the vendor's capitalisation: ESP32, ESP8266, ESP32-C6, RP2040, RP2350, BK72xx, RTL87xx, LN882H, nRF52.

## Numbers and dates
- Version numbers: `YYYY.M.P`, always three parts, including the first release of a month: 2026.8.0, then 2026.8.1, 2026.8.2. Unlike Home Assistant, ESPHome does not write a two-part version. (observed; ESPHome has used calendar versioning since 2021.8.0, https://esphome.io/changelog/2021.8.0/)
- Deprecations name the release that removes the old spelling: "the old key warns until 2027.2.0" (observed).
- Dates in prose: month then day, no ordinals: "Release 2026.8.1 - August 24" (observed). Old changelog titles use "18th August 2021"; that form is retired, do not copy it.
- Dates in frontmatter and metadata: ISO, `2026-08-19` (observed).
- Pull requests: linked by number, `[#17150](https://github.com/esphome/esphome/pull/17150)` (observed).
- Units: metric, matching Home Assistant (ruling 2026-09-16). Numerals for all measurements, even under 10. A space between the number and the unit; hyphenate when the measurement modifies a noun. Abbreviations only with numerals, never followed by a period. Yes: "3 cm", "a 13.5-inch display", "21 °C". No: "3cm", "3 cm.", "21 degrees C". Board and enclosure dimensions are no exception, even where the part is sold in inches.

## Formatting
- Links: descriptive text, never a bare URL, never "click here". Internal documentation links are relative and end in a trailing slash: `/components/wifi/` (docs).
- Code, configuration keys, file paths, component names and anything the reader types: backticks (docs).
- Pins in examples: the literal string `GPIOXX`, with the `XX` left as written, except where the hardware has fixed pins (docs). An agent that substitutes a real pin number has introduced a bug into someone's config.
- Examples are minimal: the essential configuration only, with optional variables left out, and a dependency linked rather than inlined (docs).
- Lists: `-` for unordered (docs, `.markdownlint.json` MD004).
- Images: descriptive alt text always. The alt text in the Starter Kit post is a model of it: "ESPHome Starter Kit modules on a table, with the ESPHome logo shaped notification module illuminated by rainbow LED lights."
- Emoji: one 🎉 appears in the Starter Kit announcement. Nothing else across the 2026 posts, and no social examples exist to draw from. Treat emoji as unestablished here rather than as banned or expected.

## Glossary
Terms taken from the documentation and the home page as published. This table is the most useful thing in this file for an agent that has written for Home Assistant before, because the two projects use different words for the same shape of thing.

| Term | Use | Not |
|---|---|---|
| component | the unit of hardware or feature support, named by its configuration key | integration, plugin, module |
| platform | a component's implementation for a particular family, as in `sensor` platforms | driver |
| configuration | the YAML describing a device | config file, sketch, script |
| ESPHome Device Builder | the visual interface for creating, editing and installing configurations | dashboard (officially retired in 2026.6.0, https://esphome.io/blog/2026/07/02/unbox-your-creativity-with-the-esphome-device-builder/), web UI, wizard |
| board | the physical development board | device (when the board alone is meant) |
| device | the finished thing: board plus components plus the software ESPHome built | unit, gadget. "node" still appears in the FAQ and is not a term public writing should pick up |
| microcontroller, chip | the programmable part, glossed on first mention for new readers | MCU, processor |
| Ready-Made Projects | the pre-built configurations installed from the browser | templates, presets |
| ESPHome Starter Kit | the hardware kit, named in full | the kit (on second mention only), starter pack |
| over the air, OTA | wireless installation after the first USB install | flash over WiFi |
| Home Assistant | always in full, always the destination it appears in | HA, hass |
| firmware | the software ESPHome builds; the code that runs on the chip | firmware. Ruled avoided everywhere on 2026-09-16. ESPHome's own published copy uses it ("ESPHome reads that description and builds custom firmware for your device"), so this is a gap in existing copy, not a description of it |

## Machine checks
Rules an agent or script can apply to a draft before a person sees it.
| Check | Pattern | Fix |
|---|---|---|
| No em dashes | `—` | split the sentence or use a colon |
| No banned words | the core list, see messaging.md | the specific thing |
| Version has three parts | `\b20\d{2}\.\d{1,2}(?!\.)` | write 2026.8.0, not 2026.8 |
| No shortened name | `\bESP Home\b`, `\bEspHome\b`, `\besphome\b` outside code | ESPHome |
| Component names in backticks | a known component key in prose without backticks | wrap it |
| Pins left literal | `GPIO\d+` in an example for a board without fixed pins | `GPIOXX` |
| Every version and date traceable | any version or date not in `truths/esphome/` or a linked release | verify or remove |
