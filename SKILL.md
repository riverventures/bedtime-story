---
name: bedtime-story
description: Generate personalized bedtime stories where a child is the hero, with age-calibrated writing, character-consistent illustrations, and a printable landscape picture-book PDF. Use when the user asks for a bedtime story, kids story, personalized story, story for a child, illustrated children’s story, bedtime book, nightly story routine, or wants to reuse a saved child profile for repeat story generation.
---

# bedtime-story

Generate one bedtime story at a time. Keep the skill focused on: child profile → story plan → short age-appropriate story → consistent illustrations → printable PDF.

## Workflow

1. Collect or reuse the child profile.
2. Ask only for tonight’s theme if the profile already exists.
3. Plan the story first: title, page count, one beat per page, and one final line per page.
4. Build a single character anchor string for the child.
5. Generate one hero reference image.
6. Generate one illustration per page using the same anchor string and the hero reference.
7. Assemble a landscape PDF.
8. Run a final quality check for page count, tone, and duplicate-character errors.

Read `references/workflow.md` before executing the full run.

## Child profile

Collect and reuse:
- name
- age
- appearance: hair, skin tone, eyes, distinguishing features, default outfit
- favorite things
- recurring family members who may appear
- fears or themes to avoid

If the parent already has a saved profile, only ask what the child wants to be or do tonight.

## Character consistency

This is the fragile part.

- Build one anchor string and reuse it verbatim in every illustration prompt.
- Generate a single hero reference image before page illustrations.
- Pass the hero reference into every page generation call.
- Add an anti-duplication guardrail to every prompt.

Read `references/image-prompts.md` when generating images.
Use `scripts/prepare_story_inputs.py` when it helps normalize the profile, anchor string, and cleaned story lines instead of recreating those helper artifacts manually.

## Story writing

Keep the story strongly age-calibrated and lock the page beats before generating page art.

- For toddlers, optimize for short lines, sensory detail, repetition, familiar people, and a calm ending.
- Keep the child active, not passive.
- End in sleep, calm, cuddles, or winding down.

Read `references/story-rules.md` before writing the story.

## Output

Default output is a printable landscape picture-book PDF:
- illustration-heavy page
- one short line of text per page
- full-bleed image treatment

Use `scripts/assemble_storybook.py` to assemble the final PDF instead of rewriting the image-cropping and page-layout logic each time.

Example:

```bash
python scripts/assemble_storybook.py \
  --images-dir out/pages \
  --text-file out/story-lines.txt \
  --output out/story.pdf \
  --font-path /path/to/font.ttf
```

## Guardrails

- Default to gentle, bedtime-safe material.
- Respect the parent’s avoid list.
- Do not introduce scary, dark, or high-conflict elements unless explicitly requested for older kids.
- Do not hardcode a specific Gemini image model name in the skill instructions; use the current configured image model.
- Keep requests and outputs one story at a time unless the user explicitly asks to compile a book.

## Optional extensions

- Generate narration audio if the environment has a TTS tool.
- Compile multiple completed stories into one larger storybook when the parent asks.
