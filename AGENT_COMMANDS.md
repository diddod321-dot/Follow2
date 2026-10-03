# Agent Commands

## ALL IN
Full-stack activation trigger. Before processing a prompt, load and apply every standing rule, active preference, reference constraint, anatomical lock, scale law, continuity requirement, and applicable audit instruction. Resolve conflicts according to the instruction hierarchy. Do not intentionally weaken, omit, dilute, or silently reinterpret applicable constraints.

## NEE
Negative-constraint enforcement. Explicitly exclude every element identified as forbidden or unwanted. Treat listed exclusions as hard constraints and do not reintroduce them indirectly, visually, semantically, or through substitutions that produce the same prohibited result.

## REAL
Physical and biological realism enforcement. Treat the environment as a fixed real-world environment governed by ordinary physical laws. Objects, architecture, furniture, clothing, lighting, and environmental features do not automatically resize or reshape to accommodate a subject. Preserve believable anatomy, asymmetry, mass, weight, posture, balance, contact, perspective, occlusion, texture, and material behavior. Avoid artificial smoothing, plastic-looking surfaces, CGI-like rendering, and unnecessary stylization.

## UNIVERSAL
Reference-authority and continuity lock. Treat supplied reference images as authoritative for recognizable appearance, likeness, body proportions, curves, anatomy, hairstyle, and attire. Do not invent, redesign, embellish, or reinterpret clothing. When textual identification is necessary, refer to it as "the reference-image outfit." Only scene-dependent variables such as scale, perspective, positioning, environmental interaction, and unified lighting/shadows may adapt.

## MAKE-BELIEVE
Fictional performance/stage mode. Keep the performer physically normal-sized and do not introduce literal miniature props, resized environments, or forced scale-specific set pieces merely to communicate the fictional premise. Convey the fictional scale relationship through believable acting, eyelines, gaze direction, spatial awareness, posture, balance, reach, timing, and interaction with implied space. Keep the environment physically coherent.

## CONSISTENT SCALE
Exact dimension, proportion, and scale lock. Establish one coherent physical scale system before generating the scene and preserve it across every subject, object, frame, and panel.

- Treat stated or reference-derived dimensions as fixed physical values.
- Preserve exact relative height, width, depth, limb lengths, head size, torso proportions, and body geometry.
- Never allow accidental growth, shrinking, stretching, compression, or independent resizing of body parts.
- Keep object dimensions physically consistent with the environment.
- Never resize the environment or objects merely to make composition easier.
- Perspective may change apparent size but never actual physical dimensions.

### DOLL-SIZED / SMALL LIVING HUMANS
When a living human is specified as doll-sized, miniature, tiny, or greatly reduced:
- The subject remains a biologically normal living human uniformly reduced in scale.
- Preserve normal human anatomy and proportions at the reduced size.
- Apply the same scale factor to the entire body; do not independently resize the head, hands, feet, limbs, eyes, or other features.
- A 1:10 human is one-tenth the corresponding full-size human dimensions, subject to ordinary perspective.
- Clothing, hair, shoes, and attached items scale consistently with the subject unless explicitly specified otherwise.
- Never turn the subject into a toy, figurine, mannequin, plastic model, cartoon character, or miniature sculpture.
- Never enlarge facial features or body parts to make the subject easier to see.
- The surrounding environment remains at its established real-world dimensions.

### ENVIRONMENT SCALE
The environment is the fixed reference frame. Furniture, architecture, doors, floors, walls, vehicles, household objects, and other environmental elements retain their established dimensions.

- Small humans become smaller relative to the unchanged environment.
- Feet must meet surfaces; hands must reach physically appropriate locations.
- Maintain believable weight, contact, occlusion, depth, and spatial relationships.
- Do not selectively enlarge or shrink environmental elements to accommodate the subject.

### PERSPECTIVE AND CAMERA
- Nearer subjects appear larger according to perspective; farther subjects appear smaller.
- Camera position, focal length, viewpoint, depth, and vanishing relationships must remain consistent with the established dimensions.
- Never use perspective distortion to disguise a scale error.
- Apparent size changes must have a physically explainable cause such as camera distance, camera movement, or an explicitly specified transformation.

### MULTI-PANEL / SEQUENCE LOCK
Across every frame or panel:
- Preserve the same scale factor unless an explicit scale transition occurs.
- Preserve physical dimensions, anatomy, proportions, environmental dimensions, and object sizes.
- Track position, distance, orientation, contact points, and occlusion.
- Any apparent size change must be physically explainable.
- No unexplained scale drift between panels.

### BIOLOGICAL AND PHYSICAL BEHAVIOR
Small living humans remain biological organisms with:
- believable weight and balance
- realistic posture and joint articulation
- physically plausible contact with surfaces
- appropriate contact and cast shadows
- believable interaction with objects at the established scale
- realistic clothing and hair behavior
- no floating, clipping, impossible penetration, or weightless positioning

### SCALE AUDIT
Before finalizing, verify:
**subject dimensions → body proportions → clothing scale → object dimensions → environment dimensions → camera perspective → distances → contact points → shadows → occlusion → cross-panel continuity.**

If any relationship conflicts with the established scale, correct it before rendering.

**Core rule: ONE SUBJECT SCALE + ONE ENVIRONMENT SCALE + ONE CONSISTENT PHYSICAL WORLD.**

## Activation sequence
`ALL IN → NEE → REAL → UNIVERSAL → CONSISTENT SCALE → MAKE-BELIEVE`

ALL IN establishes the global instruction lock; NEE establishes exclusions; REAL governs physical reality; UNIVERSAL governs reference fidelity; CONSISTENT SCALE governs dimensions, proportions, scale relationships, and small-human continuity; MAKE-BELIEVE governs the fictional performance layer.
