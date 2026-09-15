---
date: 2026-09-14
area: projects
project: home-assistant
trigger: interview
change: Drafted all Home Assistant spec files from public sources (onboard-project stage 2)
affected:
  - projects/home-assistant/
  - truths/home-assistant/proof-points.md
  - truths/home-assistant/current-release.md
by: @liam
---

# Drafted Home Assistant from public sources

Sources read: README (https://github.com/home-assistant/core/blob/dev/README.rst), home page and footer (https://www.home-assistant.io/), blog index and 2026.9 release post (https://www.home-assistant.io/blog/2026/09/02/release-20269/), help page (https://www.home-assistant.io/help/), developer documentation style guide and standards, frontend theme tokens (typography and colour), brands repository (https://github.com/home-assistant/brands), integrations page (https://www.home-assistant.io/integrations/), GitHub API (https://api.github.com/repos/home-assistant/core), Wikipedia (https://en.wikipedia.org/wiki/Home_Assistant).

Not reachable: design.home-assistant.io (app shell, no static content), the ten-year anniversary post, the foundation announcement post.

Findings for the interview:
- The home page says "over 1000 brands"; the integrations page says "thousands of brands". One approved phrasing is needed.
- The home page uses "Powerful automations", a banned word under this system. Decide whether the site changes or the word list bends for product feature names.
- Sustainability has no sourced translation yet.
- No newsletter link was found on the help page.
- Voice rules and personality attributes are inferred from one release post and the home page; they need a maintainer.
