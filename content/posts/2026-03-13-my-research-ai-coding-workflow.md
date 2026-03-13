---
title: My research AI coding workflow
date: 2026-03-13
css:
  - ../style/main.css
html-math-method: mathml
---

My eyes generally glaze over reading "how I use AI" posts, but enough of my colleagues have expressed interest that I think this would be worth sharing.
My overall strategy for coding these days is to have OpenAI's Codex agent write and run my code for me on the cluster.

Main considerations: 
- I don't use python notebooks.
- I don't have root/sudo access on the research cluster.

My current workflow for running experiments on the USC cluster:

- Install node+npm (I recommend using nvm, since I saw a colleague succeed with this recently). 
  You will have to figure out how to do this without root access. It's possible.
- Create your project directory (or `cd` into it if it already exists).
- Load tmux (`module load tmux`) and start a session with `tmux` so that you have a persistent session that you can reattach to if you get disconnected (`tmux attach`).
- Install OpenAI's Codex with npm: `npm install -g @openai/codex`. Then run `codex` to start your coding agent session. You can resume with `codex resume` if you get disconnected.
- Tell Codex to use `uv` to work with python. Tell it to run experiments using SLURM. It knows how to do these things.
- Start telling codex what to do. It's really good at things.
