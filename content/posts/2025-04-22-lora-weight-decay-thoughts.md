---
title: LoRA weight decay thoughts
date: 2025-04-22
css:
  - ../style/main.css
---

[Irhum makes an observation](https://irhum.github.io/blog/lorawd/) that I have thought about from time to time: LoRA-adapted model weights decay to the original model during training (not 0).
How much of LoRA's success could be attributed to this fact. 
Could there by other PEFT methods that do just as well with a similar decay schedule?
Might this inductive bias be generally helpful for even non-PEFT methods?
