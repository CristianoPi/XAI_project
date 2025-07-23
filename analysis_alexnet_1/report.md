## 1 Aggregate statistics
- **Total Images**: 91
- **Mean Score**: 0.35
- **Median Score**: 0.4
- **Standard Deviation of Scores**: 0.21
- **Percentage of Incoherent Images**: 41.76%
  
### Object Incoherence Statistics
- **Ceramic Coffee Mug**: 31.25% incoherent (5 out of 16)
- **Notebook with Kraft Cover**: 73.33% incoherent (11 out of 15)
- **Opaque Metal Water Bottle**: 45.00% incoherent (9 out of 20)
- **Soft Couch Pillow**: 50.00% incoherent (10 out of 20)
- **Table Lamp with Shade (Off)**: 15.00% incoherent (3 out of 20)

### Context Incoherence Statistics
- **Bathroom Vanity Matte Tiles**: 42.86% incoherent (3 out of 7)
- **Classroom Row of Desks Daylight**: 37.50% incoherent (3 out of 8)
- **Garage Workshop Tools on Pegboard**: 87.50% incoherent (7 out of 8)
- **Green Park Lawn Afternoon Light**: 22.22% incoherent (2 out of 9)
- **Hotel Room Desk Area**: 30.00% incoherent (3 out of 10)

## 2 Recurring error patterns
- **Misalignment with Context**: Many images show predictions that focus on contextually irrelevant items (e.g., tools in a garage instead of the intended object).
- **Overgeneralization**: The model often predicts generic or common items (like "soap dispenser" or "hammer") rather than the specific objects described in the prompts.
- **Lack of Object Recognition**: The model struggles to recognize and prioritize the main object in the prompt, leading to incoherent outputs.

## 3 Detailed list of incoherent images
1. **File Name**: dataset/images/ceramiccoffeemug__bathroom__001.png  
   **Prompt Summary**: A neutral ceramic coffee mug in a bathroom vanity matte tiles background  
   **Three Worst Labels**: soap dispenser, washbasin, tub  
   **Explanation**: Predictions focus on bathroom items, not the coffee mug requested.

2. **File Name**: dataset/images/ceramiccoffeemug__garage__001.png  
   **Prompt Summary**: A neutral ceramic coffee mug in a garage workshop tools on pegboard background  
   **Three Worst Labels**: hammer, screwdriver, pillow  
   **Explanation**: Predictions are unrelated to the prompt, focusing on tools and objects not mentioned.

3. **File Name**: dataset/images/ceramiccoffeemug__kitchen__001.png  
   **Prompt Summary**: A neutral ceramic coffee mug in a kitchen countertop daylight background  
   **Three Worst Labels**: medicine chest, espresso maker, lotion  
   **Explanation**: Predictions include various kitchen items, but only one directly matches the prompt.

4. **File Name**: dataset/images/ceramiccoffeemug__minimalist__001.png  
   **Prompt Summary**: A neutral ceramic coffee mug in a minimalist living-room corner background  
   **Three Worst Labels**: television, iPod, home theater  
   **Explanation**: Predictions do not align with the prompt; items are unrelated to a coffee mug or minimalist living room.

5. **File Name**: dataset/images/ceramiccoffeemug__modern__002.png  
   **Prompt Summary**: A neutral ceramic coffee mug in a modern office desk background  
   **Three Worst Labels**: loudspeaker, Polaroid camera, CD player  
   **Explanation**: Predictions do not align with the prompt; items are unrelated to a coffee mug or office setting.

6. **File Name**: dataset/images/notebookwithkraftcover__garage__001.png  
   **Prompt Summary**: A neutral notebook with kraft cover in a garage workshop tools on pegboard background  
   **Three Worst Labels**: hammer, carpenter's kit, pencil sharpener  
   **Explanation**: Predictions focus on tools but lack direct reference to the notebook or pegboard.

7. **File Name**: dataset/images/notebookwithkraftcover__green__001.png  
   **Prompt Summary**: A neutral notebook with kraft cover in a green park lawn afternoon light background  
   **Three Worst Labels**: binder, lighter, book jacket  
   **Explanation**: Predictions do not align with the prompt's description of a notebook in a park.

8. **File Name**: dataset/images/notebookwithkraftcover__hotel__002.png  
   **Prompt Summary**: A neutral notebook with kraft cover in a hotel room desk area background  
   **Three Worst Labels**: loudspeaker, home theater, cleaver  
   **Explanation**: Predictions do not align with the prompt's description of a notebook and hotel room.

9. **File Name**: dataset/images/opaquemetalwaterbottle__bathroom__001.png  
   **Prompt Summary**: A neutral opaque metal water bottle in a bathroom vanity matte tiles background  
   **Three Worst Labels**: soap dispenser, cocktail shaker, coffeepot  
   **Explanation**: Predictions do not align with the prompt; items are unrelated to a water bottle.

