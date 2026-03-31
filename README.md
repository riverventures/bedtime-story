# 🌙 bedtime-story

Personalized bedtime stories where your kid is the hero. An [OpenClaw](https://github.com/openclaw/openclaw) skill.

## What it does

Your kid picks who they want to be tonight. The AI writes a story with them as the main character, generates character-consistent watercolor illustrations, and gives you a printable landscape picture book. Over time, you build a physical storybook together.

```
"Nina wants to be friends with a flamingo tonight"
```

→ 9-page landscape picture book where Nina meets a flamingo by the pool, with her Nani tucking her in at the end. Full-bleed watercolor illustrations, one line of story per page.

## Install

```bash
openclaw skill add riverventures/bedtime-story
```

## Features

- **Your kid is the hero.** Every story uses their real name and puts them at the center.
- **Character-consistent illustrations.** Describe your child once — hair, skin, eyes, outfit. The skill generates a hero reference image and passes it to every page so your kid looks the same throughout.
- **Age-calibrated.** Under 2: simple sensory stories, 8-10 pages, one line each. Ages 3-5: problem-solution arcs. Ages 6+: real narrative with twists.
- **Landscape picture book format.** Full-bleed illustration fills 90% of each page. One line of story at the bottom. Looks like a real children's book.
- **Family members included.** Describe grandma, grandpa, siblings, pets — they appear as recurring characters.
- **Printable.** Landscape A4 PDF. Print, staple, done.
- **Anti-duplication guardrails.** Built-in prompt engineering to prevent the AI from cloning your child in the same illustration.
- **Voice narration.** Optional audio version via ElevenLabs.
- **Always ends with sleep.** Engineered to make kids want to close their eyes.

## First Time Setup

Tell me about your child:

```
Name: Nina
Age: 19 months
Hair: straight, short, dark brown
Skin: light olive
Eyes: big, dark brown
Features: tiny gold stud earrings
Default outfit: light pink dress with white flowers
Favorites: birds, flamingos, cats, pool, tomatoes
Family:
  - Nani (grandmother): Indian, early 50s, dark brown hair, blue cardigan and jeans
  - Nanu (grandfather): [description]
  - Masie (aunt): [description]
Avoid: nothing scary, no loud noises
```

After that, every night just say who they want to be.

## Output

| Feature | Detail |
|---|---|
| Orientation | Landscape (11 x 8.5 in) |
| Illustration | 90% of page, full-bleed, watercolor |
| Text | 10% bottom strip, Georgia 42pt, black on white |
| Pages | 8-10 (under 2), 10-15 (older) |
| Format | Multi-page PDF |
| Character consistency | Hero reference image + anchor string on every page |

## How Character Consistency Works

1. You describe your child's appearance once
2. The skill generates a **hero reference image** — a front-facing portrait in the story's art style
3. That reference image is passed as input to **every page generation** alongside the scene prompt
4. An identical character description (anchor string) is included in every prompt
5. Anti-duplication guardrails prevent the model from rendering the child twice

This isn't perfect — AI image generation still has drift. But it's significantly better than generating each page independently.

## Examples

| Request | Output |
|---|---|
| "Nina wants to be friends with a flamingo" (19mo) | 9 pages, pool party, Nani tucks her in |
| "Liam wants to be an astronaut" (4yr) | 12 pages, discovers Planet Banana, silly aliens |
| "Maya wants to be a detective" (7yr) | 15 pages, solves mystery at school, plot twist |

## Requirements

- Google API key (Gemini for illustrations)
- Python 3.9+ with Pillow (for PDF assembly)
- Optional: ElevenLabs API key (voice narration)
- Optional: printer for nightly printouts

## Why this exists

A dad on Reddit has his kids pick heroes each night. His daughter picks a princess, his son picks a superhero. AI generates a story where they ARE those characters. He prints each story with an illustration, and the kids build their own physical storybooks.

I thought every parent should be able to do this. Now they can.

## License

MIT
