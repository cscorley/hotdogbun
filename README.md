hotdogbun.py
============

Let's split some conference papers in half so we can read them on
smaller devices in continuous scroll mode instead of fumbling around on
the screen like idiots.

All this script does is split each page of a PDF down the middle,
hotdog bun style.

Usage
-----

To split a file './paper.pdf': `python2 hotdogbun.py ./paper.pdf`

That's it. Your split pdf will be located at './paper-split.pdf'

Requirements
------------

Right now, this script uses the [PyPDF2](https://github.com/knowah/PyPDF2/)
library to split things, which requires manual installation. I'd really like
to change that to something that can be installed from `pip`. Let me know.

For now, you can install the current PyPDF2 by running `make pypdf2`.

....Hotdog bun?
---------------
`python2 `<a href="http://en.wikipedia.org/wiki/File:Hotdog_-_Evan_Swigart.jpg"><img src="http://upload.wikimedia.org/wikipedia/commons/thumb/f/fb/Hotdog_-_Evan_Swigart.jpg/150px-Hotdog_-_Evan_Swigart.jpg"></a>`.py` <img src="https://raw.github.com/cscorley/hotdogbun/master/orig.png" height=300px>
***=======>***
<img src="https://raw.github.com/cscorley/hotdogbun/master/split.png" height=300px>


... basically.
