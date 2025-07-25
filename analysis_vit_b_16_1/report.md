## 1 Aggregate statistics
- **Total Images**: 121
- **Mean Score**: 0.41
- **Median Score**: 0.40
- **Standard Deviation of Score**: 0.22
- **Percentage of Incoherent Images**: 27.27%

### Object Incoherence Statistics
- **Book Jacket**: 53.33% incoherent (8/15)
- **Ceramic Coffee Mug**: 6.25% incoherent (1/16)
- **Granny Smith**: 40.00% incoherent (6/15)
- **Notebook with Kraft Cover**: 73.33% incoherent (11/15)
- **Opaque Metal Water Bottle**: 25.00% incoherent (5/20)
- **Soft Couch Pillow**: 0.00% incoherent (0/20)
- **Table Lamp with Shade Off**: 10.00% incoherent (2/20)

### Context Incoherence Statistics
- **Classroom**: 16.67% incoherent (2/12)
- **Garage**: 40.00% incoherent (4/10)
- **Green**: 16.67% incoherent (2/12)
- **Hotel**: 28.57% incoherent (4/14)
- **Kitchen**: 16.67% incoherent (2/12)
- **Minimalist**: 21.43% incoherent (3/14)
- **Modern**: 57.14% incoherent (8/14)
- **Plain**: 21.43% incoherent (3/14)
- **Science**: 27.27% incoherent (3/11)
- **Bathroom**: 25.00% incoherent (2/8)

## 2 Recurring error patterns
The **vit_b_16** model exhibits several recurring error patterns linked to biases:
- **Contextual Misalignment**: Many predictions fail to align with the specified context (e.g., book jackets in garages or hotels), indicating a bias towards recognizing objects over their contextual relevance.
- **Object Overgeneralization**: The model often misclassifies items based on their general features rather than specific attributes, such as mistaking tools for a book jacket.
- **Background Influence**: Certain backgrounds, particularly modern and minimalist, lead to higher incoherence rates, suggesting a bias against these contexts where the model struggles to identify the primary object.

