## 1 Aggregate statistics
- **Total Images**: 121
- **Mean Score**: 0.469
- **Median Score**: 0.4
- **Standard Deviation of Score**: 0.095
- **Percentage of Incoherent Images**: 65.29%
  
### Object Incoherence Statistics
- **Bookjacket**: 60% incoherent (9/15)
- **Ceramic Coffee Mug**: 12.5% incoherent (2/16)
- **Granny Smith Apple**: 66.67% incoherent (10/15)
- **Notebook with Kraft Cover**: 100% incoherent (15/15)
- **Opaque Metal Water Bottle**: 30% incoherent (6/20)
- **Soft Couch Pillow**: 85% incoherent (17/20)
- **Table Lamp with Shade Off**: 100% incoherent (20/20)

### Context Incoherence Statistics
- **Classroom**: 66.67% incoherent (8/12)
- **Garage**: 90% incoherent (9/10)
- **Green**: 66.67% incoherent (8/12)
- **Hotel**: 92.86% incoherent (13/14)
- **Kitchen**: 66.67% incoherent (8/12)
- **Minimalist**: 35.71% incoherent (5/14)
- **Modern**: 64.29% incoherent (9/14)
- **Plain**: 28.57% incoherent (4/14)
- **Science**: 63.64% incoherent (7/11)
- **Bathroom**: 100% incoherent (8/8)

## 2 Recurring error patterns
The model **resnet18** exhibits the following recurring error patterns:
- **Contextual Misalignment**: Many images are misclassified due to unclear contextual cues, particularly in settings like bathrooms and garages where the model fails to accurately interpret the scene.
- **Object Ambiguity**: The model struggles with neutral objects such as bookjackets and notebooks, often failing to distinguish their specific characteristics, leading to incoherent outputs.
- **High Incoherence Rates**: Certain object categories (e.g., notebook with kraft cover and table lamp with shade off) show 100% incoherence, indicating a systematic bias in recognizing these objects in various contexts.

