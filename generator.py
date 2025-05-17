"""
news sites are made up of up to four blocks:
header
body
bottom block
footer

header:
almost always has a header. comes in different sizes, up to 3 sections

body:
ive seen one to three cols, sometimes date is in an off-column, sometimes its in the middle. 
side cols are ususally for ads, extra news, etc

bottom block:
this is where things like relaited news or donations go. some have them some dont, so will flip a coin to generate this

footer:
same as header, some are thick, some are thin

basic idea:
use jinja templates to generate synthetic news websties by randomly choosing and inserting html template for the four
charateristics above. will use random css too. 

do this when youre done, before commit:
pip freeze > requirements.txt
pip install -r requirements.txt
"""

import jinja2
import webview

HEADER_HTML_PATH = 0
HEADER_STYLES_PATH = 0

BODY_HTML_PATH = 0
BODY_STYLES_PATH = 0

BLOCK_HTML_PATH = 0
BLOCK_STYLES_PATH = 0

FOOTER_HTML_PATH = 0
FOOTER_STYLES_PATH = 0






