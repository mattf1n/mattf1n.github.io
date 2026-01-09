---
title: Some papers that caught my attention at NeurIPS 2025
date: 2025-12-08
author: "[Matthew Finlayson](/index.html)"
css:
  - ../style/blog.css
lang: en
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