10. **File Name**: dataset/images/softcouchpillow__classroom__001.png  
    **Prompt Summary**: A neutral soft couch pillow in a classroom row of desks daylight background  
    **Three Worst Labels**: mouse, studio couch, bathtub  
    **Explanation**: Predictions are unrelated to the prompt, focusing on furniture and appliances instead of a couch pillow.

## 4 Target class logit analysis (Full Details)
### Class `pillow` (ImageNet #721)
- **Number of activations**: 91
- **Average logit**: 3.65 (std: 4.02)
- **Top‑5 activations**:
  - `dataset/images/softcouchpillow__modern__001.png` → logit=14.17
  - `dataset/images/softcouchpillow__green__002.png` → logit=13.05
  - `dataset/images/softcouchpillow__kitchen__002.png` → logit=12.28
  - `dataset/images/softcouchpillow__modern__002.png` → logit=11.82
  - `dataset/images/softcouchpillow__green__001.png` → logit=11.74

### Class `toilet seat` (ImageNet #861)
- **Number of activations**: 91
- **Average logit**: 4.42 (std: 2.78)
- **Top‑5 activations**:
  - `dataset/images/softcouchpillow__minimalist__001.png` → logit=12.37
  - `dataset/images/ceramiccoffeemug__bathroom__001.png` → logit=10.20
  - `dataset/images/ceramiccoffeemug__hotel__001.png` → logit=9.65
  - `dataset/images/softcouchpillow__classroom__001.png` → logit=9.57
  - `dataset/images/tablelampwithshadeoff__bathroom__002.png` → logit=8.97

### Class `park bench` (ImageNet #703)
- **Number of activations**: 91
- **Average logit**: 0.36 (std: 2.07)
- **Top‑5 activations**:
  - `dataset/images/tablelampwithshadeoff__classroom__002.png` → logit=9.02
  - `dataset/images/tablelampwithshadeoff__green__001.png` → logit=5.06
  - `dataset/images/ceramiccoffeemug__modern__002.png` → logit=4.34
  - `dataset/images/opaquemetalwaterbottle__green__001.png` → logit=3.59
  - `dataset/images/softcouchpillow__modern__001.png` → logit=3.50

### Class `laptop` (ImageNet #620)
- **Number of activations**: 91
- **Average logit**: 5.10 (std: 2.56)
- **Top‑5 activations**:
  - `dataset/images/notebookwithkraftcover__science__001.png` → logit=13.48
  - `dataset/images/notebookwithkraftcover__minimalist__002.png` → logit=12.49
  - `dataset/images/notebookwithkraftcover__hotel__001.png` → logit=10.62
  - `dataset/images/notebookwithkraftcover__hotel__002.png` → logit=9.17
  - `dataset/images/softcouchpillow__modern__001.png` → logit=9.17

### Class `fox squirrel` (ImageNet #335)
- **Number of activations**: 91
- **Average logit**: -3.06 (std: 1.74)
- **Top‑5 activations**:
  - `dataset/images/tablelampwithshadeoff__green__002.png` → logit=1.40
  - `dataset/images/opaquemetalwaterbottle__green__002.png` → logit=0.63
  - `dataset/images/ceramiccoffeemug__modern__002.png` → logit=0.34
  - `dataset/images/opaquemetalwaterbottle__science__002.png` → logit=0.12
  - `dataset/images/opaquemetalwaterbottle__kitchen__002.png` → logit=-0.28

### Class `tennis ball` (ImageNet #852)
- **Number of activations**: 91
- **Average logit**: 2.97 (std: 2.44)
- **Top‑5 activations**:
  - `dataset/images/opaquemetalwaterbottle__green__002.png` → logit=9.01
  - `dataset/images/opaquemetalwaterbottle__green__001.png` → logit=8.42
  - `dataset/images/opaquemetalwaterbottle__kitchen__001.png` → logit=8.03
  - `dataset/images/opaquemetalwaterbottle__classroom__001.png` → logit=7.58
  - `dataset/images/opaquemetalwaterbottle__classroom__002.png` → logit=7.54

## 5 Main biases of the model
1. **Contextual Bias**: The model often misinterprets the context, leading to predictions that focus on irrelevant items (e.g., tools in a garage instead of the main object).
2. **Object Recognition Bias**: The model struggles to correctly identify and prioritize the main object in the prompt, often leading to incoherent outputs.
3. **Overgeneralization Bias**: The model tends to predict common items rather than specific objects, which can lead to misalignment with the prompts.

## 6 Overall verdict
- **Strengths**:
  - Capable of generating a variety of predictions.
  - Shows some ability to recognize common objects in certain contexts.

- **Weaknesses**:
  - High percentage of incoherent outputs (41.76%).
  - Frequent misalignment with prompts and contexts.
  - Systematic biases in object recognition and contextual understanding.

- **Reliability Rating**: 2/5