---
title: Bug in my torch code, random links.
date: 2024-12-17
css:
  - ../style/main.css
---

Torch code bug that took me an hour to fix: I wrapped a function in `@torch.inference_mode` which called another function which called another function that was trying to call `torch.backward`.

### Cleaning out my Notes app

Booking this site [fonts for mathematics](https://luc.devroye.org/math.html) for later use.

Intrigued by the idea of building my own Bluesky feed using [Graze](https://bsky.app/profile/graze.social).
Maybe some day I will have time to.

My colleague from USC pointed me to their [incomplete paper](https://openreview.net/forum?id=eRkNNQRppH) about training dynamics that they submitted to ICLR. I mean to give it a skim sometime.
