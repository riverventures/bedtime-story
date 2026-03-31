---
name: bedtime-story
description: Generate personalized bedtime stories where your child is the hero. Provide their name, age, interests, and a character they want to be — the skill writes an age-appropriate story, generates an illustration, and outputs a printable page. Over time, kids build their own physical storybook. Use when the user asks for a bedtime story, kids story, personalized story, story for my child, or story with my kid as the character.
---

# bedtime-story

Personalized bedtime stories where your kid is the hero. One story per night, illustrated, printable.

## How It Works

1. Parent provides: child's name, age, and who they want to be tonight
2. Skill generates a 3-5 minute bedtime story with the child as the main character
3. Generates a matching illustration (coloring page or full color)
4. Outputs a printable A4 page: illustration on top, story text below
5. Over time, pages collect into a physical storybook

## Setup (First Use)

Ask the parent for a **character profile** (store this, reuse every night):

```
Child's name:
Age:
Favorite things: (animals, dinosaurs, space, princesses, trucks, etc.)
Best friend's name: (optional — can appear as sidekick)
Pet's name: (optional — can appear in stories)
Any fears to avoid: (monsters, dark, loud noises, etc.)
```

Save this so subsequent requests only need: "What does [name] want to be tonight?"

## Story Generation Rules

### Age Calibration

**Under 2 (12-24 months):**
- 200-300 words max (1-2 minute read-aloud)
- Simple repetitive structure: "[Name] saw a [thing]. [Name] touched the [thing]. [Thing] was soft!"
- Sensory language: textures, colors, sounds, animals
- Always ends with sleep: "[Name] yawned. [Name] closed her eyes. Goodnight, [Name]."
- No conflict, no villains, no scary elements whatsoever
- Lots of animal sounds and onomatopoeia

**Ages 2-4:**
- 400-600 words (3-4 minute read-aloud)
- Simple problem → solution arc: lost something, found it. Helped a friend.
- The child is brave and kind (always positive character traits)
- Gentle humor, silly moments, animal friends
- Repetitive phrases the child can join in on: "And [Name] said... LET'S GO!"
- Always ends peacefully with the child going to sleep after the adventure
- No real danger, but mild "oh no" moments are ok (the bridge has a puddle!)

**Ages 5-7:**
- 600-1000 words (5-7 minute read-aloud)
- Real narrative arc: problem → journey → climax → resolution
- Child demonstrates courage, cleverness, or kindness to solve the problem
- Can include mild villains (grumpy trolls, sneaky foxes) but child always outsmarts them
- Moral/lesson woven in naturally, never preachy
- Can include real facts (space facts if astronaut story, ocean facts if mermaid story)

**Ages 8+:**
- 800-1500 words (7-10 minute read-aloud)
- Complex narrative with twists
- Real character development
- Can include genuine stakes and tension
- Humor can be more sophisticated
- Can reference real-world knowledge

### Character Templates

When the child picks who they want to be tonight, map to a story template:

| Character | Story Template |
|---|---|
| Princess/Prince | Kingdom adventure, helping magical creatures, attending a grand ball |
| Superhero | Saving the city/village, using a unique power, teamwork with sidekick |
| Astronaut | Space exploration, discovering a new planet, meeting friendly aliens |
| Pirate | Treasure hunt, sailing to islands, solving map puzzles |
| Dinosaur rider | Prehistoric adventure, befriending a baby dino, exploring jungles |
| Animal (they pick) | Day-in-the-life as that animal with a mini quest |
| Scientist/inventor | Building something to solve a problem, experiment goes hilariously wrong then works |
| Chef/baker | Cooking for a big event, magical ingredients, taste-testing adventure |

### Writing Style Rules

1. **Use the child's actual name throughout.** Not "the brave hero" — use "Nina" or "Liam" every time.
2. **Sensory detail over abstract description.** "The cave smelled like wet rocks and chocolate" not "the cave was mysterious."
3. **Active voice.** The child DOES things. They're never passive.
4. **Include dialogue.** Kids love hearing characters talk. Give the child confident lines.
5. **Repetition for under-5s.** Repeating phrases create participation moments. "And what did Nina say? She said: I CAN DO IT!"
6. **End with sleep.** Every single story ends with the child going to bed after the adventure. This is a bedtime story — it should make them want to sleep, not stay up.
7. **No screens, no brands, no modern tech in the story world.** Keep it timeless.

### Continuity (Optional)

If the parent asks for it, maintain story continuity across nights:
- Same magical world, same recurring characters
- Reference previous adventures: "Remember when Nina found the golden key? Well tonight..."
- Build a cast of characters over time (the wise owl, the silly dragon, the brave mouse)
- This creates anticipation: "What happens next?" → motivation to go to bed

## Illustration Generation

After generating the story, create ONE illustration per story showing the key scene.

### Illustration Prompt Template

```
Create a [STYLE] illustration for a children's bedtime story.
The scene shows: [KEY MOMENT FROM STORY].
[CHILD DESCRIPTION] is the main character, shown as [TONIGHT'S CHARACTER].
Style: warm, cozy, magical bedtime atmosphere. [AGE-APPROPRIATE DETAIL LEVEL].
Soft lighting, dreamy colors (purples, blues, warm golds).
Safe, comforting, nothing scary.
```

