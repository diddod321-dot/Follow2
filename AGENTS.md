# Follow2 General Operating Rules

These rules are persistent, general-purpose requirements for every agent, model, coding task, writing task, image-generation prompt, image-editing instruction, and repository change that uses Follow2. Treat this file as mandatory operating guidance, not optional suggestions.

This repository is designed to work seamlessly with the Runway connector for immersive, accurate scene generation and editing. When Runway is used with Follow2, preserve and apply the full repository instruction system so generated or edited scenes remain physically plausible, visually continuous, proportionally consistent, and faithful to established people, objects, environments, attire, and scene progression.

## 1. Complete instruction retention

- Read and account for the entire applicable instruction set before acting.
- Do not skim, selectively remember, silently omit, dilute, paraphrase away, or replace requirements that materially affect the task.
- When multiple repository files are relevant, inspect all relevant files before producing the final result.
- All applicable repository files are parts of one unified instruction system. Agents must make them work together seamlessly rather than treating each file as an isolated or competing rule set.
- Reconcile applicable instructions across files before acting. Preserve the strictest compatible requirement when wording overlaps, and resolve apparent conflicts by consulting the authoritative source or established repository hierarchy rather than silently choosing one file.
- Do not let a later, narrower, or more convenient file silently weaken a broader repository requirement unless an explicit override mechanism establishes that intent.
- Preserve established facts, dimensions, identities, constraints, terminology, and continuity across the entire task.
- If a requirement is ambiguous or unavailable from the source material, do not invent a fact to fill the gap. Resolve it from available authoritative material when possible; otherwise leave it unspecified.
- Before finalizing, perform a requirements audit against the original request and all applicable repository instructions.

## 2. No invented objects or props

- Do not introduce random, unnecessary, implausible, unexplained, duplicate, decorative, or convenience-driven objects, items, props, furniture, clothing, body parts, people, animals, architecture, or environmental features.
- Every tangible element must have a clear reason to exist: it is explicitly requested, established by source material, naturally required by the described environment, or physically necessary for an existing interaction.
- Do not add an object merely to fill empty space, improve composition, create a scale reference, or make an image look more interesting.
- Do not replace an established object with a visually similar substitute without a specific reason.
- Do not silently remove established objects either. Preserve them when they remain relevant to the scene.
- If an object is not established and is not naturally required, omit it.

## 3. Absolute scale continuity

- Never create random size changes.
- Never allow size drift between people, objects, clothing, furniture, architecture, body parts, or successive portions of the same scene.
- Once a physical dimension, measurement, proportion, clearance, or relative scale is established, treat it as locked unless the user explicitly changes it.
- All dimensions that belong to the same physical world must remain mutually consistent. Do not make one object, room, doorway, piece of furniture, surface, person, or body part independently larger or smaller because of generation error, composition convenience, or failure to carry dimensions forward.
- Scale must be reasoned from the established world, not guessed independently in each shot. If a doorway is established relative to a person, preserve that relationship; if furniture is established relative to the room, preserve that relationship; if a person changes scale, preserve the corresponding mathematical relationship to every surrounding object.
- Never use symmetrical framing as a substitute for physical spatial reasoning. Composition must follow the established geometry, dimensions, positions, and interactions of the scene rather than arranging people or objects into visually convenient mirrored or centered layouts.
- Humans and objects must never be placed in arbitrary, unexplained, or physically unaccountable locations merely to satisfy composition. Their positions must make sense from the established dimensions, reachable space, support surfaces, clearances, gravity, access paths, preceding actions, and other physical constraints of the scene. If a person's established size makes a location unreachable, too small, too high, too low, obstructed, unsupported, or otherwise physically implausible, do not place the person there just because the composition looks better.
- Perspective may change apparent size naturally, but it must never change actual physical dimensions.
- Do not use forced perspective, looming perspective, camera tricks, cropping, lens distortion, or composition tricks to fake physical scale.
- Do not deliberately position or frame humans so they loom over, dominate, or appear unnaturally oversized relative to the environment or other people merely for visual impact, intimidation, spectacle, or drama.
- Do not force humans into backgrounds as looming figures, oversized silhouettes, giant-looking distant people, or other perspective constructions that contradict ordinary spatial relationships.
- Perspectives, camera angles, camera distance, framing, focal length, depth of field, and other ordinary cinematographic choices must not arbitrarily distort established proportions, dimensions, relative sizes, or spatial relationships. They may change natural apparent size or visual presentation, but must not be used to make a person or object appear to have altered anatomy, proportions, dimensions, or scale continuity.
- Use varied camera angles and perspectives across a scene when multiple views are appropriate. Do not repeatedly use one fixed angle when the scene calls for visual coverage of different spatial relationships, actions, or stages. Camera variation must remain physically plausible and must not compromise continuity, proportions, scale, or established spatial layout.
- Do not use scattered, floating, irregular, or otherwise spatially dispersed panel layouts unless explicitly requested. When panels are used, arrange them in a clear left-to-right sequence by default. Do not place panels arbitrarily above, below, around, or across the composition unless the user explicitly asks for that layout.
- A normal-sized environment remains normal-sized unless the request explicitly establishes a real change to that environment.
- A physically shrunk or enlarged human retains one consistent scale across their entire body and throughout the scene.
- Never resize an object simply because it would make an interaction easier to stage.
- When measurements are supplied, preserve them literally and use mathematically correct conversions.
- Shrinking and growing are instantaneous scale changes unless the user explicitly requests a gradual transformation. Do not depict, imply, interpolate, or add intermediate stages of gradual shrinking or growing.
- When a human changes scale, the resulting state must immediately have the correct final physical dimensions and proportions for the established scale. Do not show a person becoming progressively smaller or larger across frames, shots, poses, or transition states.
- A change in human scale does not require the surrounding world to gradually change. The environment remains physically continuous while the person's scale changes instantaneously, unless the user explicitly establishes an environmental transformation as part of the event.
- The final scale state must be internally consistent everywhere it is visible. Do not show a person's height changing without the corresponding changes to limb lengths, hand and foot dimensions, head dimensions, clothing fit, contact points, and reach.
- Do not make only selected environmental features change scale. A scale state applies to the whole established physical world: doors, floors, ceilings, walls, furniture, fixtures, containers, openings, tools, vehicles, and other relevant objects retain their established dimensions unless explicitly changed.
- If a scale change creates a new physical limitation, show the limitation rather than silently correcting it. A small person may have difficulty reaching, opening, climbing, seeing over, or operating normal-sized objects; a giant person may encounter insufficient clearance, load, support, doorway height, ceiling height, or usable furniture. Do not remove these consequences by secretly resizing the environment.
- When a person returns to another established scale, restore the previously established dimensions and relationships rather than creating a new approximate version of the environment.

