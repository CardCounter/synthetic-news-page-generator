"""
can have up to 3 blocks each with up to 3 cols
"""

from jinja2 import Environment
import random_words

NONE = "<!-- NONE -->"

header_html_dict = {}

h_full = """
<header>
    {{ h_top }}
    {{ h_mid }}
    {{ h_bot }}
</header>
"""

##### TOP #####

h_top = """
<div class="h-top">
    {{ h_top_l }}
    {{ h_top_c }}
    {{ h_top_r }}
</div>
"""

h_top_l = """
<div class="h-top-l">
    <span class="h-top-text">{{ RAN_SEN_S }}</span>
</div>
"""

h_top_c = """
<div class="h-top-c">
    <span class="h-top-text">{{ RAN_WORD }}</span>
</div>
"""

h_top_r = """
<div class="h-top-r">
    <span class="h-top-text">{{ RAN_SEN_S }}</span>
</div>
"""

##### MID #####

h_mid = """
<div class="h-mid">
    {{ h_mid_l }}
    {{ h_mid_c }}
    {{ h_mid_r }}
</div>
"""

h_mid_l = """
<div class="h-mid-l">
    <span class="h-mid-text">{{ RAN_SEN_S }}</span>
</div>
"""

h_mid_c = """
<div class="h-mid-c">
    <span class="h-mid-text">{{ RAN_WORD }}</span>
</div>
"""

h_mid_r = """
<div class="h-mid-r">
    <span class="h-mid-text">{{ RAN_SEN_S }}</span>
</div>
"""

##### BOT #####

h_bot = """
<div class="h-bot">
    {{ h_bot_l }}
    {{ h_bot_c }}
    {{ h_bot_r }}
</div>
"""

h_bot_l = """
<div class="h-bot-l">
    <span class="h-bot-text">{{ RAN_SEN_S }}</span>
</div>
"""

h_bot_c = """
<div class="h-bot-c">
    <span class="h-bot-text">{{ RAN_WORD }}</span>
</div>
"""

h_bot_r = """
<div class="h-bot-r">
    <span class="h-bot-text">{{ RAN_SEN_S }}</span>
</div>
"""

# def construct_header():
#     env = Environment()

#     first_pass = env.from_string(start).render(
#     one=one,
#     two=two,
#     three=three
# )



