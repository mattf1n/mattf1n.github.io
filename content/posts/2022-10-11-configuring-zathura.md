---
title: Configuring Zathura
date: 2022-10-11
---

# Configuring Zathura

I finally got Zathura (the pdf viewer) configured the way I want it on MacOS.
I installed using homebrew following these 
[instructions](https://github.com/zegervdv/homebrew-zathura).
I set up an automator script to launch Zathura for me according to this 
[gist](https://gist.github.com/agzam/76d761804330cc8c4600fccda952ed1c).
I chose my colors based on the blacks and whites in the [pencil](https://github.com/preservim/vim-colors-pencil) colorscheme.

Here's my zathurarc file:
```
set selection-clipboard clipboard
set guioptions ""
set window-title-basename true

set recolor true
set recolor-keephue true
set recolor-lightcolor \#F1F1F1
set recolor-darkcolor \#181818
set default-bg \#E5E6E6
set completion-bg \#181818
set completion-fg \#F1F1F1
set completion-group-bg \#181818
set completion-group-fg \#F1F1F1
set completion-highlight-fg \#181818
set inputbar-bg \#181818
set inputbar-fg \#F1F1F1
set statusbar-bg \#181818
set statusbar-fg \#F1F1F1
```

Good luck! :page_facing_up:
