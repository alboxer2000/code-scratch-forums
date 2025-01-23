import requests
import re
import traceback
import urllib.parse
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

def bbcode_to_html(bbcode_text):
    """Converts BBCode text to HTML, correctly handling all cases."""
    try:
        def handle_quote_with_username(match):
            username = match.group(1)
            content = match.group(2)
            return f"""<div class="quote">
                        <b>{username} wrote:</b><br>
                        {content}
                    </div>"""

        def handle_quote_without_username(match):
            content = match.group(1)
            return f"""<div class="quote">
                        {content}
                    </div>"""

        def handle_link(match, url_base, link_text_group=1, display_text_group=None): #display_text_group defaults to None
            link_text = urllib.parse.quote_plus(match.group(link_text_group)) # Use quote_plus
            display_text = match.group(display_text_group) if display_text_group is not None and len(match.groups()) >= display_text_group else match.group(link_text_group)
            return f"<a href='{url_base}{link_text}' target='_blank' rel='noopener noreferrer'>{display_text}</a>"

        def handle_img(match):
            url = match.group(1) if match.group(1) else match.group(2)
            return f"<img src='{url}' alt='Image'>"

        def handle_code(match):
            content = match.group(1)
            return f"<pre class='code'>{content}</pre>"

        def handle_scratchblocks(match):
            return f"<pre class='blocks'>{match.group(1)}</pre>"

        replacements = [
            (r"\[code\](.*?)\[/code\]", handle_code),
            (r"\[code(?:=.*?)?\](.*?)\[/code\]", handle_code),
            (r"\[scratchblocks\](.*?)\[/scratchblocks\]", handle_scratchblocks),
            (r"\[b\](.*?)\[/b\]", r"<b>\1</b>"),
            (r"\[i\](.*?)\[/i\]", r"<em>\1</em>"),
            (r"\[u\](.*?)\[/u\]", r"<u>\1</u>"),
            (r"\[s\](.*?)\[/s\]", r"<s>\1</s>"),
            (r"\[big\](.*?)\[/big\]", r"<span style='font-size: 1.2em;'>\1</span>"),
            (r"\[color=(.*?)\](.*?)\[/color\]", r"<span style='color: \1;'>\2</span>"),
            (r"\[url\](.*?)\[/url\]", r"<a href='\1' target='_blank' rel='noopener noreferrer'>\1</a>"),
            (r"\[url=(.*?)\](.*?)\[/url\]", r"<a href='\1' target='_blank' rel='noopener noreferrer'>\2</a>"),
            (r"\[quote=(.*?)\](.*?)\[/quote\]", handle_quote_with_username),
            (r"\[quote\](.*?)\[/quote\]", handle_quote_without_username),
            (r"\[small\](.*?)\[/small\]", r"<span style='font-size: 0.8em;'>\1</span>"),
            (r"\[center\](.*?)\[/center\]", r"<center>\1</center>"),
            (r"\[p\](.*?)\[/p\]", r"<p>\1</p>"),
            (r"\[img\](.*?)\[/img\]", handle_img),
            (r"\[img=(.*?)\]", handle_img),
            (r"\[wiki(?:=|\s+)(.*?)\](.*?)\[/wiki\]", lambda m: handle_link(m, "https://en.scratch-wiki.info/wiki/Special:Search?search=", 1, 2 if m.group(2) else None)),
            (r"\[wiki\](.*?)\[/wiki\]", lambda m: handle_link(m, "https://en.scratch-wiki.info/wiki/Special:Search?search=", 1)),
            (r"\[wp(?:=|\s+)(.*?)\](.*?)\[/wp\]", lambda m: handle_link(m, "https://en.wikipedia.org/wiki/Special:Search?search=", 1, 2 if m.group(2) else None)),
            (r"\[wp\](.*?)\[/wp\]", lambda m: handle_link(m, "https://en.wikipedia.org/wiki/Special:Search?search=", 1)),
            (r"\[google(?:=|\s+)(.*?)\](.*?)\[/google\]", lambda m: handle_link(m, "https://www.google.com/search?hl=en&q=", 1, 2 if m.group(2) else None)),
            (r"\[google\](.*?)\[/google\]", lambda m: handle_link(m, "https://www.google.com/search?hl=en&q=", 1)),
            (r"\[(?:dict|dictionary)(?:=|\s+)(.*?)\](.*?)\[/(?:dict|dictionary)\]", lambda m: handle_link(m, "https://dictionary.com/browse/", 1, 2 if m.group(2) else None)),
            (r"\[(?:dict|dictionary)\](.*?)\[/(?:dict|dictionary)\]", lambda m: handle_link(m, "https://dictionary.com/browse/", 1)),
        ]

        html_text = bbcode_text

        # 1. Replace newlines with <br /> globally FIRST
        html_text = html_text.replace('\n', '<br />')

        for pattern, replacement in replacements:
            html_text = re.sub(pattern, replacement, html_text, flags=re.IGNORECASE | re.DOTALL)

        return html_text

    except Exception as e:
        print(f"An error occurred during parsing: {e}")
        traceback.print_exc()
        return None

def fetch_and_parse_bbcode(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise HTTPError for bad responses (4xx or 5xx)
        bbcode_text = response.content.decode('utf-8')
        html_content = bbcode_to_html(bbcode_text)

        if html_content is None:
            return None

        full_html = f"""<!DOCTYPE html>
<html>
<head>
    <meta charset="UTF-8">
    <title>BBCode Parser</title>
    <style>
        body {{
            font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
            line-height: 1.2;
            margin: 20px;
        }}
        pre.code {{
            background-color: #f0f0f0;
            padding: 10px 20px;
            border: 1px solid #ccc;
            font-family: monospace;
            overflox-x: scroll;
            line-height: 1;
        }}
        .quote {{
            background-color: #f0f0f0;
            padding: 10px 20px;
            border: 1px solid #ccc;
        }}
    </style>
    <script src="https://cdn.scratch.mit.edu/scratchr2/static/__774e7841eab6f875e16f7cec38b2f7c3__//djangobb_forum/scratchblocks/scratchblocks.min.js" defer></script>
    <script>
        document.addEventListener('DOMContentLoaded', (event) => {{
            scratchblocks.renderMatching('pre.blocks', {{
                style: 'scratch3',
                languages: ['en'],
                scale: 1,
            }});
        }});
    </script>
</head>
<body>
{html_content}
</body>
</html>"""
        return full_html
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
        return None
    except Exception as e:
        print(f"An error occurred during parsing: {e}")
        return None

# Example usage (now more general)
post_id = 3466932
post_id_input = input("Post ID (defaults to TOLORS): ")
if not post_id_input == "":
  post_id = post_id_input
print(post_id)
bbcode_url = f'https://scratch.mit.edu/discuss/post/{post_id}/source/'  # Example URL
output_filename = "parsed_bbcode.html"

html_content = fetch_and_parse_bbcode(bbcode_url)

if html_content:
    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(html_content)
    print(f"{output_filename} written")
else:
    print("Failed to parse BBCode.")
