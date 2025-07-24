## Project Overview: *Static Images Network Analyzer*

This is the final project for the Cognitive Learning course, titled *Static Images Network Analyzer*.  
The goal is to analyze **cognitive biases** in image classification models, focusing on **spurious correlations**—for example, when the model is influenced more by background context than by the actual object in the image.

The project has two main phases:
1. **Controlled dataset generation**: we created artificial images combining neutral objects with potentially bias-inducing visual contexts, using *Stable Diffusion v1.5*.  
   > The image generation code is located in the file: `generate_dataset_diff_v1_5.py.py`.
2. **Model analysis**: we evaluated how three pretrained classifiers (AlexNet, ResNet-18, ViT-18) responded to these images and measured whether their predictions aligned with the original prompt or were misled by context.  
   > All analysis and evaluation steps are implemented in this notebook.

We extract the **top-10 logits** for each image-model pair, and send both the original prompt and the predictions to a **language model (LLM)** for semantic auditing. The LLM provides a coherence score (0–1), a short explanation, and optional confidence. These evaluations are stored in a `.jsonl` file.

Finally, we build an aggregated **bias report** using precomputed statistics and LLM-generated justifications. This final Markdown report includes:
- Aggregate performance metrics
- Recurring error patterns
- Detailed list of incoherent predictions
- Class-specific logit behavior
- Overall model verdict

This workflow allows us to systematically study the effect of **spurious visual cues** and assess the **robustness and reliability** of vision models through a cognitively informed pipeline.