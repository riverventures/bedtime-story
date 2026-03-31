# 🌙 bedtime-story

Personalized bedtime stories where your kid is the hero. An [OpenClaw](https://github.com/openclaw/openclaw) skill.

## What it does

Your kid picks who they want to be tonight. The AI writes a story with them as the main character, generates an illustration, and gives you a printable page. Over time, you build a physical storybook together.

```
"Nina wants to be a princess tonight"
```

→ 3-minute story where Princess Nina rescues a sleepy bunny, plus a watercolor illustration, delivered as a printable A4 PDF.

## Install

```bash
openclaw skill add riverventures/bedtime-story
```

## Features

- **Your kid is the hero.** Every story uses their real name and puts them at the center.
- **Age-calibrated.** Under 2: simple sensory stories, 200 words. Ages 3-5: problem-solution arcs, silly humor. Ages 6+: real narrative with twists.
- **Character picker.** Princess, superhero, astronaut, pirate, dinosaur rider, scientist, chef — or anything they dream up.
- **Illustrated.** Each story gets a matching illustration (watercolor, Pixar-style, or coloring page).
- **Printable.** A4 PDF with illustration + story text. Print nightly, collect into a book.
- **Continuity mode.** Same magical world across nights. Recurring characters. "Remember when Nina found the golden key?"
- **Voice narration.** Optional audio version via ElevenLabs or system TTS.
- **Always ends with sleep.** These are bedtime stories. They're engineered to make kids want to close their eyes.

## Quick Start

First time: tell me your child's name, age, and favorite things. I'll save the profile.

Every night: just tell me who they want to be. I handle the rest.

## Storybook Builder

After a few weeks of nightly stories, ask me to compile them into a book:

```
"Compile Nina's storybook"
```

→ Multi-page PDF with cover page, all stories and illustrations, ready to print and bind.

## Examples

| Request | Output |
|---|---|
| "Nina wants to be a princess" (19mo) | 200-word sensory story, sleepy bunny, watercolor illustration |
| "Liam wants to be an astronaut" (4yr) | 500-word adventure on Planet Banana, silly aliens, full color illustration |
| "Maya wants to be a detective" (7yr) | 1000-word mystery in her school, plot twist, pencil sketch illustration |

## Requirements

- Google API key (Gemini for story illustration)
- Python 3.9+ with Pillow (for PDF generation)
- Optional: ElevenLabs API key (for voice narration)
- Optional: printer for nightly printouts

## Why this exists

A dad on Reddit has his kids pick heroes each night. His daughter picks a princess, his son picks a superhero. AI generates a story where they ARE those characters. He prints each story with an illustration, and the kids build their own physical storybooks.

I thought every parent should be able to do this. Now they can.

## License

MIT