## 3 Detailed list of incoherent images
| File Name | Prompt Summary | Worst Labels | Explanation |
|-----------|----------------|--------------|-------------|
| images/bookjacket__garage__002.png | Neutral bookjacket in garage | hammer, screwdriver, carpenter's kit | Predictions focus on tools and objects, not a bookjacket or garage context. |
| images/bookjacket__hotel__002.png | Neutral bookjacket in hotel | window shade, cowboy hat, lampshade | Predictions are unrelated to the prompt, indicating poor alignment. |
| images/bookjacket__minimalist__002.png | Neutral bookjacket in minimalist | book jacket, binder, notebook | Predictions do not align with the prompt about a book jacket. |
| images/bookjacket__modern__001.png | Neutral bookjacket in modern | switch, envelope, wardrobe | Predictions are unrelated to the prompt about a bookjacket. |
| images/bookjacket__modern__002.png | Neutral bookjacket in modern | binder, quill, coffee mug | Predictions focus on unrelated items rather than a bookjacket in a modern background. |
| images/bookjacket__plain__001.png | Neutral bookjacket in plain | switch, buckle, book jacket | Predictions do not align with the prompt about a bookjacket. |
| images/bookjacket__plain__002.png | Neutral bookjacket in plain | bathtub, tub, lampshade | Predictions are unrelated to the prompt about a bookjacket. |
| images/bookjacket__science__001.png | Neutral bookjacket in science | book jacket, hard disc, fountain pen | Predictions are unrelated to the prompt about a book jacket in a science background. |
| images/ceramiccoffeemug__classroom__001.png | Neutral ceramic mug in classroom | espresso, cup, coffee mug | Predictions focus on coffee-related items but lack relevance to a neutral ceramic mug in a classroom. |
| images/grannysmith__bathroom__002.png | Neutral grannysmith in bathroom | bathtub, tub, washbasin | Predictions focus on bathroom items, missing the neutral grannysmith. |
| images/grannysmith__garage__001.png | Neutral grannysmith in garage | hammer, screwdriver, carpenter's kit | Predictions are unrelated to the prompt, focusing on tools instead of a Granny Smith apple. |
| images/grannysmith__minimalist__002.png | Neutral grannysmith in minimalist | table lamp, bookcase, studio couch | Predictions do not align with the prompt about a grannysmith apple. |
| images/grannysmith__modern__001.png | Neutral grannysmith in modern | wall clock, combination lock, wardrobe | Predictions do not relate to a neutral grannysmith or modern background. |
| images/grannysmith__modern__002.png | Neutral grannysmith in modern | wall clock, bottlecap, tray | Predictions do not relate to a neutral grannysmith or modern background. |
| images/grannysmith__science__002.png | Neutral grannysmith in science | menu, joystick, abacus | Predictions are largely unrelated to the prompt, indicating poor alignment. |
| images/notebookwithkraftcover__garage__001.png | Neutral notebook in garage | hammer, screwdriver, carpenter's kit | Predictions focus on tools, not the requested notebook or garage context. |
| images/notebookwithkraftcover__green__001.png | Neutral notebook in green | book jacket, binder, envelope | Predictions do not align with the prompt about a notebook. |
| images/notebookwithkraftcover__green__002.png | Neutral notebook in green | ballpoint, rubber eraser, cup | Predictions do not align with the prompt about a notebook. |
| images/notebookwithkraftcover__hotel__001.png | Neutral notebook in hotel | ballpoint, rubber eraser, rule | Predictions do not align with the prompt about a notebook in a hotel background. |
| images/notebookwithkraftcover__hotel__002.png | Neutral notebook in hotel | binder, envelope, coffee mug | Predictions do not align with the prompt, focusing on unrelated items. |
| images/notebookwithkraftcover__kitchen__001.png | Neutral notebook in kitchen | fountain pen, ballpoint, binder | Predictions mostly unrelated to the prompt, lacking focus on the notebook and kitchen context. |
| images/notebookwithkraftcover__kitchen__002.png | Neutral notebook in kitchen | loudspeaker, binder, orange | Predictions do not align with the prompt; items are unrelated to a notebook or kitchen. |
| images/notebookwithkraftcover__minimalist__002.png | Neutral notebook in minimalist | binder, book jacket, ballpoint | Predictions mostly unrelated to the prompt, indicating poor alignment. |
| images/notebookwithkraftcover__modern__001.png | Neutral notebook in modern | envelope, binder, rubber eraser | Predictions do not align with the prompt about a notebook with a kraft cover. |
| images/notebookwithkraftcover__modern__002.png | Neutral notebook in modern | rule, rubber eraser, envelope | Predictions do not align with the prompt, focusing on unrelated items. |
| images/notebookwithkraftcover__science__002.png | Neutral notebook in science | ballpoint, rule, rubber eraser | Predictions are unrelated to the prompt about a notebook. |
| images/opaquemetalwaterbottle__bathroom__002.png | Neutral water bottle in bathroom | soap dispenser, lotion, cocktail shaker | Predictions do not align with the prompt; items are unrelated to a metal water bottle. |
| images/opaquemetalwaterbottle__hotel__001.png | Neutral water bottle in hotel | water bottle, saltshaker, cocktail shaker | Predictions mostly unrelated to the prompt, lacking a clear representation of a water bottle. |
| images/opaquemetalwaterbottle__modern__001.png | Neutral water bottle in modern | cocktail shaker, water bottle, soap dispenser | Predictions mostly misalign with the prompt, focusing on unrelated items. |
| images/opaquemetalwaterbottle__modern__002.png | Neutral water bottle in modern | joystick, microphone, water bottle | Predictions include unrelated items, indicating poor alignment with the prompt. |
| images/opaquemetalwaterbottle__plain__001.png | Neutral water bottle in plain | pill bottle, saltshaker, syringe | Predictions mostly misalign with the prompt, focusing on unrelated items. |
| images/tablelampwithshadeoff__classroom__002.png | Neutral table lamp in classroom | dining table, library, folding chair | Predictions do not align with the prompt; items listed are unrelated to a table lamp. |
| images/tablelampwithshadeoff__garage__001.png | Neutral table lamp in garage | screwdriver, power drill, pencil sharpener | Predictions do not align with the prompt about a table lamp. |