## 3 Detailed list of incoherent images
| File Name | Prompt Summary | Worst Labels | Explanation |
|-----------|----------------|--------------|-------------|
| images/bookjacket__classroom__001.png | Neutral bookjacket in classroom | None | Predictions suggest a classroom setting, but the bookjacket's neutrality is unclear. |
| images/bookjacket__classroom__002.png | Neutral bookjacket in classroom | None | Predictions suggest a classroom setting, but the neutral bookjacket aspect is unclear. |
| images/bookjacket__garage__002.png | Neutral bookjacket in garage | None | Predictions suggest a neutral design, but the garage context is unclear. |
| images/bookjacket__green__001.png | Neutral bookjacket in green | None | Predictions suggest a neutral design, but lack specific references to a bookjacket or green background. |
| images/bookjacket__green__002.png | Neutral bookjacket in green | None | Predictions suggest a neutral design, but lack specific reference to a bookjacket. |
| images/bookjacket__hotel__001.png | Neutral bookjacket in hotel | None | Predictions suggest a hotel setting, but lack specific references to a neutral bookjacket. |
| images/bookjacket__hotel__002.png | Neutral bookjacket in hotel | None | Predictions suggest a hotel setting but lack specific details about a neutral bookjacket. |
| images/bookjacket__kitchen__002.png | Neutral bookjacket in kitchen | None | Predictions suggest a kitchen setting, but lack specific references to a neutral bookjacket. |
| images/bookjacket__modern__001.png | Neutral bookjacket in modern | None | Predictions suggest a modern aesthetic, but lack specific references to a bookjacket. |
| images/ceramiccoffeemug__bathroom__001.png | Neutral ceramic mug in bathroom | None | Predictions suggest a coffee mug, but the bathroom context is unclear. |
| images/ceramiccoffeemug__hotel__002.png | Neutral ceramic mug in hotel | None | Predictions include a coffee mug, aligning with the prompt's description. |
| images/grannysmith__bathroom__002.png | Neutral granny smith in bathroom | None | The model identifies a granny smith apple, but the bathroom context is unclear. |
| images/grannysmith__classroom__001.png | Neutral granny smith in classroom | None | The model identifies a granny smith apple in a classroom setting, aligning with the prompt. |
| images/grannysmith__classroom__002.png | Neutral granny smith in classroom | None | The model identifies a granny smith apple, but the classroom context is unclear. |
| images/grannysmith__garage__001.png | Neutral granny smith in garage | None | Predictions include apple and garage-related items, indicating some alignment with the prompt. |
| images/grannysmith__hotel__001.png | Neutral granny smith in hotel | None | The model identifies a granny smith apple but lacks clear hotel context. |
| images/grannysmith__hotel__002.png | Neutral granny smith in hotel | None | The model identified a granny smith apple but struggled with the hotel context. |
| images/grannysmith__kitchen__002.png | Neutral granny smith in kitchen | None | The model identifies kitchen elements but lacks specific focus on a neutral Granny Smith apple. |
| images/grannysmith__modern__001.png | Neutral granny smith in modern | None | The model identifies a granny smith apple but lacks clarity on the modern background. |
| images/grannysmith__modern__002.png | Neutral granny smith in modern | None | The model identifies a granny smith apple, but the modern background is unclear. |
| images/notebookwithkraftcover__garage__001.png | Neutral notebook in garage | None | The predictions suggest a neutral object in a garage, aligning with the prompt's description. |
| images/notebookwithkraftcover__green__001.png | Neutral notebook in green | None | The predictions suggest a neutral notebook, but the kraft cover and green background are not explicitly identified. |
| images/notebookwithkraftcover__green__002.png | Neutral notebook in green | None | The predictions suggest a neutral object, but the specific details of the notebook and background are unclear. |
| images/notebookwithkraftcover__hotel__001.png | Neutral notebook in hotel | None | The model identifies a notebook but lacks clarity on the hotel background. |
| images/notebookwithkraftcover__hotel__002.png | Neutral notebook in hotel | None | The predictions suggest a notebook, but the hotel background is unclear. |
| images/notebookwithkraftcover__kitchen__001.png | Neutral notebook in kitchen | None | The predictions suggest a notebook, but the kitchen background is unclear. |
| images/notebookwithkraftcover__kitchen__002.png | Neutral notebook in kitchen | None | The model identifies a notebook but lacks clarity on the kraft cover and kitchen context. |
| images/notebookwithkraftcover__minimalist__001.png | Neutral notebook in minimalist | None | The predictions suggest a neutral aesthetic, but lack specific details about the kraft cover. |
| images/notebookwithkraftcover__minimalist__002.png | Neutral notebook in minimalist | None | The predictions suggest a neutral aesthetic, but lack specific details about the kraft cover. |
| images/notebookwithkraftcover__modern__001.png | Neutral notebook in modern | None | The predictions suggest a neutral notebook, but the modern background is unclear. |
| images/notebookwithkraftcover__modern__002.png | Neutral notebook in modern | None | The predictions suggest a modern aesthetic, but the specific details of the notebook are unclear. |
| images/notebookwithkraftcover__plain__001.png | Neutral notebook in plain | None | The predictions suggest a neutral notebook, but the kraft cover and plain background are not explicitly identified. |
| images/notebookwithkraftcover__plain__002.png | Neutral notebook in plain | None | The predictions suggest a neutral object, but lack specific details about the notebook and its cover. |
| images/notebookwithkraftcover__science__001.png | Neutral notebook in science | None | The predictions suggest a neutral notebook, but the science background is less clear. |
| images/notebookwithkraftcover__science__002.png | Neutral notebook in science | None | The predictions suggest a neutral notebook, but the science background is unclear. |
| images/opaquemetalwaterbottle__bathroom__001.png | Neutral water bottle in bathroom | None | The model identifies a water bottle in a bathroom setting, aligning with the prompt's description. |
| images/opaquemetalwaterbottle__bathroom__002.png | Neutral water bottle in bathroom | None | The model identifies a water bottle in a bathroom setting, aligning with the prompt's description. |
| images/opaquemetalwaterbottle__garage__001.png | Neutral water bottle in garage | None | The model identified a water bottle in a garage setting, aligning with the prompt's description. |
| images/opaquemetalwaterbottle__garage__002.png | Neutral water bottle in garage | None | The model identifies a water bottle in a garage setting, aligning with the prompt's description. |
| images/opaquemetalwaterbottle__hotel__001.png | Neutral water bottle in hotel | None | The model identifies a water bottle in a hotel setting, aligning with the prompt's description. |
| images/opaquemetalwaterbottle__hotel__002.png | Neutral water bottle in hotel | None | Predictions include water bottle and hotel elements, indicating partial alignment with the prompt. |
| images/softcouchpillow__bathroom__001.png | Neutral soft pillow in bathroom | None | The predictions suggest a soft object in a bathroom setting, aligning with the prompt's description. |
| images/softcouchpillow__bathroom__002.png | Neutral soft pillow in bathroom | None | The model identifies a soft object in a bathroom setting, aligning with the prompt's description. |
| images/softcouchpillow__classroom__001.png | Neutral soft pillow in classroom | None | The model identifies a soft object in a classroom setting, aligning with the prompt's description. |
| images/softcouchpillow__classroom__002.png | Neutral soft pillow in classroom | None | The model identified a soft object in a classroom setting, aligning with the prompt's description. |
| images/softcouchpillow__garage__001.png | Neutral soft pillow in garage | None | The model identifies a soft object in a garage setting, aligning with the prompt's description. |
| images/softcouchpillow__garage__002.png | Neutral soft pillow in garage | None | The model identifies a soft object in a garage setting, aligning with the prompt's description. |
| images/softcouchpillow__green__001.png | Neutral soft pillow in green | None | The model identifies a soft object in a green setting, aligning with the prompt's description. |
| images/softcouchpillow__green__002.png | Neutral soft pillow in green | None | The model identifies a soft object in a green setting, aligning with the prompt's description. |
| images/softcouchpillow__hotel__001.png | Neutral soft pillow in hotel | None | The model identifies a soft pillow in a hotel setting, aligning with the prompt's description. |
| images/softcouchpillow__hotel__002.png | Neutral soft pillow in hotel | None | The model identifies a soft pillow in a hotel setting, aligning with the prompt's description. |
| images/softcouchpillow__kitchen__001.png | Neutral soft pillow in kitchen | None | The predictions suggest a soft object in a kitchen, aligning with the prompt's description. |
| images/softcouchpillow__kitchen__002.png | Neutral soft pillow in kitchen | None | The model identifies a soft pillow in a kitchen setting, aligning with the prompt's description. |
| images/softcouchpillow__minimalist__002.png | Neutral soft pillow in minimalist | None | The predictions suggest a soft object in a simple setting, aligning with the prompt's description. |
| images/softcouchpillow__modern__001.png | Neutral soft pillow in modern | None | The predictions suggest a soft pillow in a modern setting, aligning with the prompt's description. |
| images/softcouchpillow__modern__002.png | Neutral soft pillow in modern | None | The predictions suggest a soft pillow in a modern setting, aligning with the prompt's description. |
| images/softcouchpillow__science__001.png | Neutral soft pillow in science | None | The predictions suggest a soft object in a scientific setting, aligning with the prompt's description. |
| images/softcouchpillow__science__002.png | Neutral soft pillow in science | None | The predictions suggest a soft object in a scientific context, aligning with the prompt's description. |
| images/tablelampwithshadeoff__bathroom__001.png | Neutral lamp in bathroom | None | The predictions suggest a lamp in a bathroom, aligning with the prompt's description. |
| images/tablelampwithshadeoff__bathroom__002.png | Neutral lamp in bathroom | None | The predictions suggest a lamp in a bathroom, aligning with the prompt's description. |
| images/tablelampwithshadeoff__classroom__001.png | Neutral lamp in classroom | None | Predictions include items related to lamps and classroom settings, indicating some alignment with the prompt. |
| images/tablelampwithshadeoff__classroom__002.png | Neutral lamp in classroom | None | Predictions include relevant classroom elements, but the lamp description lacks clarity. |
| images/tablelampwithshadeoff__garage__001.png | Neutral lamp in garage | None | The model identifies a lamp in a garage setting, aligning with the prompt's description. |
| images/tablelampwithshadeoff__garage__002.png | Neutral lamp in garage | None | Predictions include items related to lamps and garage settings, indicating some alignment with the prompt. |
| images/tablelampwithshadeoff__green__001.png | Neutral lamp in green | None | The model identifies a lamp but lacks clarity on the shade and background details. |
| images/tablelampwithshadeoff__green__002.png | Neutral lamp in green | None | The model identifies a lamp but lacks clarity on the shade and background color. |
| images/tablelampwithshadeoff__hotel__001.png | Neutral lamp in hotel | None | Predictions include items related to lamps and hotel settings, indicating some alignment with the prompt. |
| images/tablelampwithshadeoff__hotel__002.png | Neutral lamp in hotel | None | Predictions include items related to lamps and hotel settings, indicating partial alignment with the prompt. |
| images/tablelampwithshadeoff__kitchen__001.png | Neutral lamp in kitchen | None | Predictions include kitchen items, but lack specific mention of a table lamp or shade. |
| images/tablelampwithshadeoff__kitchen__002.png | Neutral lamp in kitchen | None | Predictions include kitchen elements, but the lamp description lacks clarity. |
| images/tablelampwithshadeoff__minimalist__001.png | Neutral lamp in minimalist | None | The predictions suggest a lamp, but the description lacks clarity on the minimalist background. |
| images/tablelampwithshadeoff__minimalist__002.png | Neutral lamp in minimalist | None | Predictions include relevant elements like 'lamp' and 'minimalist', aligning with the prompt's description. |
| images/tablelampwithshadeoff__modern__001.png | Neutral lamp in modern | None | The predictions include elements of a lamp but lack clarity on the modern background. |
| images/tablelampwithshadeoff__modern__002.png | Neutral lamp in modern | None | Predictions include relevant elements like 'lamp' and 'modern', but lack clarity on 'shade off'. |
| images/tablelampwithshadeoff__plain__001.png | Neutral lamp in plain | None | Predictions include lamp-related items, indicating some alignment with the prompt. |
| images/tablelampwithshadeoff__plain__002.png | Neutral lamp in plain | None | The predictions suggest a lamp, but the description lacks clarity on the shade and background. |
| images/tablelampwithshadeoff__science__001.png | Neutral lamp in science | None | Predictions suggest a lamp in a scientific setting, aligning with the prompt's description. |
| images/tablelampwithshadeoff__science__002.png | Neutral lamp in science | None | Predictions include relevant objects, but may not fully capture the specific scene described. |

