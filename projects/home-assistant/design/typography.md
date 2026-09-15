---
area: design/typography
project: home-assistant
owner: Marketing Team
last_reviewed: 2026-09-14
review_every: 180d
draft: true
---

# Home Assistant: typography

Sourced from the frontend theme tokens (https://github.com/home-assistant/frontend/blob/dev/src/resources/theme/typography.globals.ts). These are the product UI tokens; confirm whether marketing surfaces use the same families.

## Families
| Role | Family | Fallback | Source |
|---|---|---|---|
| headings | Roboto (inherits body) | Noto, sans-serif | `--ha-font-family-heading` |
| body | Roboto | Noto, sans-serif | `--ha-font-family-body` |
| long-form | ui-sans-serif | system-ui, sans-serif | `--ha-font-family-longform` |
| code | monospace | | `--ha-font-family-code` |

## Scale
Base sizes before the user scale factor: 10, 12, 14, 16, 20, 24, 28, 32, 40 px (`--ha-font-size-xs` to `-5xl`). Weights: light 300, normal 400, medium 500, bold 700. Headings bold, body normal, actions medium. Line heights: condensed 1.2, normal 1.6, expanded 2. Mirrored in tokens.json.

## Usage
- Headings in sentence case (style.md).
- TODO: marketing and print scale; whether Roboto is the brand face or only the UI face.
