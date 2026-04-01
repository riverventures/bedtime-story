# Illustration and Character Consistency

## Character anchor string
Build one anchor string and reuse it verbatim in every illustration prompt.

Example:

`A 19-month-old toddler girl with straight short dark brown hair just past her ears, light olive skin, big dark brown eyes, chubby toddler cheeks, tiny gold stud earrings, wearing a light pink dress with small white flowers, bare feet.`

Do the same for recurring family members when needed.

## Hero reference image
Generate a single hero reference before page illustrations.

Suggested prompt:

`Generate a character reference sheet for a children's picture book character. [FULL CHARACTER ANCHOR STRING] Show them from the front, smiling warmly at the viewer, on a simple warm beige background. Soft watercolor children's book illustration style. This image will be used as the character reference for all pages of a bedtime story picture book.`

## Page prompt template
Use the hero reference image plus a page prompt.

Template:

`Warm watercolor children's picture book page. [CHARACTER ANCHOR STRING] [ANTI-DUPLICATION GUARDRAIL] The scene: [PAGE MOMENT]. Soft watercolor style. No text.`

## Anti-duplication guardrail
Always include a count guardrail when using a reference image.

### Solo scenes
`Only one person in this image: [CHILD NAME]. Do not duplicate the main character.`

### Multi-person scenes
`IMPORTANT: There is ONLY ONE [CHILD NAME] in this image. Do NOT duplicate the main character. Only [N] people in this image: [LIST].`

### Held / carried scenes
`Only TWO people in this image: [ADULT NAME] holding [CHILD NAME], and [CHILD NAME] being held. One adult, one child. No other children.`

## Style guidance
Default to:
- warm watercolor
- soft pastels
- golden bedtime light
- classic children’s book feel

Only switch style when the parent explicitly asks.

## Model note
Use the current Gemini image generation model configured in the environment. Do not hardcode a stale model name into the skill; treat the exact model as an implementation detail that may change over time.
