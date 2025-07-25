## 1 Aggregate statistics
- **Total Images**: 121
- **Mean Score**: 0.31
- **Median Score**: 0.33
- **Standard Deviation of Score**: 0.21
- **Percentage of Incoherent Images**: 48.76%
- **Object Incoherence**:
  - Bookjacket: 80%
  - Ceramic Coffee Mug: 31.25%
  - Granny Smith: 73.33%
  - Notebook with Kraft Cover: 60%
  - Opaque Metal Water Bottle: 40%
  - Soft Couch Pillow: 55%
  - Table Lamp with Shade Off: 15%
- **Context Incoherence**:
  - Classroom: 58.33%
  - Garage: 90%
  - Green: 33.33%
  - Hotel: 50%
  - Kitchen: 41.67%
  - Minimalist: 35.71%
  - Modern: 57.14%
  - Plain: 35.71%
  - Science: 45.45%
  - Bathroom: 50%

## 2 Recurring error patterns
- **Misalignment with Prompts**: Many images scored below 0.3 show predictions that do not correlate with the provided prompts, indicating a lack of contextual understanding.
- **Object Confusion**: The model often confuses similar objects, such as mistaking a bookjacket for unrelated items like a laptop or envelope.
- **Contextual Misinterpretation**: The model struggles to relate objects to their specified contexts (e.g., a bookjacket in a classroom), leading to incoherent predictions.

## 3 Detailed list of incoherent images
1. **File Name**: images/bookjacket__classroom__001.png  
   **Prompt Summary**: A neutral bookjacket in a classroom background  
   **Three Worst Labels**: envelope, paintbrush, iPod  
   **Explanation**: Predictions do not align with the prompt; items are unrelated to a bookjacket or classroom.

2. **File Name**: images/bookjacket__classroom__002.png  
   **Prompt Summary**: A neutral bookjacket in a classroom background  
   **Three Worst Labels**: wooden spoon, iPod, marimba  
   **Explanation**: Predictions do not align with the prompt about a bookjacket in a classroom.

3. **File Name**: images/bookjacket__garage__002.png  
   **Prompt Summary**: A neutral bookjacket in a garage background  
   **Three Worst Labels**: fountain pen, revolver, radio  
   **Explanation**: Predictions are unrelated to a bookjacket or garage context.

4. **File Name**: images/bookjacket__green__002.png  
   **Prompt Summary**: A neutral bookjacket in a green background  
   **Three Worst Labels**: envelope, laptop, binder  
   **Explanation**: Predictions do not align with the prompt about a bookjacket.

5. **File Name**: images/bookjacket__hotel__001.png  
   **Prompt Summary**: A neutral bookjacket in a hotel background  
   **Three Worst Labels**: table lamp, studio couch, lampshade  
   **Explanation**: Predictions focus on furniture and electronics, not a bookjacket or hotel context.

6. **File Name**: images/bookjacket__hotel__002.png  
   **Prompt Summary**: A neutral bookjacket in a hotel background  
   **Three Worst Labels**: binder, shoji, quill  
   **Explanation**: Predictions do not align with the prompt about a bookjacket in a hotel background.

7. **File Name**: images/bookjacket__minimalist__002.png  
   **Prompt Summary**: A neutral bookjacket in a minimalist background  
   **Three Worst Labels**: dishwasher, refrigerator, paper towel  
   **Explanation**: Predictions are unrelated to a bookjacket or minimalist background.

8. **File Name**: images/bookjacket__modern__001.png  
   **Prompt Summary**: A neutral bookjacket in a modern background  
   **Three Worst Labels**: lighter, binder, medicine chest  
   **Explanation**: Predictions do not align with the concept of a bookjacket or modern background.

9. **File Name**: images/bookjacket__modern__002.png  
   **Prompt Summary**: A neutral bookjacket in a modern background  
   **Three Worst Labels**: fountain pen, binder, violin  
   **Explanation**: Predictions do not align with the prompt about a bookjacket.

10. **File Name**: images/bookjacket__plain__001.png  
    **Prompt Summary**: A neutral bookjacket in a plain background  
    **Three Worst Labels**: switch, iPod, loudspeaker  
    **Explanation**: Predictions do not align with the concept of a neutral bookjacket.

11. **File Name**: images/bookjacket__plain__002.png  
    **Prompt Summary**: A neutral bookjacket in a plain background  
    **Three Worst Labels**: lampshade, table lamp, ping-pong ball  
    **Explanation**: Predictions are unrelated to a bookjacket or plain background.

