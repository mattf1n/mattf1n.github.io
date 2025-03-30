# My research stack

- Editor: vim

## Compute environment

I leave a laptop at the office and use another at home, using git to sync between.
I usually start by coding and running experiments on my local machine.
Once my experiments reach a certains scale (require more than a few mins of time) 
I start working on a server with a SLURM cluster.
Since I use mostly-default vim, editing code on the server is mostly the same.
Were I to want more functionality, I might use sshfs to mount the server directory locally.


- Pyenv manages python versions
- Python's own venv module for virtual environments
- Makefiles track experiment commands and prevent re-running sub-parts
- Pytest for writing tests
- Jaxtyping for tensor shape annotations. I haven't actually gotten to the point of running a checker, it's just nice to have the annotations there.

Most of my research code just uses numpy, sometimes I have to use torch, sometimes I get to use jax. A lot of my research is made easier with cvxpy for convex optimization.

## CUDA versions: an ongoing struggle

On the USC NLP compute cluster, different nodes have different CUDA versions installed.
I'm trying to figure out how to get a consistent compute environment.
For now I'm just specifying the node that I want to run on.
I believe that some of my peers use Docker.


