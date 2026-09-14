# Interview protocol for capturing judgment

Use this when sitting with a designer, writer, comms lead or founder to turn what they know into files an agent can follow. The aim is decisions and their reasons, not adjectives.

## Setup
- Tell them the goal: "I want to write down the calls you make automatically, so other people and tools make the same calls without asking you."
- Have three or four recent pieces of real work open: one they are proud of, one they had to fix, one someone else made without them.

## Rounds

### Round 1: The fix
Start with the piece they had to fix. Ask, for each change they made: what was wrong, what did you change it to, would you make that change every time or only here? Every "every time" answer is a rule. Every "only here" answer is context that belongs in an example, not a rule.

### Round 2: The contrast
For each rule from round 1, ask for the opposite. "Show me the version you would reject." Write the pair down verbatim. A rule with a contrast pair is worth five rules without.

### Round 3: The boundary
Ask: "When do you break this rule?" and "What would you never let a tool do without you?" The first gives you modes. The second gives you escalation rules. Push on the second until you get specific triggers: audience, channel, topic, stakes.

### Round 4: The proud piece
Ask for a link first. "Proud of everything" is a common answer and not a selection; do not ask why until a specific piece is on the table. If they cannot pick, propose two recent pieces yourself and ask which is closer to the bar. Then ask what makes it work. Push past "the tone" to observable things: word choice, structure, what it leaves out, what it opens with. These become `why_it_works` entries.

### Round 5: The stranger's piece
The one made without them. Ask what they would change and why. Compare with round 1. Repeated answers are your highest-confidence rules.

### Round 6: The queue
Ask: "What do people ask you for that you could do in your sleep?" List them. For each, ask whether it is one artefact or a beat with several; a beat becomes a skill family (see codify-workflow). Each is a candidate for `codify-workflow`. Ask which one they would most like to never touch again.

## Writing it up
- Rules go into `foundation/` or `brands/<brand>/` with the contrast pair inline.
- Boundaries go into `foundation/escalation.md` as trigger → route.
- Proud pieces become entries for `harvest-examples`.
- The queue becomes a prioritised list for `codify-workflow`.
- Log the interview in `decisions/` with the date and who was interviewed.

## Signs you are getting adjectives instead of decisions
- The rule could apply to any company.
- You cannot write a contrast pair for it.
- The expert says "it depends" without saying on what.
When this happens, go back to a specific piece of work and ask about a specific sentence or element.