12. **File Name**: images/bookjacket__science__001.png  
    **Prompt Summary**: A neutral bookjacket in a science background  
    **Three Worst Labels**: cleaver, letter opener, envelope  
    **Explanation**: Predictions do not align with the prompt about a bookjacket in a science background.

13. **File Name**: images/ceramiccoffeemug__bathroom__001.png  
    **Prompt Summary**: A neutral ceramiccoffeemug in a bathroom background  
    **Three Worst Labels**: soap dispenser, washbasin, tub  
    **Explanation**: Predictions focus on bathroom items, lacking relevance to a coffee mug.

14. **File Name**: images/ceramiccoffeemug__garage__001.png  
    **Prompt Summary**: A neutral ceramiccoffeemug in a garage background  
    **Three Worst Labels**: hammer, screwdriver, pillow  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a coffee mug or garage.

15. **File Name**: images/ceramiccoffeemug__kitchen__001.png  
    **Prompt Summary**: A neutral ceramiccoffeemug in a kitchen background  
    **Three Worst Labels**: medicine chest, espresso maker, lotion  
    **Explanation**: Predictions mostly include kitchen items but lack a clear match to a neutral ceramic coffee mug.

16. **File Name**: images/ceramiccoffeemug__minimalist__001.png  
    **Prompt Summary**: A neutral ceramiccoffeemug in a minimalist background  
    **Three Worst Labels**: television, iPod, home theater  
    **Explanation**: Predictions are unrelated to the prompt about a coffee mug.

17. **File Name**: images/ceramiccoffeemug__modern__002.png  
    **Prompt Summary**: A neutral ceramiccoffeemug in a modern background  
    **Three Worst Labels**: loudspeaker, Polaroid camera, CD player  
    **Explanation**: Predictions do not align with the prompt about a coffee mug.

18. **File Name**: images/grannysmith__bathroom__002.png  
    **Prompt Summary**: A neutral grannysmith in a bathroom background  
    **Three Worst Labels**: washbasin, bathtub, tub  
    **Explanation**: Predictions focus on bathroom objects, not a Granny Smith apple.

19. **File Name**: images/grannysmith__classroom__001.png  
    **Prompt Summary**: A neutral grannysmith in a classroom background  
    **Three Worst Labels**: ping-pong ball, pool table, tennis ball  
    **Explanation**: Predictions are unrelated to a Granny Smith or classroom context.

20. **File Name**: images/grannysmith__classroom__002.png  
    **Prompt Summary**: A neutral grannysmith in a classroom background  
    **Three Worst Labels**: ping-pong ball, computer keyboard, croquet ball  
    **Explanation**: Predictions do not align with the prompt; no mention of a grannysmith or classroom.

21. **File Name**: images/grannysmith__garage__001.png  
    **Prompt Summary**: A neutral grannysmith in a garage background  
    **Three Worst Labels**: hammer, croquet ball, paintbrush  
    **Explanation**: Predictions do not align with the prompt; no mention of a grannysmith or garage.

22. **File Name**: images/grannysmith__green__002.png  
    **Prompt Summary**: A neutral grannysmith in a green background  
    **Three Worst Labels**: croquet ball, golf ball, baseball  
    **Explanation**: Predictions are unrelated to a Granny Smith apple or green background.

23. **File Name**: images/grannysmith__hotel__001.png  
    **Prompt Summary**: A neutral grannysmith in a hotel background  
    **Three Worst Labels**: hip, rubber eraser, pomegranate  
    **Explanation**: Predictions do not align with the prompt; no relevant items identified.

24. **File Name**: images/grannysmith__kitchen__002.png  
    **Prompt Summary**: A neutral grannysmith in a kitchen background  
    **Three Worst Labels**: pomegranate, croquet ball, maraca  
    **Explanation**: Predictions do not align with the prompt; no relevant kitchen or Granny Smith apple identified.

25. **File Name**: images/grannysmith__minimalist__002.png  
    **Prompt Summary**: A neutral grannysmith in a minimalist background  
    **Three Worst Labels**: desk, home theater, television  
    **Explanation**: Predictions do not relate to a neutral grannysmith or minimalist background.

26. **File Name**: images/grannysmith__modern__001.png  
    **Prompt Summary**: A neutral grannysmith in a modern background  
    **Three Worst Labels**: hook, table lamp, lampshade  
    **Explanation**: Predictions do not relate to a Granny Smith apple or modern background.

