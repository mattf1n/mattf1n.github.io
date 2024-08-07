---
title: Research Interest Demo
author: "[Matthew Finlayson](index.html)"
---

# Update: just join our discord!

I have created a discord server for people interested in collaborating with the lab. 
Email me for an invite!

# Original post

Hello! It is great to hear that you are interested in doing research :).
I love doing research and mentoring people when I have the time. 
Time and effort are precious limited resources both for mentors and mentees,
and I want to respect that for both of us. 
In order to gauge our fit I ask that you do a "demonstration of interest,"
i.e., a small demo project/writeup. 

An interest demo might consist of:

- A high-level project proposal that outlines the what, how, and why.
- A hypothesis, goal, mathematical idea that could help us better understand some aspect of language or language modeling
- The results for an initial experiment, with an interpretation and ideas for next steps.

The point of the demo is to show me that you are able to carry out a mostly-independent research project,
so I will look for evidence that you have the time, commitment, and required skills 
to think about interesting problems and hypotheses and engineer experiments to test them.
Of course you may have not done research before, 
so feel free to reach out to me with incomplete demos to get feedback on what might be interesting or worthwhile.
Once you have a complete demo, I would be happy to meet to discuss how to move forward. 
I will do my best to provide guidance as best I can.

# Research ideas

Some interesting questions, directions, and project kernels. I will add and revise this list periodically.
You do not need to choose a topic from this list, but hopefully this can help give you some ideas.
You can also look for inspiration among my [posts](index.html#posts).

## Pretraining data detection

There are existing methods for identifying which data a language model has been trained on. 
Is it possible to provide guarantees on the accuracy of such methods?
Can we come up with new, more effective methods?
Can the softmax bottleneck provide any leverage for this?

## Evaluating decoding in language models

How can we reliably tell which sampling method is better (e.g., top-k, top-p) for a language model on a task?
Is there a mathematically justified way to accurately compare these methods in a fair way?
One ideas I have thrown around is an adversarial setting where each decoding method must sample from the set difference of the two methods.
However, I'm not sure if this is a fair comparison.

## Error allocation for language models

When a language model suffers from a "softmax bottleneck", how do they allocate errors?
Is there a way to mathematically characterize which tokens will have larger errors than others?
My paper "Closing the Curious Case of Neural Text Degeneration" deals with some of these questions,
but some of the mathematical ideas could be further developed. 

For instance, during the project I thought I might be able to show that SM bottleneck causes log-prob underestimation errors that are not arbitrarily close to 0, but I never got to figuring out if it could be done.
I also hypothesize that models will have much larger absolute probability errors on high-probability tokens,
but larger absolute log-probability errors on low-probability tokens, but I have not worked out any formal mathematical justification.
Lastly, I wonder if models are more likely to underestimate high-probability tokens and overestimate low-probability tokens.

## Language model embeddings

How do language models choose their embeddings?
Some preliminary experiments suggest that embeddings tend to reside near the surface of a small-radius hypersphere.
How could this geometric phenomenon be used to our advantage?

Can the particular choice of embeddings and their linear dependencies be used to identify text generated by a language model with guaranteed accuracy?
