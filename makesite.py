import chevron 
import pypandoc as pandoc
from glob import glob
import os.path as path

for infile in glob('content/*.md'):
    p, f = path.split(infile)
    f, e = path.splitext(f)
    fmt = 'markdown+tex_math_dollars+emoji'
    xa = ['--mathjax']
    content = pandoc.convert_file(infile, 'html', format=fmt, extra_args=xa)
    with open('skeleton/template.html') as template:
        with open(f + '.html', 'w') as out:
            out.write(chevron.render(template, {'content':content}))