27. **File Name**: images/grannysmith__modern__002.png  
    **Prompt Summary**: A neutral grannysmith in a modern background  
    **Three Worst Labels**: ping-pong ball, puck, wall clock  
    **Explanation**: Predictions are unrelated to a Granny Smith apple or modern background.

28. **File Name**: images/grannysmith__science__002.png  
    **Prompt Summary**: A neutral grannysmith in a science background  
    **Three Worst Labels**: computer keyboard, scoreboard, ping-pong ball  
    **Explanation**: Predictions are unrelated to the prompt about a neutral grannysmith in a science background.

29. **File Name**: images/notebookwithkraftcover__garage__001.png  
    **Prompt Summary**: A neutral notebookwithkraftcover in a garage background  
    **Three Worst Labels**: hammer, carpenter's kit, pencil sharpener  
    **Explanation**: Predictions do not align with the prompt about a notebook in a garage.

30. **File Name**: images/notebookwithkraftcover__green__001.png  
    **Prompt Summary**: A neutral notebookwithkraftcover in a green background  
    **Three Worst Labels**: binder, lighter, book jacket  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a notebook.

31. **File Name**: images/notebookwithkraftcover__green__002.png  
    **Prompt Summary**: A neutral notebookwithkraftcover in a green background  
    **Three Worst Labels**: hatchet, hard disc, necklace  
    **Explanation**: Predictions do not relate to a notebook or kraft cover.

32. **File Name**: images/notebookwithkraftcover__hotel__002.png  
    **Prompt Summary**: A neutral notebookwithkraftcover in a hotel background  
    **Three Worst Labels**: loudspeaker, home theater, cleaver  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a notebook or hotel setting.

33. **File Name**: images/notebookwithkraftcover__kitchen__002.png  
    **Prompt Summary**: A neutral notebookwithkraftcover in a kitchen background  
    **Three Worst Labels**: television, screen, monitor  
    **Explanation**: Predictions are unrelated to the prompt about a notebook in a kitchen.

34. **File Name**: images/notebookwithkraftcover__modern__001.png  
    **Prompt Summary**: A neutral notebookwithkraftcover in a modern background  
    **Three Worst Labels**: binder, rule, cleaver  
    **Explanation**: Predictions do not align with the prompt about a notebook.

35. **File Name**: images/notebookwithkraftcover__modern__002.png  
    **Prompt Summary**: A neutral notebookwithkraftcover in a modern background  
    **Three Worst Labels**: hatchet, paintbrush, spatula  
    **Explanation**: Predictions do not align with the prompt about a notebook.

36. **File Name**: images/notebookwithkraftcover__plain__001.png  
    **Prompt Summary**: A neutral notebookwithkraftcover in a plain background  
    **Three Worst Labels**: binder, modem, envelope  
    **Explanation**: Predictions do not align with the prompt describing a notebook.

37. **File Name**: images/notebookwithkraftcover__science__002.png  
    **Prompt Summary**: A neutral notebookwithkraftcover in a science background  
    **Three Worst Labels**: binder, ballpoint, rule  
    **Explanation**: Predictions do not align with the prompt about a notebook in a science background.

38. **File Name**: images/opaquemetalwaterbottle__bathroom__001.png  
    **Prompt Summary**: A neutral opaquemetalwaterbottle in a bathroom background  
    **Three Worst Labels**: soap dispenser, washbasin, tub  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a water bottle.

39. **File Name**: images/opaquemetalwaterbottle__bathroom__002.png  
    **Prompt Summary**: A neutral opaquemetalwaterbottle in a bathroom background  
    **Three Worst Labels**: soap dispenser, combination lock, corkscrew  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a water bottle.

40. **File Name**: images/opaquemetalwaterbottle__garage__001.png  
    **Prompt Summary**: A neutral opaquemetalwaterbottle in a garage background  
    **Three Worst Labels**: carpenter's kit, screwdriver, pencil box  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a water bottle or garage.

41. **File Name**: images/opaquemetalwaterbottle__garage__002.png  
    **Prompt Summary**: A neutral opaquemetalwaterbottle in a garage background  
    **Three Worst Labels**: cocktail shaker, hourglass, saltshaker  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a water bottle.

