# Writing messaging.md

The messaging hierarchy is how a project's story stays the same whether it appears in a tweet, a release post or a press quote. It is a hierarchy because each level derives from the one above, and the top is not in the project at all: `core/story.md` and `core/pillars.md` sit above positioning. A project's positioning is its reading of the shared story; its pillar translations are its reading of the shared pillars. An agent writing a social post reads the boilerplate; an agent writing a landing page reads key messages; both trace back to the same positioning.

## Positioning
One or two sentences. For whom, what it is, why it matters, what makes it different. Not a tagline. Test: could you swap in a competitor's name and have it still be true? If yes, it is not positioning.

- Weak: "Home Assistant is a powerful open source home automation platform."
- Usable: "Home Assistant is the open source home automation platform for people who want their home to work for them, not for a vendor. It runs locally, connects devices from any maker, and puts every decision about data in the hands of the person who lives there."

## Pillar translations
One `###` per pillar the project serves, from `PROJECT.md`. Each translates the foundation's belief into what this project concretely does about it. This is where the shared core becomes product benefit, and it is the mechanism that keeps hundreds of projects pulling in the same direction.

```
### Privacy
Home Assistant runs entirely on hardware in your home. Cloud services are optional add-ons you turn on. Nothing about your home leaves it unless you send it.
```
A translation that could be written for any project is not a translation. Name the feature, the default, the behaviour.

## Key messages
One `###` per audience in `audiences.md`. Two or three sentences each: what this audience should believe after hearing from us, in terms of what they care about. Derived from positioning and pillar translations; never a new claim.

## Boilerplate
Three fixed lengths, written once, reused verbatim. Agents copy these rather than paraphrasing, so they stay identical across channels.
- `### One line`: under 20 words. The sentence after the project name in any article.
- `### 50 words`: the social bio, the footer, the partner listing.
- `### 100 words`: the press release boilerplate, the about page.

Every fact in boilerplate traces to `truths/<slug>/proof-points.md`. No banned words.

## We don't say
Words, framings and comparisons this project avoids, each with the replacement. Criticising other companies by name is always on this list for project voices; that belongs to the foundation voice per `core/voices.md`.

## For stewarded projects
Only Positioning and Boilerplate are required. Write them from the README and the repo description, mark the file `draft: true` in frontmatter, and move on. The validator accepts this for the stewarded tier.