## 4 Target class logit analysis (Full Details)
### Class `pillow` (ImageNet #721)
- **Number of activations**: 121
- **Average logit**: 3.15 (std: 5.17)
- **Top‑5 activations**:
  - `dataset/images/softcouchpillow__modern__002.png` → logit=20.01
  - `dataset/images/softcouchpillow__garage__002.png` → logit=19.52
  - `dataset/images/softcouchpillow__kitchen__002.png` → logit=17.80
  - `dataset/images/softcouchpillow__green__001.png` → logit=17.58
  - `dataset/images/softcouchpillow__hotel__002.png` → logit=17.07

### Class `toilet seat` (ImageNet #861)
- **Number of activations**: 121
- **Average logit**: 3.29 (std: 2.02)
- **Top‑5 activations**:
  - `dataset/images/ceramiccoffeemug__bathroom__001.png` → logit=11.01
  - `dataset/images/tablelampwithshadeoff__bathroom__002.png` → logit=8.86
  - `dataset/images/opaquemetalwaterbottle__bathroom__001.png` → logit=8.83
  - `dataset/images/softcouchpillow__minimalist__001.png` → logit=8.34
  - `dataset/images/ceramiccoffeemug__kitchen__002.png` → logit=7.98

### Class `park bench` (ImageNet #703)
- **Number of activations**: 121
- **Average logit**: -0.16 (std: 2.08)
- **Top‑5 activations**:
  - `dataset/images/tablelampwithshadeoff__classroom__002.png` → logit=8.85
  - `dataset/images/softcouchpillow__garage__001.png` → logit=5.57
  - `dataset/images/softcouchpillow__modern__001.png` → logit=4.89
  - `dataset/images/softcouchpillow__science__001.png` → logit=4.82
  - `dataset/images/grannysmith__classroom__001.png` → logit=4.10