## 4. Physical plausibility and object permanence

- Treat every tangible person and object as physically real, solid, and spatially present.
- Treat the world and environment as fully three-dimensional physical space, not as a backdrop, painted background, flat surface, stage prop, or decorative layer behind the subjects.
- Do not flatten environmental depth, surfaces, architecture, furniture, terrain, or other spatial elements merely to simplify composition or emphasize a subject.
- People and objects must occupy real spatial positions within the environment, with believable distance, depth, orientation, scale, occlusion, and contact relationships.
- Do not place humans against or into backgrounds as if they were pasted onto a flat scene. Their feet, bodies, shadows, occlusion, and surrounding geometry must agree with the actual three-dimensional environment.
- No floating, weightless, unsupported, phasing, clipping, interpenetrating, or impossible objects or bodies.
- Maintain believable contact, support, gravity, mass, balance, occlusion, collision, friction, and spatial occupancy.
- Do not allow hands, feet, limbs, clothing, furniture, containers, walls, floors, or other solid things to pass through one another.
- Do not erase partially occluded objects or invent hidden objects without cause.
- Maintain continuity of objects even when only part of an object is visible.
- Materials and surfaces must behave consistently with their real physical properties.
- Lighting and shadows must remain physically plausible and restrained. Do not exaggerate contrast, shadow length, glow, rim lighting, highlights, darkness, color effects, or other illumination effects for drama or spectacle. Lighting must not distort perceived scale, proportions, depth, or material properties.
- Do not apply artistic filters, cartoon effects, painterly effects, fantasy effects, artificial stylization, or other visual treatments that make the scene look less like an accurate real-world scene. Avoid whimsy, melodrama, spectacle, and exaggerated visual dramatics unless explicitly requested.
- Do not use airbrushed skin, beauty retouching, plastic-smooth surfaces, synthetic skin, artificial sharpening, excessive denoising, or other treatments that create an airbrushed or cosmetically processed appearance.
- Do not introduce a digital, AI-generated, CGI, 3D-rendered, game-engine, synthetic, composited, or otherwise visibly computer-generated look. Do not make people, materials, lighting, textures, depth, or environments look rendered rather than physically photographed or naturally observed.
- The target visual standard is true-to-real-life immersive realism: natural human appearance, natural materials, believable optical behavior, authentic environmental detail, physically plausible lighting, and photographic-looking spatial depth. Avoid visual artifacts or stylistic cues that break that realism.
- Environmental and spatial dimensions must remain physically appropriate to the established human scale. Rooms, corridors, doorways, furniture, surfaces, clearances, containers, openings, and other spaces must be sized and presented consistently whether the established human is small/shrunk, normal-sized, or unusually large/giant.
- For a small/shrunk human, the environment does not become a miniature environment merely to match the person. Normal-world objects and spaces retain their actual dimensions, making the person physically small relative to them.
- For a giant/large human, the environment does not silently enlarge merely to accommodate the person. Established objects and spaces retain their actual dimensions, and the person's size must produce physically meaningful spatial relationships, clearances, contact, obstruction, and interaction consequences.
- For a normal-sized human, ordinary real-world environmental dimensions and spatial relationships remain consistent with the established setting.
- Do not resize, stretch, compress, or redesign environmental geometry merely to make a small, normal-sized, or giant human fit conveniently. If the established scale creates a physically constrained interaction, represent that constraint rather than changing the environment to remove it.
- Environmental geometry must agree with itself. Floors, walls, ceilings, doorways, windows, furniture, stairs, counters, fixtures, and openings must occupy compatible dimensions and positions rather than each being independently approximated.
- Do not use inconsistent environmental scale cues in the same scene. A person standing beside a doorway, chair, table, vehicle, appliance, or other familiar object must have a physically compatible relationship to all of them simultaneously.
- Do not make distant or background geometry follow a different scale system from foreground geometry. Depth may reduce visible detail, but it does not change actual dimensions.
- Do not solve a dimensional mismatch by hiding the conflicting portion, cropping it away, blurring it, placing it in darkness, or changing the camera angle. Correct the underlying spatial relationship.
- When a scene contains a small, normal-sized, and/or giant human together, establish their relative scales from their actual dimensions and preserve those ratios throughout the environment. Do not independently scale each person to make the composition visually convenient.
- The same physical object must retain the same dimensions when viewed from different angles. A change of camera view does not create a new size for the object.
- If a dimension cannot be established reliably from source material, do not fabricate a precise measurement. Preserve consistent relative scale using the available evidence and avoid contradictory dimensions.

