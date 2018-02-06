---
title: Another Test Page
layout: doc
permalink: /doc/testpage2/
redirect_from:
- /doc/testpage2/
- /en-US/doc/testpage2/
langprefix:
---

Another test page
=================

This is another test page.
With that, I can test, too.

And [here][aaa] is a relative link to a page.

And [here][bbb] is an absolute link to a page.
And [here][bbb2] is another absolute link to a page.

And [here][ccc] is a relative link to the root directory of Doc.

And [here][ddd] is an absolute link to the root directory of Doc.
And [here][ddd2] is another absolute link to the root directory of Doc.

And [here][eee] is a relative link to the root directory.

And [here][fff] is an absolute link to the root directory.
And [here][fff2] is another absolute link to the root directory.

Have fun!

[aaa]: ../testpage1/
[bbb]: /doc/testpage1/
[bbb2]: {{ page.langprefix }}/doc/testpage1/
[ccc]: ../
[ddd]: /doc/
[ddd2]: {{ page.langprefix }}/doc/
[eee]: ../../
[fff]: /
[fff2]: {{ page.langprefix }}/