42. **File Name**: images/opaquemetalwaterbottle__hotel__002.png  
    **Prompt Summary**: A neutral opaquemetalwaterbottle in a hotel background  
    **Three Worst Labels**: cocktail shaker, saltshaker, soap dispenser  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a neutral opaque metal water bottle.

43. **File Name**: images/opaquemetalwaterbottle__kitchen__002.png  
    **Prompt Summary**: A neutral opaquemetalwaterbottle in a kitchen background  
    **Three Worst Labels**: soap dispenser, coffeepot, perfume  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a metal water bottle.

44. **File Name**: images/opaquemetalwaterbottle__modern__002.png  
    **Prompt Summary**: A neutral opaquemetalwaterbottle in a modern background  
    **Three Worst Labels**: monitor, notebook, table lamp  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a water bottle.

45. **File Name**: images/opaquemetalwaterbottle__science__001.png  
    **Prompt Summary**: A neutral opaquemetalwaterbottle in a science background  
    **Three Worst Labels**: fountain pen, stethoscope, sewing machine  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a water bottle or science background.

46. **File Name**: images/softcouchpillow__classroom__001.png  
    **Prompt Summary**: A neutral softcouchpillow in a classroom background  
    **Three Worst Labels**: mouse, studio couch, bathtub  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a soft couch pillow in a classroom.

47. **File Name**: images/softcouchpillow__classroom__002.png  
    **Prompt Summary**: A neutral softcouchpillow in a classroom background  
    **Three Worst Labels**: paper towel, studio couch, home theater  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a neutral soft couch pillow in a classroom.

48. **File Name**: images/softcouchpillow__garage__001.png  
    **Prompt Summary**: A neutral softcouchpillow in a garage background  
    **Three Worst Labels**: pillow, paper towel, brassiere  
    **Explanation**: Predictions do not align with the prompt; only 'pillow' is relevant.

49. **File Name**: images/softcouchpillow__hotel__001.png  
    **Prompt Summary**: A neutral softcouchpillow in a hotel background  
    **Three Worst Labels**: dough, butternut squash, wooden spoon  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a soft couch pillow.

50. **File Name**: images/softcouchpillow__hotel__002.png  
    **Prompt Summary**: A neutral softcouchpillow in a hotel background  
    **Three Worst Labels**: pillow, carton, toilet tissue  
    **Explanation**: Predictions include 'pillow' but lack context of a hotel background.

51. **File Name**: images/softcouchpillow__kitchen__001.png  
    **Prompt Summary**: A neutral softcouchpillow in a kitchen background  
    **Three Worst Labels**: coffee mug, cup, mortar  
    **Explanation**: Predictions focus on kitchen items, not a soft couch pillow.

52. **File Name**: images/softcouchpillow__minimalist__001.png  
    **Prompt Summary**: A neutral softcouchpillow in a minimalist background  
    **Three Worst Labels**: mortar, toilet seat, cup  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a soft couch pillow.

53. **File Name**: images/softcouchpillow__minimalist__002.png  
    **Prompt Summary**: A neutral softcouchpillow in a minimalist background  
    **Three Worst Labels**: studio couch, toilet tissue, bathtub  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a soft couch pillow.

54. **File Name**: images/softcouchpillow__plain__001.png  
    **Prompt Summary**: A neutral softcouchpillow in a plain background  
    **Three Worst Labels**: mortar, lampshade, cup  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a soft couch pillow.

55. **File Name**: images/softcouchpillow__plain__002.png  
    **Prompt Summary**: A neutral softcouchpillow in a plain background  
    **Three Worst Labels**: home theater, laptop, iPod  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a soft couch pillow.

56. **File Name**: images/softcouchpillow__science__001.png  
    **Prompt Summary**: A neutral softcouchpillow in a science background  
    **Three Worst Labels**: tub, studio couch, carton  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a neutral soft couch pillow.

57. **File Name**: images/tablelampwithshadeoff__classroom__002.png  
    **Prompt Summary**: A neutral tablelampwithshadeoff in a classroom background  
    **Three Worst Labels**: marimba, crib, prison  
    **Explanation**: Predictions do not align with the prompt; none relate to a table lamp.

58. **File Name**: images/tablelampwithshadeoff__garage__001.png  
    **Prompt Summary**: A neutral tablelampwithshadeoff in a garage background  
    **Three Worst Labels**: syringe, screwdriver, lipstick  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a table lamp.