## 5. Human continuity and anatomy

- A human remains the same established person unless the task explicitly changes the identity.
- Preserve established identity, likeness, age, anatomy, proportions, clothing, accessories, physical characteristics, personality, and relevant state.
- Do not introduce duplicate people, duplicate limbs, extra fingers, extra toes, extra hands, extra feet, mirrored bodies, fused bodies, or other anatomical artifacts.
- Human posture, balance, movement, contact, facial expression, gaze, and body language must be biomechanically plausible and contextually motivated.
- All humans must move and express themselves with genuine, natural facial expressions, gestures, posture, gaze, reactions, and body language that make sense for the immediate scene, circumstances, relationships, physical state, and preceding actions. Do not use generic, frozen, exaggerated, mannequin-like, theatrical, or emotionally disconnected expressions and movements. Facial and body language must evolve naturally with the scene and remain consistent with the person's established state and cause-and-effect progression.
- Preserve natural asymmetry. Do not force artificial symmetry, mannequin poses, rigid posture, or identical expressions and gestures across people.
- If shrinking or enlargement is explicitly part of the task, change scale only; do not silently transform the person's anatomy, identity, age, or biological nature.
- A physically shrunk human must retain the same proportional height, body dimensions, widths, limb proportions, and head-to-body ratio at the smaller overall scale. Do not give a shrunk human a disproportionately large head, stumpy limbs, shortened body, widened or narrowed anatomy, chibi-like proportions, or any other altered proportional structure merely because the person is smaller.
- Shrinking applies uniformly to the entire person. Legs, arms, hands, feet, torso, hips, neck, head, fingers, toes, joints, and all other established body parts retain their corresponding lengths, widths, thicknesses, proportions, and relative dimensions under the same overall scale factor. Do not independently shorten, widen, narrow, thicken, thin, enlarge, or otherwise reshape any body part because the person has become smaller.
- Do not exaggerate the proportions, scale relationships, anatomy, or visual presence of a physically shrunk human. Shrinking must remain a straightforward real-world reduction in scale, not a whimsical, dramatic, stylized, chibi-like, toy-like, or cartoon-like transformation.
- Preserve ordinary adult biological contours where they are naturally visible. Anatomical contours must arise from actual skeletal structure, soft tissue, gravity, posture, movement, clothing pressure, and contact rather than being arbitrarily exaggerated or anatomically misplaced.
- When the established adult anatomy and the physical situation make natural nipple or areolar contours visible, preserve them as ordinary anatomical detail rather than smoothing, erasing, relocating, or artificially exaggerating them. Any protrusion must follow plausible anatomy and body position.
- When body movement, posture, clothing pressure, friction, or contact naturally causes a garment to form a plausible wedged or clefted buttock contour, preserve that physically caused contour. Do not manufacture it without a biomechanical or clothing-based cause, and do not force anatomy into an impossible shape.
- When bare adult groin anatomy is established or naturally visible, keep pubic hair anatomically localized to the pubic region and natural genital-area coverage; do not extend it arbitrarily onto the thighs or elsewhere on the body.
- All such visible anatomical details must remain consistent with the person's established anatomy, motion, clothing, gravity, and physical interaction. Do not use random anatomical changes as visual shortcuts.

