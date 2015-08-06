import sys
from render_markdown import render_markdown

# line = \
# """
# Let $G_{t}^{n}$ (sometimes written as $G_{t}^{(k)}$) denote the n-step return 
# following time step $t$. 
# """

# print(render_markdown(line))


if __name__ == "__main__":
    for path in sys.argv[1:]:
        print(path)
        print(render_markdown(open(path, 'r').read()))
        
