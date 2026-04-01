# Bedtime Story Workflow

Use this when executing the skill end-to-end.

## 1. Intake

If there is no saved child profile, collect:
- child name
- age
- appearance: hair, skin tone, eyes, distinguishing features, default outfit
- favorite things
- recurring family members with short visual descriptions
- avoid list: fears, topics, characters, sounds, or themes to avoid

If a profile already exists, ask only for tonight's theme or role.

## 2. Plan the story before generating assets

Decide all of this up front:
- title
- target page count based on age
- one page beat per page
- final line for each page
- which pages include recurring family members

Do not generate illustrations before the page beats and story lines are locked.

## 3. Build character anchors

Create:
- one anchor string for the child
- one anchor string for each recurring family member who appears

Reuse these strings verbatim across prompts.

## 4. Generate the hero reference image

Create exactly one child reference image before any page art.

Use the child anchor string and a neutral front-facing composition so the reference is maximally reusable.

## 5. Generate page illustrations

For each page:
- use the hero reference image as an input
- include the same child anchor string verbatim
- include anti-duplication guardrails
- describe only one story beat per image
- do not place text inside the image

When family members appear, include their anchor strings too.

## 6. Assemble deliverables

Minimum deliverable:
- one text line per page
- one image per page
- one landscape PDF

Optional deliverables when requested:
- readable PDF variant with larger margins or text area
- narration audio
- archived story folder with images + text

## 7. Final quality check

Before delivering:
- verify page count matches age target
- verify number of images matches number of lines
- verify the child is not duplicated within any single image
- verify tone is calm and bedtime-safe
- verify the ending lands in sleep, cuddles, or winding down
