---
date: 2026-09-15
area: brand/voice
project: open-home-foundation
trigger: correction
change: Two rulings on audience. The gloss rule is qualified by who the post asks something of, and the foundation may not list several projects in one post as a way of reaching all their audiences at once
affected:
  - projects/open-home-foundation/brand/voice.md
  - projects/open-home-foundation/PROJECT.md
by: @liam
---

# Who the post is for

Two corrections from drafting a single social post: an invitation to the Open Home Foundation meetup in Lisbon on 2026-09-23. Both are the same mistake in different clothes. The draft misread who it was talking to, once by explaining too much and once by speaking for people it had no standing to speak for.

## The gloss rule is qualified by audience

`brand/voice.md`, "Assume they have never heard of it", said to gloss every event, acronym, standard, product and partner on first mention. It was written absolutely, from a single broadcast rejection, and `PROJECT.md` already carried "qualify the gloss rule by audience" as open work on the grounds that glossing Zigbee to contributors reads as patronising. This settles it.

The draft read "the people who build Home Assistant, the smart home platform that runs locally in your own house". The owner cut the gloss: the people who will travel to Lisbon to meet the team already know who we are and what we stand for.

**The test is not the channel.** This post went out on the broadcast social feeds, where the original rule would have demanded the gloss. The discriminator is who the post asks something of: if the call to action only makes sense to somebody already in the community, do not gloss. A meetup invitation, a call for contributors, a beta request and a reply in a thread all take no gloss, on any channel. A post aimed at press, industry, regulators or the public still glosses everything, because reaching people without the vocabulary is the whole reason the rule exists.

This unblocks item 3 of five in `PROJECT.md`.

## The foundation does not post on behalf of several projects

The same draft was then asked to name all three flagship projects, and became "come meet the teams behind Home Assistant, ESPHome, and Music Assistant". It was caught before it shipped.

`core/voices.md`, Cross-promotion, already covers this: each project posts in its own voice about its own users' benefit, and nobody announces on somebody else's behalf. No new rule is needed at core. What was missing is that the violation does not feel like one. Listing the projects reads as generous and inclusive, which is why it gets written, and a community-facing post is where the instinct is strongest because the whole point is to gather everyone in.

So it is recorded as a named trap in the foundation's `## Never`, with the worked example, rather than left as an inference from core.

The fix is four posts, not one. The foundation invites people to its own event in its own voice and names no projects; each project invites its own community in its own voice. This is more work and it is the point: a single post reaching four audiences is the shortcut the cross-promotion rule exists to prevent.

## What this exposed elsewhere

Writing the three project posts showed what is actually buildable today. Home Assistant is `live` with `ready: [brand]` and a confirmed `voice.md`, so its post is a real draft, though `examples/home-assistant/` holds only release posts and no social examples, so its social register is still unevidenced. ESPHome and Music Assistant are `registered`, their `brand/voice.md` files are unfilled TODO stubs, and neither has an examples directory. Their posts were built from `core/voices.md` and public sources only, and read generically because there is nothing project-specific to build from.

That is not a blocker for this pull request. It is the cost of the ruling, and it lands on the two projects nobody has interviewed yet.
