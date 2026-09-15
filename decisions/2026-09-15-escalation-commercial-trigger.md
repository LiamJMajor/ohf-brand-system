---
date: 2026-09-15
area: escalation
project: core
trigger: correction
change: The commercial-boundary escalation trigger now fires on the ask, not on the noun — naming hardware is no longer a trigger; a price, store link, buy call or launch claim is
affected:
  - core/escalation.md
by: @liam
---

# Commercial boundary: the trigger is the ask, not the noun

## What was wrong
The trigger read "Foundation voice and a product, hardware, merch or store item in one output". Taken literally it fires on any sentence naming a product, which made the IFA 2026 post a violation for saying what the booth ran on — "a single Home Assistant Green using two ZBT-2s", five Voice Preview devices running Sendspin via Music Assistant.

That post is not a commercial push. It is the foundation demonstrating that the open home works, using the hardware that exists. The rule it was breaking was the rule's wording, not its intent. `core/voices.md`, Commercial boundary, is about fronting a commercial push and about advocacy and selling sharing a post; it was never about the nouns.

A trigger that fires on correct work is worse than no trigger, because people learn to route around it. This one was already producing that effect: it fired on the IFA social drafts and would have stripped the most concrete evidence in the story.

## What it says now
The trigger is a call to buy, a price, a store or product link, or a launch claim. All four are observable in the draft, which is what `core/escalation.md` requires of a trigger — the previous wording was observable too, it was just observing the wrong thing.

The foundation may say what it ran, built or tested on. It may not ask anyone to buy it. A launch belongs to the project whose brand is on the box, in that project's voice and channels, per the brand licence.

## What this does not change
`core/voices.md`, Commercial boundary, is untouched. The foundation still never fronts a commercial push, and advocacy and selling still never share a post. Only the checkable trigger that implements it has changed.
