---
area: design/color
project: home-assistant
owner: Marketing Team
last_reviewed: 2026-09-14
review_every: 180d
draft: true
---

# Home Assistant: colour

Tokens are the source of truth in tokens.json; this file explains them. Sourced from the frontend theme (https://github.com/home-assistant/frontend/tree/dev/src/resources/theme/color). These are product UI tokens. Confirm in interview which shade is the brand blue for marketing (primary-50, #18bcf2, matches the long-standing logo blue; primary-40, #009ac7, is the UI primary and link colour).

## Palette
| Token | Value | Name |
|---|---|---|
| primary-05 | #001721 | primary, darkest |
| primary-30 | #006787 | primary, dark |
| primary-40 | #009ac7 | primary (UI `--primary-color`, links) |
| primary-50 | #18bcf2 | brand blue |
| primary-60 | #37c8fd | primary, light |
| primary-80 | #b9e6fc | primary, pale |
| primary-95 | #eff9fe | primary, tint |
| neutral-05 | #141414 | text primary |
| neutral-40 | #5e5e5e | text secondary |
| neutral-60 | #989898 | text disabled |
| neutral-90 | #e6e6e6 | surface lower |
| neutral-95 | #f3f3f3 | surface low |
| white | #ffffff | surface default |
| accent | #ff9800 | accent (`--accent-color`) |
| error | #db4437 | danger |
| warning | #ffa600 | warning |
| success | #43a047 | success |
| info | #039be5 | info |

## Semantic roles
| Role | Token |
|---|---|
| primary action, links | primary-40 |
| brand mark, hero accents | primary-50 (confirm) |
| text primary | neutral-05 |
| text secondary | neutral-40 |
| surface default | white |
| surface low | neutral-95 |
| accent | accent |

## Light and dark
Dark mode surfaces: background #111111, card #1c1c1c; text primary #e1e1e1, secondary #9b9b9b (`--primary-background-color`, `--card-background-color` dark overrides). Semantic surfaces default to neutral-10 in dark mode.

## Contrast
Pairs for body text (ratios to confirm with a checker; listed pairs are the product defaults):
| Foreground | Background | Ratio |
|---|---|---|
| neutral-05 #141414 | white #ffffff | about 17:1 |
| neutral-40 #5e5e5e | white #ffffff | about 5.9:1 |
| #e1e1e1 | #111111 | about 14:1 |
| white | primary-40 #009ac7 | TODO check; borderline for small text |