### Class `laptop` (ImageNet #620)
- **Number of activations**: 121
- **Average logit**: 4.11 (std: 2.77)
- **Top‑5 activations**:
  - `dataset/images/bookjacket__science__001.png` → logit=13.14
  - `dataset/images/notebookwithkraftcover__kitchen__001.png` → logit=11.23
  - `dataset/images/bookjacket__kitchen__002.png` → logit=10.82
  - `dataset/images/bookjacket__green__001.png` → logit=10.53
  - `dataset/images/notebookwithkraftcover__science__001.png` → logit=8.68

### Class `fox squirrel` (ImageNet #335)
- **Number of activations**: 121
- **Average logit**: -2.42 (std: 1.65)
- **Top‑5 activations**:
  - `dataset/images/opaquemetalwaterbottle__green__002.png` → logit=2.39
  - `dataset/images/ceramiccoffeemug__green__002.png` → logit=1.78
  - `dataset/images/grannysmith__green__002.png` → logit=1.76
  - `dataset/images/tablelampwithshadeoff__kitchen__001.png` → logit=1.71
  - `dataset/images/ceramiccoffeemug__plain__002.png` → logit=0.38

### Class `tennis ball` (ImageNet #852)
- **Number of activations**: 121
- **Average logit**: 2.61 (std: 2.12)
- **Top‑5 activations**:
  - `dataset/images/grannysmith__plain__002.png` → logit=9.89
  - `dataset/images/grannysmith__green__002.png` → logit=8.59
  - `dataset/images/grannysmith__minimalist__001.png` → logit=8.36
  - `dataset/images/grannysmith__plain__001.png` → logit=8.02
  - `dataset/images/grannysmith__minimalist__002.png` → logit=7.87

## 5 Main biases of the model
1. **Contextual Bias**: The model struggles with specific contexts, particularly in bathrooms and garages, leading to high incoherence rates.
   - *Example*: High incoherence for images featuring notebooks in kitchen settings.
   
2. **Object Recognition Bias**: Certain objects, especially neutral ones like bookjackets and notebooks, are frequently misclassified or lack clarity in their representation.
   - *Example*: 100% incoherence for notebook images across various contexts.

3. **Color and Aesthetic Bias**: The model often fails to accurately interpret the significance of color and design aesthetics, particularly in minimalist or modern settings.
   - *Example*: Misclassification of soft pillows in modern backgrounds, leading to incoherent outputs.

## 6 Overall verdict
- **Strengths**:
  - Reasonably good performance on clear and distinct objects.
  - Some alignment with prompts in familiar contexts.

- **Weaknesses**:
  - High incoherence rates, especially in ambiguous or complex scenes.
  - Systematic biases in recognizing neutral objects and contextual cues.

- **Final Reliability Rating**: 2/5