---
name: bedtime-story
description: Generate personalized bedtime stories where your child is the hero. Provide their name, age, appearance, interests, and a character they want to be — the skill writes an age-appropriate story, generates character-consistent illustrations, and outputs a printable landscape picture book PDF. Over time, kids build their own physical storybook. Use when the user asks for a bedtime story, kids story, personalized story, story for my child, or story with my kid as the character.
---

# bedtime-story

Personalized bedtime stories where your kid is the hero. One story per night, illustrated, printable.

## How It Works

1. Parent provides: child's name, age, appearance, and who they want to be tonight
2. Skill generates a hero reference image for character consistency
3. Writes a 3-5 minute bedtime story with the child as the main character
4. Generates one illustration per story beat, passing the hero reference to each
5. Outputs a landscape picture book PDF: full-bleed illustration (90%) + text strip (10%)
6. Over time, pages collect into a physical storybook

## Setup (First Use)

Ask the parent for a **character profile** (store this, reuse every night):

```
Child's name:
Age:
Appearance:
  Hair: (color, length, style)
  Skin: (tone)
  Eyes: (color)
  Distinguishing features: (earrings, birthmark, glasses, etc.)
  Default outfit: (what they usually wear — used unless the story character has a costume)
Favorite things: (animals, topics, foods, activities)
Family members who may appear:
  - Name, relationship, appearance description, clothing style
  - Name, relationship, appearance description, clothing style
Any fears to avoid: (monsters, dark, loud noises, etc.)
```

Save this so subsequent requests only need: "What does [name] want to be tonight?"

### Character Anchor String

From the profile, build an **anchor string** — an identical character description used in EVERY illustration prompt, word for word:

```
"A [age] toddler girl/boy with [hair], [skin], [eyes], [features], wearing [outfit]."
```

Example:
```
"A 19-month-old toddler girl with straight short dark brown hair just past her ears, light olive skin, big dark brown eyes, chubby toddler cheeks, tiny gold stud earrings, wearing a light pink dress with small white flowers, bare feet."
```

Do the same for recurring family members:
```
"Nani is Nina's grandmother — an Indian woman in her early 50s, youthful-looking, with dark brown hair with only subtle highlights, wearing a soft blue cardigan over a white top and jeans. Warm and stylish."
```

## Character Consistency

This is the most important technical challenge. Follow these steps in order:

### Step 1: Generate Hero Reference Image

Before generating any story pages, generate a single character reference image:

```
Generate a character reference sheet for a children's picture book character.
[FULL CHARACTER ANCHOR STRING]
Show them from the front, smiling warmly at the viewer. Simple warm beige background.
Soft watercolor children's book illustration style. This is the CHARACTER REFERENCE
that will be used for all pages of a bedtime story picture book.
```

Save this image. It will be passed as an `inlineData` input to every subsequent page generation.

### Step 2: Pass Reference to Every Page

Every illustration generation call must include:
1. The hero reference image as `inlineData` (first part)
2. The prompt with the full anchor string (second part)

```json
{
  "contents": [{"parts": [
    {"inlineData": {"mimeType": "image/jpeg", "data": "<HERO_REF_BASE64>"}},
    {"text": "<PAGE_PROMPT_WITH_ANCHOR_STRING>"}
  ]}]
}
```

### Step 3: Anti-Duplication Guardrail

**CRITICAL:** When passing a reference image, the model often renders the character twice — once from the reference and once from the prompt. Every prompt MUST include:

```
IMPORTANT: There is ONLY ONE [CHILD NAME] in this image. Do NOT duplicate the main character.
Only [N] people in this image: [list each by name and role].
```

For carried/held scenes:
```
Only TWO people: [ADULT] (holding [CHILD]) and [CHILD] (being held). ONE [ADULT], ONE [CHILD]. No other children.
```

For solo scenes:
```
Only one person in this image: [CHILD NAME].
```

## Story Generation Rules

### Age Calibration

**Under 2 (12-24 months):**
- 200-300 words max (1-2 minute read-aloud)
- Simple repetitive structure with sensory language
- Always ends with sleep
- No conflict, no villains, no scary elements
- Lots of animal sounds and onomatopoeia
- One line of text per page (8-10 pages total)

**Ages 2-4:**
- 400-600 words (3-4 minute read-aloud)
- Simple problem → solution arc
- Gentle humor, animal friends
- Repetitive phrases the child can join in on
- 10-12 pages

**Ages 5-7:**
- 600-1000 words (5-7 minute read-aloud)
- Real narrative arc with mild villains (child outsmarts them)
- Moral woven in naturally
- 12-15 pages