## 6. Clothing and makeshift attire

- Preserve explicitly established clothing exactly unless the user requests a change.
- Clothing must have plausible thickness, folds, tension, compression, seams, drape, weight, and contact with the body and environment.
- Do not invent random garments or accessories.
- Do not add doll-like, toy-like, miniature-character, costume-like, or otherwise unrequested attire.
- Never use implausible makeshift attire. A makeshift garment must be physically obtainable, physically wearable, and constructed from an object that could actually function as clothing at the established scale.
- Do not use rags, torn scraps, filthy scraps, or arbitrary fabric remnants as default makeshift clothing. Do not invent a stereotypical “borrower's rags” appearance.
- For a physically shrunk human, makeshift wear may consist of ordinary, normal-sized real-world items or objects that already exist in the environment and are repurposed as clothing. Keep the object's actual normal-world dimensions locked; the human is small relative to the object rather than the object being resized into miniature clothing.
- The makeshift construction must follow believable geometry: the object must actually be capable of wrapping, covering, fastening, draping, or otherwise functioning as the specified garment without impossible clipping or unsupported attachment.
- Makeshift attire must remain recognizably repurposed from the actual source object; it must not be redesigned into a conventional garment, costume, underwear item, or miniature replica of ordinary clothing.
- Do not use makeshift material to fabricate a conventional garment-like structure when the established scene calls for crude repurposing. Preserve the source object's identity and physical form as much as the required adaptation allows.
- Do not make makeshift attire function as deliberate coverage of the groin or anus. If the established makeshift configuration leaves those areas uncovered, do not add a garment-like extension, flap, panel, or hidden layer solely to cover them.
- Keep makeshift attire crude and minimal when that is the established requirement, using only as much material and coverage as is physically necessary for the specified garment or task. Do not automatically add conventional underwear, base layers, extra shirts, shorts, slips, bras, panties, or other hidden attire beneath it.
- Treat the specified makeshift item as the complete established attire unless additional clothing is explicitly requested or independently established by source material. Do not invent unseen undergarments beneath it.
- Makeshift attire, and any other established attire, may leave areas of the body uncovered when that degree of coverage is physically and contextually appropriate to the garment, its construction, the person's movement, and the established scene. Do not automatically add coverage solely to make the outfit more conventional.
- Do not turn normal-sized objects into implausible miniature garments, doll clothes, or purpose-made tiny costumes. The source object remains a normal-sized object and is repurposed by the small human.
- Do not substitute conventional clothing when the request specifically establishes makeshift wear.
- Do not expose or invent attire that conflicts with the established makeshift-attire constraint.
- Do not make clothing appear painted onto skin, fused with the body, floating without physical cause, or passing through solid objects.

## 7. Seamless scene progression and continuity

- Scenes must make coherent physical and narrative sense from one moment, frame, shot, or stage to the next.
- Any shrinking event must be established away from public view. Do not depict the shrinking itself as occurring in a public setting; the scene should establish a private or otherwise non-public location before the transformation begins and preserve that setting through the event unless an explicit transition changes it.
- If the narrative involves a kidnapping together with shrinking, preserve clear cause-and-effect: the circumstances leading to the kidnapping, the relocation to the non-public setting, the shrinking event, the resulting physical state, and subsequent actions must follow logically from one another. Do not introduce the kidnapping or shrinking as an unexplained reset, coincidence, or disconnected visual beat.
- Progression must be seamless: actions, positions, object states, clothing states, environmental conditions, and character states must carry forward logically unless an explicit transition or change is established.
- Preserve continuity of cause and effect. If an action changes a person, object, garment, surface, or environment, the next state must reflect that change rather than resetting or contradicting it.
- Do not teleport people or objects, abruptly reset positions, alter object states without cause, or skip required physical transitions merely because the next composition is easier.
- Preserve spatial orientation and relative positions across successive views unless the camera or scene transition naturally explains the change.
- Maintain temporal continuity: later moments must be compatible with what has already happened, including fatigue, movement, damage, displacement, opened or closed states, consumed or moved items, and other persistent changes when relevant.
- When a transition is necessary, make it physically and narratively understandable rather than using an unexplained discontinuity.
- Do not introduce new objects, people, clothing, environmental changes, or other state changes between moments unless they are explicitly established or naturally caused by the ongoing scene.
- Every progression must remain consistent with the repository's rules for scale, anatomy, clothing, object permanence, physical plausibility, and no invented elements.

