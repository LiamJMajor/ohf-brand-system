---
standard: integration-brand-assets
title: Integration brand assets
scope: project
conformance: none
status: active
area: standards/integration-brand-assets
project: home-assistant
owner: Marketing Team
last_reviewed: 2026-09-14
review_every: 180d
draft: false
---

# Standard: integration brand assets

Scope: project. Owned by Home Assistant. Governs the icons and logos of brands Home Assistant integrates with, served from brands.home-assistant.io. Source: https://github.com/home-assistant/brands. A candidate for promotion to shared if ESPHome or Music Assistant adopt the same rules.

## Rules
- PNG only, losslessly compressed, interlaced and transparent preferred, optimised for a white background; dark variants prefixed `dark_`.
- Trimmed to minimum empty space at the edges.
- Icons: 1:1, 256x256 (512x512 for @2x).
- Logos: landscape preferred, respect the brand's real aspect ratio; shortest side 128 to 256 px (256 to 512 for @2x).
- Filenames: `icon.png`, `dark_icon.png`, `logo.png`, `dark_logo.png` and their `@2x` variants, in `core_integrations/<domain>/`, `custom_integrations/<domain>/` or `thread_brands/`.
- All trademarks remain the property of their owners.
