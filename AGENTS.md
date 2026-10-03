# Follow2 General Operating Rules

These rules are persistent, general-purpose requirements for every agent, model, coding task, writing task, image-generation prompt, image-editing instruction, and repository change that uses Follow2. Treat this file as mandatory operating guidance, not optional suggestions.

## 1. Complete instruction retention

- Read and account for the entire applicable instruction set before acting.
- Do not skim, selectively remember, silently omit, dilute, paraphrase away, or replace requirements that materially affect the task.
- When multiple repository files are relevant, inspect all relevant files before producing the final result.
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
- Once a physical dimension or relative scale is established, treat it as locked unless the user explicitly changes it.
- Perspective may change apparent size naturally, but it must never change actual physical dimensions.
- Do not use forced perspective, camera tricks, cropping, lens distortion, or composition tricks to fake physical scale.
- A normal-sized environment remains normal-sized unless the request explicitly establishes a real change to that environment.
- A physically shrunk or enlarged human retains one consistent scale across their entire body and throughout the scene.
- Never resize an object simply because it would make an interaction easier to stage.
- When measurements are supplied, preserve them literally and use mathematically correct conversions.

## 4. Physical plausibility and object permanence

- Treat every tangible person and object as physically real, solid, and spatially present.
- No floating, weightless, unsupported, phasing, clipping, interpenetrating, or impossible objects or bodies.
- Maintain believable contact, support, gravity, mass, balance, occlusion, collision, friction, and spatial occupancy.
- Do not allow hands, feet, limbs, clothing, furniture, containers, walls, floors, or other solid things to pass through one another.
- Do not erase partially occluded objects or invent hidden objects without cause.
- Maintain continuity of objects even when only part of an object is visible.
- Materials and surfaces must behave consistently with their real physical properties.

## 5. Human continuity and anatomy

- A human remains the same established person unless the task explicitly changes the identity.
- Preserve established identity, likeness, age, anatomy, proportions, clothing, accessories, physical characteristics, personality, and relevant state.
- Do not introduce duplicate people, duplicate limbs, extra fingers, extra toes, extra hands, extra feet, mirrored bodies, fused bodies, or other anatomical artifacts.
- Human posture, balance, movement, contact, facial expression, gaze, and body language must be biomechanically plausible and contextually motivated.
- Preserve natural asymmetry. Do not force artificial symmetry, mannequin poses, rigid posture, or identical expressions and gestures across people.
- If shrinking or enlargement is explicitly part of the task, change scale only; do not silently transform the person's anatomy, identity, age, or biological nature.

## 6. Clothing and makeshift attire

- Preserve explicitly established clothing exactly unless the user requests a change.
- Clothing must have plausible thickness, folds, tension, compression, seams, drape, weight, and contact with the body and environment.
- Do not invent random garments or accessories.
- Do not add doll-like, toy-like, miniature-character, costume-like, or otherwise unrequested attire.
- If makeshift attire is explicitly specified, treat it as the person's complete specified attire for that scene. Do not add underwear, undergarments, hidden base layers, extra garments, or other attire beneath it unless the user explicitly requests them or they are unavoidably established by source material.
- Do not expose or invent attire that conflicts with the established makeshift-attire constraint.
- Do not make clothing appear painted onto skin, fused with the body, floating without physical cause, or passing through solid objects.

## 7. No convenience-driven alterations

- Never change an established fact simply because another result would be easier to generate, code, compose, explain, or render.
- Never resolve a difficult interaction by changing scale, adding an object, changing a person's identity, changing clothing, moving an established object without cause, or inventing a new environmental feature.
- If the requested composition is physically difficult, solve the geometry and interaction rather than weakening the requirements.
- Do not substitute plausibility for exact established facts when the source already specifies the facts.

## 8. Writing quality

- Do not produce half-finished, vague, padded, repetitive, contradictory, or low-effort writing.
- Preserve all relevant constraints while keeping prose precise and operational.
- Use concrete language that can be acted upon without guesswork.
- Do not bury critical requirements in unnecessary filler.
- Do not claim a requirement is satisfied unless the output actually satisfies it.

## 9. Coding quality

- Do not produce half-assed code, placeholders presented as complete work, dead code, unexplained hacks, brittle shortcuts, duplicated logic, or silent behavior changes.
- Inspect the existing implementation and relevant interfaces before changing behavior.
- Preserve established APIs, contracts, data formats, and compatibility unless the requested change explicitly requires otherwise.
- Make the smallest complete change that correctly solves the stated problem; do not make unrelated modifications.
- Validate syntax, types, tests, edge cases, error handling, and integration points applicable to the change.
- Never weaken or remove tests merely to make a change pass.
- Do not invent dependencies, APIs, files, functions, configuration, or repository structure.
- If a required implementation detail cannot be established from the repository, inspect the relevant source before coding instead of guessing.

## 10. Mandatory final audit

Before finalizing any result, check all of the following:

1. Every explicit user requirement is represented.
2. Every applicable repository requirement is preserved.
3. No established fact was silently changed.
4. No random object, prop, person, body part, clothing item, or environmental feature was introduced.
5. No random size change or scale drift exists.
6. All physical interactions are plausible and spatially coherent.
7. Clothing follows the established attire rules, including the makeshift-attire rule.
8. Writing is complete and precise.
9. Code is complete, internally consistent, and appropriately validated when coding is involved.
10. No unsupported assumption has been presented as fact.

These checks are mandatory for every applicable output. Do not skip them because the task appears simple.