59. **File Name**: images/tablelampwithshadeoff__garage__002.png  
    **Prompt Summary**: A neutral tablelampwithshadeoff in a garage background  
    **Three Worst Labels**: lens cap, digital clock, loudspeaker  
    **Explanation**: Predictions do not align with the prompt; items are unrelated to a table lamp.

## 4 Target class logit analysis (Full Details)
### Class `pillow` (ImageNet #721)
- **Average logit**: 3.35 (std: 3.70)
- **Top‑5 activations**:
  - `dataset/images/softcouchpillow__modern__001.png` → logit=14.17
  - `dataset/images/softcouchpillow__green__002.png` → logit=13.05
  - `dataset/images/softcouchpillow__kitchen__002.png` → logit=12.28
  - `dataset/images/softcouchpillow__modern__002.png` → logit=11.82
  - `dataset/images/softcouchpillow__green__001.png` → logit=11.74

### Class `toilet seat` (ImageNet #861)
- **Average logit**: 4.16 (std: 2.71)
- **Top‑5 activations**:
  - `dataset/images/softcouchpillow__minimalist__001.png` → logit=12.37
  - `dataset/images/ceramiccoffeemug__bathroom__001.png` → logit=10.20
  - `dataset/images/ceramiccoffeemug__hotel__001.png` → logit=9.65
  - `dataset/images/softcouchpillow__classroom__001.png` → logit=9.57
  - `dataset/images/tablelampwithshadeoff__bathroom__002.png` → logit=8.97

### Class `park bench` (ImageNet #703)
- **Average logit**: 0.28 (std: 2.10)
- **Top‑5 activations**:
  - `dataset/images/tablelampwithshadeoff__classroom__002.png` → logit=9.02
  - `dataset/images/grannysmith__minimalist__002.png` → logit=5.27
  - `dataset/images/tablelampwithshadeoff__green__001.png` → logit=5.06
  - `dataset/images/ceramiccoffeemug__modern__002.png` → logit=4.34
  - `dataset/images/bookjacket__green__002.png` → logit=3.79

### Class `laptop` (ImageNet #620)
- **Average logit**: 5.29 (std: 2.96)
- **Top‑5 activations**:
  - `dataset/images/bookjacket__green__001.png` → logit=15.80
  - `dataset/images/notebookwithkraftcover__science__001.png` → logit=13.48
  - `dataset/images/bookjacket__green__002.png` → logit=13.10
  - `dataset/images/notebookwithkraftcover__minimalist__002.png` → logit=12.49
  - `dataset/images/bookjacket__classroom__002.png` → logit=11.38

### Class `fox squirrel` (ImageNet #335)
- **Average logit**: -3.04 (std: 1.80)
- **Top‑5 activations**:
  - `dataset/images/grannysmith__minimalist__002.png` → logit=1.41
  - `dataset/images/tablelampwithshadeoff__green__002.png` → logit=1.40
  - `dataset/images/grannysmith__green__002.png` → logit=1.39
  - `dataset/images/opaquemetalwaterbottle__green__002.png` → logit=0.63
  - `dataset/images/ceramiccoffeemug__modern__002.png` → logit=0.34

### Class `tennis ball` (ImageNet #852)
- **Average logit**: 3.44 (std: 3.08)
- **Top‑5 activations**:
  - `dataset/images/grannysmith__plain__002.png` → logit=17.15
  - `dataset/images/grannysmith__classroom__001.png` → logit=12.90
  - `dataset/images/grannysmith__plain__001.png` → logit=11.18
  - `dataset/images/grannysmith__minimalist__001.png` → logit=9.71
  - `dataset/images/grannysmith__hotel__001.png` → logit=9.10

## 5 Main biases of the model
1. **Contextual Bias**: The model often fails to associate objects with their correct contexts, leading to incoherent predictions. For example, it misidentifies a bookjacket in a classroom as unrelated items like a laptop or envelope.
2. **Object Confusion**: The model frequently confuses similar objects, such as mistaking a Granny Smith apple for a croquet ball or a pillow for a couch.
3. **Cultural Bias**: The model may reflect biases present in the training data, leading to skewed predictions based on cultural contexts that are not universally applicable.

## 6 Overall verdict
- **Strengths**:
  - Capable of identifying certain objects accurately in ideal contexts.
  - Demonstrates some level of understanding of object categories.
  
- **Weaknesses**:
  - High incoherence rate (48.76%) indicates significant misalignment with prompts.
  - Frequent contextual and object confusion leads to unreliable predictions.

- **Final Reliability Rating**: 2/5