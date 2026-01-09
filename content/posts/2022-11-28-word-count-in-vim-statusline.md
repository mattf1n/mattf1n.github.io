---
title: Putting word count in Vim statusline for LaTeX files
date: 2022-11-28
css:
  - ../style/main.css
---

This ftplugin updates the word count in the statusline on every save. 
More frequent updates slow Vim down and cause random rendering problems.

```
" .vim/after/ftplugin/tex.vim

function CountWords()
  silent return systemlist('texcount ' .. expand('%:p'))[2]
endfunction

let b:wordcount = CountWords()

augroup tex
  autocmd! * <buffer>
  autocmd BufWritePost <buffer> :let b:wordcount = CountWords()
augroup END

setlocal statusline=%{b:wordcount}
```

### Update (2023-03-27)

Using vim’s `job_start` function, I can asynchronously update the word count,
preventing the short hang on save.

```
" .vim/after/ftplugin/tex.vim

function UpdateWordcount(_, msg)
  if match(a:msg, 'Words in text:') >= 0
    let b:wordcount = a:msg
    let &l:statusline = &l:statusline " Refresh statusline
  endif
endfunction

augroup my_tex
  autocmd! * <buffer>
  autocmd BufEnter,BufWritePost <buffer> call job_start(
        \  [ 'texcount', expand('%:p') ], 
        \  {'out_cb': 'UpdateWordcount'}
        \) 
augroup END

let b:wordcount = 'Words in text: ...'
setlocal statusline=%{b:wordcount}
```
