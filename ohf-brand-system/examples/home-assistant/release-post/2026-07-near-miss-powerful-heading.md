---
type: release-post
project: home-assistant
date: 2026-07-01
source_url: https://www.home-assistant.io/blog/2026/07/01/release-20267/
mode: Medium
near_miss: true
pending_review: true
why_it_works:
  - Shows a banned word reaching production in a heading, where the pressure to be short makes it tempting
  - The fix is already in the post's own body text, which proves the specific version fits a heading
tags: [release, heading, banned-words]
---

# Near-miss: "Creating automations just became easier, natural and more powerful"

## Context
Section heading in the 2026.7 release post. Identified as a near-miss by @liam in interview 2026-09-14: a heading with a meaningless word that says nothing for the user. Everything else about the post is an example (see `2026-07-release-20267.md`).

## The work
Heading as published: "Creating automations just became easier, natural and more powerful".

## What was wrong
"Powerful" is on the banned list because it describes nothing. "Easier" and "natural" are adjectives without a subject. The heading tells the reader that something is better without saying what they can now do. The post's own body has the specific version: automations now "start from what you actually want your home to do."

## The fix
Heading rewritten to the specific thing, in the post's own words:
- Yes: "Start automations from what you want your home to do"
- No: "Creating automations just became easier, natural and more powerful"

## What to copy
- When a heading reaches for "powerful", look in the section's first paragraph; the specific claim is usually already there.
- Headings state the outcome or the opinion (see 2026.8: "Your entity IDs, your choice").

## What not to copy
- The published heading.
