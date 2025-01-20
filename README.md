[![Leesmij Nederlands](https://img.shields.io/badge/Leesmij-Nederlands-blue)](LEESMIJ.md)
### The LibreOffice extension has been accepted by the extension store admins and is now available here! https://extensions.libreoffice.org/en/extensions/show/99299


This repository contains the files for a LibreOffice extension for spell checking Gronings Low Saxon (ISO 639-3: gos). It uses a dictionary (so a long word list) and a file with some spelling patterns. This approach is based on the spelling program Hunspell. In hindsight it was quite easy for me to create this extension, and by far the hardest and most time consuming task is to create a high quality word list. My current word list is usable, but it can be improved.

I do this in my free time, and I have other projects, interests and obligations as well, so progress might be slow and the project could die. So don't hesitate to contact me, and contributions and suggestions are very welcome! If you want help for another language, or have thoughts about Gronings / Low Saxon you'd like to share, feel free to reach out!

---
Some minor technical details:

Barebones hunspell only needs a dictionary file to work (the affix file can be empty).
Relevant link:
- https://web.archive.org/web/20130810100226/http://www.suares.com/index.php?page_id=25&news_id=233

I have some idea of what .aff files can do, but haven't looked into it in depth. I tried to add some rules but haven't tested them.
Relevant link:
- https://manpages.ubuntu.com/manpages/focal/man5/hunspell.5.html

LibreOffice requires .oxt files, which are apparently just .zip files. I've managed to make one! It needs a few extra files. Feel free to unpack my .oxt file and copy its structure (and its generic contents), also feel free to ask me for help.
In the future I'd like to investigate how to add the tool to more places other than LibreOffice's extension store (I saw some Debian and Fedora things, Firefox, maybe Google Chrome?) since no clue yet how to do that.
