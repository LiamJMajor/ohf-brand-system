---
area: brand/story
project: esphome
owner: @liam
last_reviewed: 2026-09-16
review_every: 180d
draft: true
---

# ESPHome: story

What a writer needs for an about page, a backgrounder or a talk intro. Drafted 2026-09-16 from the contributors page, the changelog and the 2026 blog. Thin on the early years by design: the public sources carry the rename and the versioning change, and almost nothing else that is dated and citable. The interview is where the first five years come from.

## Origin
ESPHome was originally founded by Otto Winter (https://esphome.io/guides/supporters/). It began as two projects: esphomelib, a C++ library, and esphomeyaml, the YAML layer on top of it. The v1.10.0 release folded them into one name and put the YAML at the centre, on the reasoning that "the name esphomelib and esphomeyaml were too technical, and this project has changed a lot since the first published release (the yaml part didn't even exist back then)" (https://esphome.io/changelog/v1.10.0/). The same release deprecated writing against the core framework in C++ directly. That decision is the shape of the project ever since: you describe, ESPHome builds.

The LICENSE carries a 2019 copyright and splits the project along the same seam: the C++ and runtime code is GPLv3, the Python and everything else is MIT (https://github.com/esphome/esphome/blob/dev/LICENSE).

TODO: founding year and the handover from Otto Winter to the current maintainers. The v1.15.0 changelog opens "Stop! this is not Otto Winter, but Guillermo Ruffino" (https://esphome.io/changelog/v1.15.0/), which dates the change to somewhere around that release but does not date the release. Interview, or a dated tag, settles it.

## Milestones
| Date | Milestone | Source |
|---|---|---|
| TODO | First public release, as esphomelib and esphomeyaml | TODO: no dated source found |
| TODO (v1.10.0) | Renamed to ESPHome; YAML becomes the primary way to use it | https://esphome.io/changelog/v1.10.0/ |
| TODO (v1.15.0) | Maintenance passes from Otto Winter to Guillermo Ruffino | https://esphome.io/changelog/v1.15.0/ |
| 18 August 2021 | Calendar versioning begins with 2021.8.0, on a monthly cycle | https://esphome.io/changelog/2021.8.0/ |
| TODO | ESPHome becomes an Open Home Foundation project | TODO: badge present in the README, no date found |
| April 2026 | ESPHome Starter Kit shown at State of the Open Home 2026 | https://esphome.io/blog/2026/08/12/the-esphome-starter-kit-is-here/ |
| 17 June 2026 (2026.6.0) | ESPHome Device Builder replaces the retired dashboard | https://esphome.io/blog/2026/06/17/esphome-2026-6/ |
| 2 July 2026 | The ESPHome blog opens, as a register distinct from the changelog | https://esphome.io/blog/2026/07/02/unbox-your-creativity-with-the-esphome-device-builder/ |
| 4 August 2026 | ESPHome Desktop App, for Windows, macOS and Linux | https://esphome.io/blog/2026/08/04/simplify-your-esphome-setup-with-the-new-desktop-app/ |
| 12 August 2026 | ESPHome Starter Kit ships: the project's first official product, with Apollo Automation | https://esphome.io/blog/2026/08/12/the-esphome-starter-kit-is-here/ |
| 19 August 2026 | 2026.8.0: 348 pull requests from over 40 contributors | https://esphome.io/blog/2026/08/19/esphome-2026-8/ |

Dates above are the publication dates of the posts and changelog entries cited, which for a release is the release date. The three TODO rows are the ones that matter most for an about page and none of them could be sourced.

## People
- **Otto Winter** ([@OttoWinter](https://github.com/OttoWinter)), founder. Named on the contributors page; not visible in recent public activity.
- **Jesse Hills** ([@jesserockz](https://github.com/jesserockz)), described on the site as ESPHome Developer, and the author of the release posts.
- **Paulus Schoutsen** ([@balloob](https://github.com/balloob)), President of the Open Home Foundation, who writes the first-party product announcements on the ESPHome blog.
- **Darren Griffin** ([@mrdarrengriffin](https://github.com/mrdarrengriffin)), Web Developer, and **Missy Quarry** ([@missyquarry](https://github.com/missyquarry)), Community Manager, both listed as ESPHome blog authors.
- The contributors page lists over 2,300 people who have had a patch merged into an ESPHome organisation repository (https://esphome.io/guides/supporters/). A single release draws from dozens: 2026.8.0 named over 40.
- Titles above are taken from the blog author list as published. Names are already public in that capacity; anything beyond them needs consent before it is written down.

TODO: how the project describes its own community in its own words. Home Assistant has "a worldwide community of tinkerers and DIY enthusiasts" in its README. ESPHome's README carries no equivalent sentence, and the closest published phrasing is the home page's "thousands of makers already using ESPHome".