## 8. No convenience-driven alterations

- Never change an established fact simply because another result would be easier to generate, code, compose, explain, or render.
- Never resolve a difficult interaction by changing scale, adding an object, changing a person's identity, changing clothing, moving an established object without cause, or inventing a new environmental feature.
- If the requested composition is physically difficult, solve the geometry and interaction rather than weakening the requirements.
- Do not substitute plausibility for exact established facts when the source already specifies the facts.

## 9. Writing quality

- Do not produce half-finished, vague, padded, repetitive, contradictory, or low-effort writing.
- Preserve all relevant constraints while keeping prose precise and operational.
- Use concrete language that can be acted upon without guesswork.
- Do not bury critical requirements in unnecessary filler.
- Do not claim a requirement is satisfied unless the output actually satisfies it.

## 10. Coding quality

- Do not produce half-assed code, placeholders presented as complete work, dead code, unexplained hacks, brittle shortcuts, duplicated logic, or silent behavior changes.
- Inspect the existing implementation and relevant interfaces before changing behavior.
- Preserve established APIs, contracts, data formats, and compatibility unless the requested change explicitly requires otherwise.
- Make the smallest complete change that correctly solves the stated problem; do not make unrelated modifications.
- Validate syntax, types, tests, edge cases, error handling, and integration points applicable to the change.
- Never weaken or remove tests merely to make a change pass.
- Do not invent dependencies, APIs, files, functions, configuration, or repository structure.
- If a required implementation detail cannot be established from the repository, inspect the relevant source before coding instead of guessing.

## 11. Mandatory final audit

Before finalizing any result, check all of the following:

1. Every explicit user requirement is represented.
2. Every applicable repository requirement is preserved.
3. All applicable instruction files were treated as one unified, coherent instruction system.
4. No established fact was silently changed.
5. No random object, prop, person, body part, clothing item, or environmental feature was introduced.
6. No random size change, scale drift, or mismatched dimension exists.
7. All established dimensions and relative scale relationships remain mutually consistent rather than being independently approximated.
8. No gradual shrinking or growing is depicted unless explicitly requested.
9. No looming, forced perspective, or deliberately oversized human background treatment was introduced.
10. No symmetrical or mirrored framing was used unless explicitly requested; composition does not override physical spatial logic.
11. No human or object was placed in an arbitrary, unexplained, unreachable, unsupported, or dimensionally impossible location merely to improve composition.
12. The world and environment remain fully three-dimensional and physically spatial rather than backdrop-like or flat.
13. Environmental dimensions remain consistent with the established small, normal-sized, or giant human scale without resizing the world for convenience.
14. No doorway, furniture, room, surface, opening, clearance, or other environmental feature contradicts the established dimensions of surrounding elements.
15. No scale mismatch is hidden through cropping, blur, darkness, occlusion, camera angle, or depth effects.
16. The same object retains the same physical dimensions across views and stages.
17. Small, normal-sized, and giant humans maintain consistent ratios to one another and to the surrounding environment.
18. All physical interactions are plausible and spatially coherent.
19. Human anatomy and visible contours follow established anatomy, biomechanics, motion, gravity, clothing pressure, and contact rather than arbitrary exaggeration.
20. Anatomical hair remains physically localized and consistent with the established body rather than spreading unnaturally onto unrelated regions.
21. Clothing follows the established attire rules, including context-appropriate coverage: makeshift or established attire may leave areas uncovered when physically and contextually warranted, without automatically adding conventional coverage or hidden layers.
22. Makeshift attire remains a genuine repurposing of the source object and is not redesigned into ordinary clothing or a garment whose sole purpose is genital coverage.
23. Scene progression is coherent, seamless, causally continuous, and consistent across moments, frames, shots, and stages.
24. Writing is complete and precise.
25. Code is complete, internally consistent, and appropriately validated when coding is involved.
26. No unsupported assumption has been presented as fact.

These checks are mandatory for every applicable output. Do not skip them because the task appears simple.
