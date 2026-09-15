---
area: brand/style
project: home-assistant
owner: Marketing Team
last_reviewed: 2026-09-14
review_every: 180d
draft: false
---

# Home Assistant: style

Mechanics. Two guides govern Home Assistant writing (interview 2026-09-14):

| Guide | Governs | Location |
|---|---|---|
| OHF Editorial Style Guide (draft v1, owners Cassidy and Gemma) | communications content: marketing copy, social, blog, email, announcements | https://docs.google.com/document/d/15OKslXJI7ViOFQs_ujM224psyZ8KOI2eOws-uC1NZOU/edit |
| Microsoft Writing Style Guide | everything the editorial guide is silent on | https://learn.microsoft.com/en-us/style-guide/welcome/ |
| Developer documentation style guide | documentation and developer docs | https://developers.home-assistant.io/docs/documenting/general-style-guide and https://developers.home-assistant.io/docs/documenting/standards |

Precedence (editorial guide, Overview): for communications content, the editorial guide first, then Microsoft, then ask in #marketing-comms and log the decision in the guide's "Maintaining this guide" section. For content that blends both, such as a blog post explaining a technical feature, use the editorial guide for voice and tone and defer to the developer guide for exact terminology, commands and instructions. Bracketed placeholders in the editorial guide are unsettled and are not rules.

Most rules below were first drafted from the developer guide. Each is marked with where it now traces: (editorial) settled in the OHF guide; (Microsoft) the fallback; (developer) documentation only, confirm for prose.

## Spelling and grammar
- Spelling convention: US English, for spelling, punctuation and grammar (editorial, Base standard).
- Serial comma: yes (Microsoft; also developer).
- End sentences with a period (developer; consistent with Microsoft).
- Avoid em dashes; split the sentence or use a colon (developer; Microsoft allows them sparingly, confirm for prose).
- Inclusive and accessible language (editorial section exists, empty; Microsoft bias-free communication applies meanwhile).

## Capitalisation
- Headings: sentence case (Microsoft; also developer).
- Brand and product names: match the official capitalisation exactly ("Z-Wave", never "Zwave").
- Product and feature names: see naming.md.
- UI elements in prose: bold, and use "select" rather than "click" except for specific mouse actions such as right-click.
- Placeholders: capitals with underscores, `YOUR_API_KEY`.

## Numbers and dates
- Version numbers: `YYYY.M` for monthly releases, `YYYY.M.x` for patches. Example: 2026.9, 2026.9.2. (Observed from release posts; confirm.)
- Dates (Microsoft, Date and time terms): month day, year, as in "September 2, 2026". No ordinals. Do not abbreviate the month unless space is extremely limited; when it is, use the three-letter form with no period: Jan, Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, Dec. Include the year in the standard form; drop it only where space forces the abbreviated form.
  - Yes: "September 23, 2026"; in a cramped social caption, "Sep 23"
  - No: "Sept 23rd"; "23 September 2026"
  - Note for the editorial guide: the last social post used "Sept". Microsoft's form is "Sep". Either the editorial guide records "Sept" as a deliberate departure, or "Sep" is the rule. Until decided, agents use the full month name and avoid the question.
- Times (Microsoft): numerals with AM or PM in capitals, preceded by a space: "10:45 AM". Include the time zone for anything people beyond one zone will attend, as "Central European Time (UTC+1)"; never bare GMT.
- A date is only a date when it is in a linkable source. A date agreed in conversation is a plan, not a fact, and is not published (interview 2026-09-14: the last social post carried an assumed date that turned out wrong).
- Units: metric (interview 2026-09-14). Numerals for all measurements, even under 10. A space between the number and the unit; hyphenate when the measurement modifies a noun. Abbreviations only with numerals and never followed by a period. Commas in numbers of four or more digits, except years and pixels. Degrees as ° for temperature (Microsoft, Units of measure).
  - Yes: "3 cm", "a 13.5-inch display", "1,093 MB", "21 °C", "1920 × 1080 pixels"
  - No: "3cm", "3 cm.", "1093 MB", "21 degrees C", "1920x1080px"

## Formatting
- Links: descriptive text, never bare URLs, never affiliate or tracking links.
- Code, file paths, filenames, variables and text to type: backticks.
- Emphasis: italics with underscores; never ALL CAPITALS.
- Lists: `-` for unordered; increasing numbers for ordered.
- Tables: avoid in docs; use lists (developer only; release posts use tables, so this does not carry to prose).
- Images: descriptive alt text always.
- Integration and platform names link to their documentation page on first mention.

## Glossary
Terminology from the documentation glossary (`source/_data/glossary.yml` in the home-assistant.io repository, read 2026-09-14). Definitions are the glossary's first sentence. Use the term as written; the Not column lists what public writing avoids. The editorial guide's own glossary is empty in draft v1 apart from one intent: avoid "firmware" and offer alternatives; add that row when it is settled.

| Term | Use | Not |
|---|---|---|
| integration | connects Home Assistant with devices, services and more | plugin, component, connector |
| add-on | a Supervisor-managed application installed alongside Home Assistant | plugin, extension, app |
| entity | represents a sensor, actor or function | object, item |
| device | a physical or logical unit that contains entities | gadget, thing |
| automation | connects triggers to actions, "when trigger then do action" | rule, routine |
| trigger, condition, action | the three parts of an automation, in that order | event, filter, task |
| script | a sequence of actions run by Home Assistant | macro |
| scene | captures the states you want certain entities to be | preset, mode |
| blueprint | a script, automation or template with configurable parts | template (for this meaning) |
| helper | a virtual entity not backed by a physical device | virtual sensor |
| area | a logical grouping representing a room or space | room (in UI copy) |
| zone | a region on a map | geofence |
| dashboard | the UI you build to display and control your home | panel, Lovelace (retired name) |
| Home Assistant Core | the Python program at the heart of Home Assistant | HA Core, hass |
| Home Assistant Operating System | the embedded OS that runs the Home Assistant ecosystem | HassOS, Hass.io |
| Home Assistant Container | standalone container-based installation of Core | Docker version |
| Assist | the built-in voice assistant | voice assistant (generic), Alexa-style comparisons |
| Matter | open standard for controlling smart home devices over Wi-Fi or Thread | Matter protocol (redundant) |
| Thread | low-power mesh networking standard | Thread network (unless the network itself is meant) |
| Z-Wave, Zigbee | brand capitalisation as shown | Zwave, ZigBee |

## Machine checks
Rules an agent or script can apply to any draft before a human sees it. Skills run these in their review step.
| Check | Pattern | Fix |
|---|---|---|
| No ordinals in dates | `\b\d{1,2}(st\|nd\|rd\|th)\b` near a month name | remove the suffix |
| No "e.g." | `\be\.g\.` | for example, such as |
| No "click" for UI | `\bclick\b` outside "right-click" | select |
| No banned words | list in core, see messaging.md | the specific thing |
| Every date traceable | any date not present in `truths/home-assistant/` or a linked source | verify or remove |
