"""
Code for converting markdown to HTML.

Cobbled together from various sources, since the Mistune documentation is far
from helpful.
"""
import re

import mistune

from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter
from pygments.util import ClassNotFound


class MathBlockGrammar(mistune.BlockGrammar):
    block_math = re.compile(r"^\$\$(.*?)\$\$", re.DOTALL)
    latex_environment = re.compile(r"^\\begin\{([a-z]*\*?)\}(.*?)\\end\{\1\}",
                                                re.DOTALL)

class MathBlockLexer(mistune.BlockLexer):
    default_rules = ['block_math', 'latex_environment'] + mistune.BlockLexer.default_rules

    def __init__(self, rules=None, **kwargs):
        if rules is None:
            rules = MathBlockGrammar()
        super(MathBlockLexer, self).__init__(rules, **kwargs)

    def parse_block_math(self, m):
        """Parse a $$math$$ block"""
        self.tokens.append({
            'type': 'block_math',
            'text': m.group(1)
        })

    def parse_latex_environment(self, m):
        self.tokens.append({
            'type': 'latex_environment',
            'name': m.group(1),
            'text': m.group(2)
        })


class MathInlineGrammar(mistune.InlineGrammar):
    # Regular expressions work strangely with mistune, but the IPython people 
    # have something mostly functional here.
    math = re.compile(r"^\$(.+?)\$", re.DOTALL)
    block_math = re.compile(r"^\$\$(.+?)\$\$", re.DOTALL)
    text = re.compile(r'^[\s\S]+?(?=[\\<!\[_*`~$]|https?://| {2,}\n|$)')


class MathInlineLexer(mistune.InlineLexer):
    default_rules = ['block_math', 'math'] + mistune.InlineLexer.default_rules

    def __init__(self, renderer, rules=None, **kwargs):
        if rules is None:
            rules = MathInlineGrammar()
        super(MathInlineLexer, self).__init__(renderer, rules, **kwargs)

    def output_math(self, m):
        return self.renderer.inline_math(m.group(1))

    def output_block_math(self, m):
        return self.renderer.block_math(m.group(1))


class MarkdownWithMath(mistune.Markdown):
    def __init__(self, renderer, **kwargs):
        if 'inline' not in kwargs:
            kwargs['inline'] = MathInlineLexer
        if 'block' not in kwargs:
            kwargs['block'] = MathBlockLexer
        super(MarkdownWithMath, self).__init__(renderer, **kwargs)

    def output_block_math(self):
        return self.renderer.block_math(self.token['text'])

    def output_latex_environment(self):
        return self.renderer.latex_environment(self.token['name'], self.token['text'])


class CustomRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        """Rendering code blocks."""
        if lang:
            if lang == 'python':
                lang = 'python3'  # default to python3 syntax
            try:
                lexer = get_lexer_by_name(lang, stripall=True)
            except ClassNotFound:
                code = lang + '\n' + code
                lang = None

        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % \
                mistune.escape(code)

        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)

    def header(self, text, level, raw=None):
        html = super(CustomRenderer, self).header(text, level, raw=raw)
        return html

    # Pass math through unaltered - mathjax does the rendering in the browser
    def block_math(self, text):
        return '$$%s$$' % text

    def latex_environment(self, name, text):
        return r'\begin{%s}%s\end{%s}' % (name, text, name)

    def inline_math(self, text):
        return '$%s$' % text


def render_markdown(source):
    """Convert a markdown string to HTML using mistune"""
    return MarkdownWithMath(renderer=CustomRenderer(escape=False)).render(source)