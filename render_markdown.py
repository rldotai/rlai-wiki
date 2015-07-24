"""
Script for converting markdown to HTML.
"""
import mistune
from pygments import highlight
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter


class HighlightRenderer(mistune.Renderer):
    def block_code(self, code, lang):
        if not lang:
            return '\n<pre><code>%s</code></pre>\n' % mistune.escape(code)
        
        # Default to Python3 lexer
        if lang == "python":
            lang = "python3"

        lexer = get_lexer_by_name(lang, stripall=True, encoding="utf-8")
        formatter = HtmlFormatter()
        return highlight(code, lexer, formatter)

def render_markdown(txt):
    md = mistune.Markdown(renderer=HighlightRenderer())
    return md(txt)