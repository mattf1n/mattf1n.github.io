---
title: Papers that caught my attention at NeurIPS 2025
author: '[Matthew Finlayson](index.html)'
---

[Broken Tokens? Your Language Model can Secretly Handle Non-Canonical Tokenizations](https://arxiv.org/abs/2506.19004)
shows that language models are fine with however you tokenize your doc.
Can we hide information in the tokenization scheme (Alisa's idea at poster) that might allow jailbreaking at test time/fingerprinting?
How do LMs learn not to attend to "New" in "New York"? (York token encodes all info).
Does the model "know" when it is getting non-canonical tokenizations?
What does the model do with the extra compute from inefficient tokenizations?

[Sample, Don't Search: Rethinking Test-Time Alignment for Language Models](https://arxiv.org/abs/2504.03790)
gives an algorithm that, in the limit, samples from an RL-tuned model without actually doing the RL.
All it needs is a reward model and base language model.
Works best with continuous rewards and when the RL training would narrow the distribution from the base model. From one of Andre Martin's former students now doing a PhD with Noah Smith.

[We Should Chart an Atlas of All the World's Models](https://horwitz.ai/model-atlas)
gives a pretty visualization of model family trees.
May be useful for model forensics work.

[Projecting Assumptions: The Duality Between Sparse Autoencoders and Concept Geometry](https://arxiv.org/abs/2503.01822)
expounds on how the nonlinearity in an SAE (top-K, threshold, etc.) makes an implicit assumption about how models represent concepts (linear separability, angular separability, etc.).
They suggest a new one.
I think the takeaway should have been that SAEs need to use multiple nonlinearities to capture different methods for storing info in LLMs.

[Born a Transformer -- Always a Transformer? On the Effect of Pretraining on Architectural Abilities](https://arxiv.org/abs/2505.21785)
is Michael Hahn's student's work on theoretical expressivity of transformers impact in practice.