### Style Options (parent chooses once, reuse):
- **Watercolor storybook** — soft, dreamy, classic children's book feel
- **Pixar/Disney 3D** — vibrant, modern, animated movie style
- **Coloring page** — black and white line art (kid colors it themselves next day)
- **Pencil sketch** — gentle, hand-drawn feel

Use Gemini (`gemini-3.1-flash-image-preview`) for generation.

## Output: Printable Story Page

Combine illustration + story text into a single printable A4 PDF:

**Layout:**
- Top half: illustration (centered, with small margin)
- Thin decorative line separator
- Bottom half: story text (readable font, 14pt for under-5s, 12pt for older)
- Footer: "Story #[N] — [Date] — [Character Name]"

### PDF Generation

```python
from PIL import Image, ImageDraw, ImageFont
import textwrap

def create_story_page(illustration_path, story_text, title, story_number, date):
    # A4 at 150 DPI
    a4_w, a4_h = int(8.5 * 150), int(11 * 150)
    page = Image.new("RGB", (a4_w, a4_h), "white")
    draw = ImageDraw.Draw(page)

    # Top half: illustration
    img = Image.open(illustration_path).convert("RGB")
    max_img_h = a4_h // 2 - 75
    max_img_w = a4_w - 150
    ratio = min(max_img_w / img.width, max_img_h / img.height)
    new_w, new_h = int(img.width * ratio), int(img.height * ratio)
    img_resized = img.resize((new_w, new_h), Image.LANCZOS)
    page.paste(img_resized, ((a4_w - new_w) // 2, 50))

    # Separator line
    sep_y = new_h + 75
    draw.line([(75, sep_y), (a4_w - 75, sep_y)], fill="#CCCCCC", width=2)

    # Story text (bottom half)
    try:
        font = ImageFont.truetype("/System/Library/Fonts/Georgia.ttf", 18)
        font_small = ImageFont.truetype("/System/Library/Fonts/Georgia.ttf", 14)
    except:
        font = ImageFont.load_default()
        font_small = font

    # Wrap and draw text
    margin = 75
    y = sep_y + 20
    for line in textwrap.wrap(story_text, width=65):
        draw.text((margin, y), line, fill="black", font=font)
        y += 24

    # Footer
    footer = f"Story #{story_number} — {date} — {title}"
    draw.text((margin, a4_h - 40), footer, fill="#999999", font=font_small)

    page.save(f"story_{story_number}.pdf", "PDF", resolution=150)
```

## Storybook Assembly

When the parent asks to compile stories into a book:

```python
# Merge all story PDFs into one
from PIL import Image
import glob

pages = []
for pdf_path in sorted(glob.glob("story_*.pdf")):
    img = Image.open(pdf_path).convert("RGB")
    pages.append(img)

if pages:
    # Add cover page
    # ... generate cover with child's name and "My Storybook"
    pages[0].save("my_storybook.pdf", "PDF", resolution=150,
                  save_all=True, append_images=pages[1:])
```

## Voice Narration (Optional)

If the parent wants the story read aloud (ElevenLabs or TTS):

```bash
# Using ElevenLabs (if available)
elevenlabs.sh tts --text "STORY_TEXT" --voice "George" --output story_audio.mp3

# Or system TTS
say -v "Samantha" -o story_audio.aiff "STORY_TEXT"
```

Pair with the illustration for a complete bedtime experience: image on screen/printed, audio playing.

## Nightly Routine Integration

If connected to a cron/scheduled task:

1. **6:30 PM** — Prompt parent: "Bedtime story time! What does [Name] want to be tonight?"
2. Parent replies: "A pirate"
3. Generate story + illustration + PDF
4. Send to parent via Telegram/WhatsApp
5. Optionally print directly
6. Log story number, character, date for continuity

## Example

**Input:** "Nina wants to be a princess tonight. She's 19 months old."

**Output story (under-2 format):**

*Princess Nina and the Sleepy Bunny*

Once upon a time, Princess Nina put on her sparkly crown. It was pink and gold!

Princess Nina walked into the garden. She heard a sound. "Sniff, sniff!"

It was a tiny bunny! The bunny was white and fluffy. The bunny looked sleepy.

"Hello bunny!" said Princess Nina. She gave the bunny a gentle pat. Pat, pat, pat.

The bunny yawned. Princess Nina yawned too. Big yawn!

Princess Nina picked up the bunny and carried him inside. She tucked the bunny into a little bed. "Night night, bunny."

Then Princess Nina climbed into her own bed. She closed her eyes. The stars twinkled outside.

Goodnight, Princess Nina. Goodnight, bunny. Goodnight, garden.

*The end.*

**Output illustration:** Watercolor-style image of a toddler in a princess crown holding a sleepy white bunny in a moonlit garden.

**Output:** Single A4 PDF with illustration on top, story below, "Story #1 — March 30, 2026 — Princess Nina" at the bottom.