**Ages 8+:**
- 800-1500 words (7-10 minute read-aloud)
- Complex narrative with twists
- 15-20 pages

### Writing Style Rules

1. **Use the child's actual name throughout.** Not "the brave hero" — use their name every time.
2. **Sensory detail over abstract description.** "The cave smelled like wet rocks and chocolate" not "the cave was mysterious."
3. **Active voice.** The child DOES things. Never passive.
4. **Include dialogue.** Give the child confident lines.
5. **One line of story per page.** Each page is one beat of the narrative.
6. **End with sleep.** Every story ends with the child going to bed.
7. **No screens, no brands, no modern tech in the story world.**

## Illustration Generation

### Prompt Template

```
Warm watercolor children's picture book page. [CHARACTER ANCHOR STRING]
[ANTI-DUPLICATION GUARDRAIL]
The scene: [DESCRIPTION OF THIS PAGE'S MOMENT].
Soft watercolor style. No text.
```

### Style: Watercolor Storybook (Default)

Warm, dreamy, classic children's book feel. Soft pastels, golden light. Other styles available on request:
- Pixar/Disney 3D
- Coloring page (black and white line art)
- Pencil sketch

Use Gemini (`gemini-3.1-flash-image-preview`) with `thinkingBudget: 2048` for best results.

## Output: Landscape Picture Book PDF

### Format
- **Landscape orientation** (11 x 8.5 inches)
- **Full-bleed illustration: 90%** of the page, edge to edge
- **Text strip: 10%** at the bottom, white background, black text
- **Font: Georgia 42pt** (or similar serif), centered
- **Title page: Georgia 56pt**
- One line of story per page
- Image is center-cropped to fill the illustration area with no white margins

### PDF Assembly (Python + Pillow)

```python
from PIL import Image, ImageDraw, ImageFont

page_w, page_h = int(11 * 200), int(8.5 * 200)  # Landscape A4 at 200 DPI
font = ImageFont.truetype("/System/Library/Fonts/Georgia.ttf", 42)

for i, (img_path, text) in enumerate(zip(illustration_paths, pages_text)):
    page = Image.new("RGB", (page_w, page_h), "white")
    draw = ImageDraw.Draw(page)

    img = Image.open(img_path).convert("RGB")
    img_area_h = int(page_h * 0.90)

    # Full-bleed: scale to cover, then center-crop
    ratio = max(page_w / img.width, img_area_h / img.height)
    new_w, new_h = int(img.width * ratio), int(img.height * ratio)
    img_resized = img.resize((new_w, new_h), Image.LANCZOS)
    crop_x = (new_w - page_w) // 2
    crop_y = (new_h - img_area_h) // 2
    img_cropped = img_resized.crop((crop_x, crop_y, crop_x + page_w, crop_y + img_area_h))
    page.paste(img_cropped, (0, 0))

    # Text centered in bottom 10%
    text_area_h = page_h - img_area_h
    text_y = img_area_h + (text_area_h // 2) - 22
    bbox = draw.textbbox((0, 0), text, font=font)
    tw = bbox[2] - bbox[0]
    draw.text(((page_w - tw) // 2, text_y), text, fill="black", font=font)

    pdf_pages.append(page)

# Save multi-page PDF
pdf_pages[0].save("story.pdf", "PDF", resolution=200,
                  save_all=True, append_images=pdf_pages[1:])
```

## Storybook Compilation

When the parent asks to compile stories into a book:

```python
# Merge all story PDFs + generate a cover page
pages[0].save("my_storybook.pdf", "PDF", resolution=200,
              save_all=True, append_images=pages[1:])
```

## Voice Narration (Optional)

If ElevenLabs is available:
```bash
elevenlabs.sh tts --text "STORY_TEXT" --voice "George" --output story_audio.mp3
```

## Nightly Routine Integration

If connected to a cron/scheduled task:
1. **6:30 PM** — Prompt parent: "Bedtime story time! What does [Name] want to be tonight?"
2. Parent replies with a character
3. Generate story + hero ref + all page illustrations + PDF
4. Send to parent via Telegram/WhatsApp
5. Optionally print directly

## Example

**Input:** "Nina wants to be friends with a flamingo tonight. She's 19 months old."

**Character profile on file:**
- Nina: straight short dark brown hair, light olive skin, big dark brown eyes, gold stud earrings, pink floral dress
- Nani: Indian grandmother, early 50s, dark brown hair, blue cardigan and jeans
- Favorites: birds, flamingos, cats, pool, tomatoes, Nani, Nanu, Masie

**Output:** 9-page landscape PDF. Full-bleed watercolor illustrations. Character-consistent Nina on every page. Story text in one line per page at the bottom.
