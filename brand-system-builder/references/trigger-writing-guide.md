# Writing skill descriptions that trigger correctly

The `description` in a skill's frontmatter is the only thing in context before the skill loads. It decides whether the skill fires. Most skill failures in practice are trigger failures: the skill exists but never loads, or two skills load for one request.

## Structure
1. **What it does**, one sentence, verb first.
2. **When to use it**: the phrases and situations that should invoke it. Include casual phrasings, not just the formal name.
3. **When not to use it**, if a sibling skill is close. Name the sibling.

## Be slightly pushy
Models under-trigger. Write "Use this whenever someone mentions a release, a changelog, 'what's new', or asks for an announcement, even if they don't say 'blog post'." rather than "Use for release posts."

## Keep siblings apart
If `write-release-post` and `write-feature-short` both exist, each description names the other and states the boundary: length, audience, or channel.

## Test it
Before shipping, list ten realistic requests: six that should trigger this skill, four that should not. Check which skills would fire for each. Tighten until the six fire and the four do not. Record the ten in the skill's `evals/cases.md` under a `## Trigger cases` heading so the audit can re-run them.

## Anti-patterns
- Descriptions that only restate the name.
- "Use for anything brand related." That fires for everything.
- Putting "when to use" in the body instead of the description. The body is not loaded until after the decision is made.