## 4 Target class logit analysis (Full Details)
### Class `pillow` (ImageNet #721)
- **Average logit**: 1.16 (std: 3.38)
- **Top‑5 activations**:
  - `dataset/images/softcouchpillow__plain__001.png` → logit=9.78
  - `dataset/images/softcouchpillow__kitchen__001.png` → logit=9.51
  - `dataset/images/softcouchpillow__bathroom__001.png` → logit=9.41
  - `dataset/images/softcouchpillow__kitchen__002.png` → logit=9.17
  - `dataset/images/softcouchpillow__modern__002.png` → logit=9.12

### Class `toilet seat` (ImageNet #861)
- **Average logit**: -0.19 (std: 1.08)
- **Top‑5 activations**:
  - `dataset/images/ceramiccoffeemug__bathroom__001.png` → logit=4.79
  - `dataset/images/softcouchpillow__minimalist__001.png` → logit=2.89
  - `dataset/images/opaquemetalwaterbottle__bathroom__001.png` → logit=2.69
  - `dataset/images/bookjacket__plain__002.png` → logit=2.59
  - `dataset/images/ceramiccoffeemug__kitchen__001.png` → logit=1.91

### Class `park bench` (ImageNet #703)
- **Average logit**: 0.06 (std: 0.56)
- **Top‑5 activations**:
  - `dataset/images/softcouchpillow__science__001.png` → logit=1.83
  - `dataset/images/tablelampwithshadeoff__garage__002.png` → logit=1.72
  - `dataset/images/tablelampwithshadeoff__classroom__002.png` → logit=1.68
  - `dataset/images/softcouchpillow__green__001.png` → logit=1.13
  - `dataset/images/opaquemetalwaterbottle__green__002.png` → logit=1.01

### Class `laptop` (ImageNet #620)
- **Average logit**: 0.81 (std: 1.37)
- **Top‑5 activations**:
  - `dataset/images/bookjacket__green__001.png` → logit=5.86
  - `dataset/images/notebookwithkraftcover__science__001.png` → logit=5.54
  - `dataset/images/bookjacket__kitchen__002.png` → logit=5.27
  - `dataset/images/ceramiccoffeemug__modern__001.png` → logit=4.38
  - `dataset/images/notebookwithkraftcover__modern__001.png` → logit=4.26

### Class `fox squirrel` (ImageNet #335)
- **Average logit**: -0.05 (std: 0.34)
- **Top‑5 activations**:
  - `dataset/images/grannysmith__green__002.png` → logit=0.71
  - `dataset/images/softcouchpillow__modern__002.png` → logit=0.70
  - `dataset/images/softcouchpillow__science__002.png` → logit=0.59
  - `dataset/images/grannysmith__bathroom__002.png` → logit=0.53
  - `dataset/images/ceramiccoffeemug__kitchen__002.png` → logit=0.49

### Class `tennis ball` (ImageNet #852)
- **Average logit**: 0.23 (std: 0.85)
- **Top‑5 activations**:
  - `dataset/images/grannysmith__hotel__002.png` → logit=3.52
  - `dataset/images/grannysmith__green__002.png` → logit=3.39
  - `dataset/images/grannysmith__classroom__001.png` → logit=2.46
  - `dataset/images/grannysmith__minimalist__002.png` → logit=2.44
  - `dataset/images/ceramiccoffeemug__green__002.png` → logit=2.03

## 5 Main biases of the model
1. **Contextual Bias**: The model often fails to recognize the relevance of the background context, leading to incoherent predictions. For instance, it misidentifies objects in settings like garages or hotels.
2. **Object Recognition Bias**: The model tends to overgeneralize object features, mistaking tools for items like book jackets or notebooks, which indicates a lack of specificity in object recognition.
3. **Background Influence Bias**: Certain backgrounds, especially modern and minimalist, correlate with higher incoherence rates, suggesting a bias against these contexts where the model struggles to identify the primary object.

## 6 Overall verdict
- **Strengths**:
  - High performance on certain object classes (e.g., soft couch pillow).
  - Consistent identification of common objects in familiar contexts.

- **Weaknesses**:
  - Significant incoherence in diverse backgrounds.
  - Overgeneralization in object recognition leading to misclassifications.
  - Contextual misalignment affecting overall accuracy.

- **Final Reliability Rating**: 2/5