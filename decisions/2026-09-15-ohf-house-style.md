---
date: 2026-09-15
area: brand/style
project: open-home-foundation
trigger: interview
change: House style settled for the foundation voice — US English everywhere including this repository, serial comma always including in the thread, and strong language permitted where it is earned
affected:
  - projects/open-home-foundation/brand/style.md
  - projects/open-home-foundation/brand/voice.md
  - core/story.md
by: @liam
---

# Open Home Foundation house style

Three mechanics rulings from the onboarding interview on 2026-09-15. All three existed as contradictions in the wild before the interview; an agent had no way to resolve any of them from the repository.

## US English, output and repository
Published copy has always been US English ("anonymized", "organizations", "monetization"). The brand system's own core files were written in UK English. Rather than maintain the split, US English is now the standard for both, so an agent reading a core file and an agent copying published boilerplate get the same answer.

Not yet done: the UK spellings still in `core/` ("criticises", "organisation", "recognisable"). That is a mechanical sweep across core plus the Home Assistant project files, and it touches files owned by the marketing team, so it travels as its own pull request rather than riding along with this onboarding. Until it lands, `brand/style.md` tells agents to trust the rule over the spelling in front of them.

## Serial comma, including in the thread
Every public surface writes "privacy, choice, and sustainability". `core/story.md:19` wrote the thread without the serial comma, which made the single most repeated line in the system inconsistent with every place it actually appears. The thread was corrected, not the website.

This is a core change made in a project onboarding branch. It is one character, it moves core toward published reality rather than away from it, and the core owner is the same person who made the ruling — but it is still a core change, and the reviewer should confirm it deliberately rather than let it pass as a typo fix.

## Strong language, where it is earned
The IFA 2026 post reproduced a cross-stitch reading "fuck VCs and private equity" in foundation voice on the foundation's own blog. The ruling is that this is house voice, not an outlier, and it extends past quoting artefacts to the foundation's own sentences.

The limit is that the profanity has to carry the argument. "fuck VCs and private equity" names the exact outcome the foundation's legal structure exists to prevent. Profanity as intensifier does no work and is out. Sanitising for respectability (asterisks, "[expletive]") is specifically out, because it concedes the point the language is making. See the amendment below, which narrows this for social channels on distribution grounds rather than editorial ones.

Scoped to the foundation voice only. Project voices inherit nothing here; a project wanting the same latitude writes it into its own `voice.md`.

### Amended the same day: censoring on social
On social channels the word is written "f\*ck". The original ruling said no asterisks anywhere, and this narrows it.

The two rulings do not conflict, because they answer different questions. The interview ruling was about editorial nerve: do not soften the foundation's language to sound respectable. This amendment is about distribution: a platform may down-rank a post carrying profanity, and a post nobody sees makes no argument at all. Softening for courage is still banned. Softening to get through a ranking filter is permitted, on social only.

The basis is explicitly unverified, and was flagged as such by the person who made the call. No test has been run here; platform behaviour differs between organic and promoted reach and changes without notice. `brand/style.md` records what would settle it — the same post censored on one network and uncensored on another with comparable audiences — so that this is revisited rather than quietly inherited as fact.

Worth noting the cost. The foundation's argument at IFA was partly carried by refusing the conventions of the category it was in. Accepting a platform's convention to get reach on that platform is the same trade in the other direction, made deliberately.
