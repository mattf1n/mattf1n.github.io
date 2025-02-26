# A side-scrolling website.

Here, I am developing a side-scrolling webpage,
documenting my choices and struggles as I go.

## A bit of history

Before the invention of the codex, we had scrolls.
A scroll is a long, continuous page, unlike a book which has many pages.
Typographers developed certain customs and traditions were to deal with the challenges presented by the medium.
In particular, two main types of scrolls exist: the *volumen* and *rotulus*. 
The *volumen*, like this website, consisted of a series of text blocks, kind of like pages.
The *rotulus*, like most modern webistes, consists of a continuous stream of text, and is not divided into page-like sections. 
When websites came along, suddenly we had a long, continuous medium again. 
So why did we decide to solve the layout problem with a *rotulus* design?
Perhaps, like *rotuli*, websites tend to be short in length. 
In that case, long-form articles online might consider the *volumen* design.

## Implementation

I start by putting everything in columns like so using the *columns* property.
I would like all text to be aligned between columns.
For this reason, I set the font size to always be 12 pt, line height to be fixed at 1.2, and top and bottom margins to be $1.2\times12=14.4$.
Bold fonts mess with page color, so I opt for all-caps and italics for h1 and h2, add slight letter spacing (5%) to the caps.

As the content of the page surpasses the window size, horizontal scrolling begins.
I notice that the far left page has no padding, so I add some to each paragraph.
The column gap needed some extra room anyways. 
This still does not solve the problem completely, since the body does not stretch to fit the content, meaning only the left margin seems to have any effect.
I'm not yet sure how to make it do that.

To let the content breathe, I set a *max-height* for the body and divide the remaining space between the top and bottom margins, giving twice as much space to the bottom.

## Some things I would like to have

This is a list of things I would like.

- Small caps
- Text figures
- A satisfying float design that works with columns.

I want to prevent the browser from synthesizing bad versions of font faces like weight, italics, and small caps so I turn off *font-synthesis*.

## Filler text

Lorem ipsum dolor sit amet, consectetur adipiscing elit. Aliquam pulvinar vel risus vel congue. In sagittis dolor vitae mi vehicula viverra. Cras facilisis nisl ipsum, in fringilla diam egestas vel. Aliquam cursus sed metus eu pharetra. In non ipsum vel eros malesuada molestie in non augue. Donec sit amet elementum risus. Fusce ipsum turpis, facilisis feugiat metus vitae, porta cursus est. Aliquam eu pretium enim.

Quisque pharetra tristique dolor, nec pharetra magna. Pellentesque ac vulputate mauris. Aliquam mattis magna ut nulla tincidunt fringilla. Maecenas diam lectus, eleifend eget nibh quis, volutpat auctor orci. Cras dapibus dui dolor, eget pellentesque sem congue non. Sed sit amet lobortis sem. Phasellus consequat lacus volutpat enim vestibulum, vitae volutpat metus aliquam. Maecenas tincidunt arcu neque, non bibendum massa interdum sed. Aliquam lobortis lectus aliquam bibendum aliquet. Aenean sed felis nisl. In venenatis eros non pellentesque gravida. Integer viverra fringilla risus ac pulvinar. Class aptent taciti sociosqu ad litora torquent per conubia nostra, per inceptos himenaeos.

Mauris blandit euismod arcu ut fermentum. Etiam tristique nisi in mi lacinia consequat. Duis efficitur, nunc tincidunt laoreet maximus, est magna tincidunt dui, placerat elementum est nunc sit amet risus. Curabitur sit amet lacus scelerisque, faucibus turpis at, pellentesque enim. Pellentesque facilisis felis quam, id dapibus sapien lobortis eget. Fusce fermentum diam arcu, ut posuere lectus ultricies et. Aenean aliquet aliquet odio eget porttitor. Curabitur ante mauris, euismod vel justo vel, finibus porttitor neque. Nunc vel ex pellentesque, venenatis sem nec, varius purus. Aenean bibendum vitae dolor cursus bibendum.

Mauris faucibus nisl et metus pellentesque, at posuere lectus semper. Morbi consectetur odio vitae turpis vehicula porttitor quis sit amet magna. Praesent nulla nunc, efficitur eget auctor at, scelerisque et lorem. Morbi ac nibh in libero malesuada laoreet eu et ex. Donec faucibus efficitur arcu id aliquet. Quisque mattis sit amet lorem nec ultricies. Maecenas auctor viverra urna. Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia curae; Sed commodo tincidunt viverra. Vestibulum sagittis risus enim, in consectetur quam sagittis imperdiet.

Sed viverra quis orci eu sagittis. Mauris enim metus, pulvinar nec felis et, volutpat lobortis diam. Pellentesque aliquet euismod ultrices. Vestibulum molestie volutpat neque id pulvinar. Sed ultrices a velit at semper. Duis pharetra pretium metus, sit amet vehicula purus finibus sed. Nullam at metus in metus vehicula hendrerit sit amet vel tortor. Nam odio nisi, auctor nec cursus vitae, ullamcorper sit amet urna. Suspendisse potenti. Etiam quis diam mauris. Pellentesque fringilla ligula non faucibus dignissim. Nunc eu malesuada ante. Sed diam orci, finibus ut rutrum a, dictum in lectus. In leo eros, venenatis eu augue non, mollis consectetur massa. Lorem ipsum dolor sit amet, consectetur adipiscing elit.


