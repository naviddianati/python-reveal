# python-reveal
Python API for creating reveal.js presentations.

This package provides a Python API for creating HTML-based presentations using Reveal.js
The semi-declarative syntax allows you to easily create sections, pages, paragraphs, lists, 
images, videos, Latex formulas, etc. and update properties such as alignment, color and size by chaining methods.

Here's what a minimal example looks like:

```python 
from pythonreveal import *

p = Presentation(
    theme=ThemeDark(),
    width=1200,
    height=1024,
    margin='0.05',
    transition='fade',
    data_dir='./files/example/'
    )

# Frontpage
################################################
page = p.frontpage()
page.title('Presentation Title')
author = page.author('Your Name')
author.institution('Your Institution')

# New Section 
################################################
p.sectionpage('Introduction')

# New Page 
################################################
page = p.page('First case')

# Paragraph
page.par('We have a very <b>dense</b> matrix. It is the "correct" matrix, but its density makes\
it hard to efficiently compute its network charachteristics such as its <b>community structure</b>.')

# Paragraph
page.par('Example:')

# ulist
l = page.ul()

# ulist items
l.item('Large dense similarity matrix.')
l.item('Dimensionality reduction.')
l.item('Correlation matrix in <b>genetic</b> or <b>protein</b> interaction networks?')

# Add vspace
page.vspace('2em')

# H2
page.h2('We need to approximate the graph').cl('h2yellow').fr()

# Save to file
################################################
p.export('minimal_example.html')
```

Examples:
![](/files/screenshots/reveal1.png)
![](/files/screenshots/reveal2.png)
![](/files/screenshots/reveal3.png)
 
For a complete example see `presentation_example.py`.
