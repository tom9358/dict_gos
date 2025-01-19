This repository contains the files for my goal to make an extension for LibreOffice using Hunspell for Gronings Low Saxon (ISO 639-3: gos). I am still figuring out how to do that.

Note that I do this in my free time, and I have other projects, interests and obligations as well, so progress might be slow and the project could die. So don't hesitate to contact me, and contributions and suggestions are very welcome!

So far I've figured out:
Barebones hunspell only needs a dictionary file to work (the affix file can be empty).
Relevant link:
- https://web.archive.org/web/20130810100226/http://www.suares.com/index.php?page_id=25&news_id=233

I have some idea of what .aff files can do, but haven't looked into it in depth. I tried to add some rules but haven't tested them.
Relevant link:
- https://manpages.ubuntu.com/manpages/focal/man5/hunspell.5.html

LibreOffice requires .oxt files, which are apparently just .zip files. I've managed to make one! I should investigate how to add it to LibreOffice's extension store and to some other places (I saw some Debian and Fedora things, Firefox, maybe Google Chrome?) since no clue how to do that, but apart from that I might pause the project here for now. Although I do intend to improve at least the wordlist in the future.
