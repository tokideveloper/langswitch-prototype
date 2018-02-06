---
title: Doc Root
layout: doc
permalink: /doc/
redirect_from:
- /doc/
- /en-US/doc/
langprefix:
---

Doc root
========

This is a test page.
With that, I can test the root directory of Doc.

And [here][aaa] is a relative link to a page.

And [here][bbb] is an absolute link to a page.
And [here][bbb2] is another absolute link to a page.

And [here][ccc] is a relative link to another page.

And [here][ddd] is an absolute link to another page.
And [here][ddd2] is another absolute link to another page.

And [here][eee] is a relative link to the root directory.

And [here][fff] is an absolute link to the root directory.
And [here][fff2] is another absolute link to the root directory.

Bye!

[aaa]: testpage1/
[bbb]: /doc/testpage1/
[bbb2]: {{ page.langprefix }}/doc/testpage1/
[ccc]: testpage2/
[ddd]: /doc/testpage2/
[ddd2]: {{ page.langprefix }}/doc/testpage2/
[eee]: ../
[fff]: /
[fff2]: {{ page.langprefix }}/
