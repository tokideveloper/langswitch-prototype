---
title: Test Page (pt-BR)
layout: doc
permalink: /pt-BR/doc/testpage1/
redirect_from:
- 
- /pt-BR/doc/testpage1/
langprefix: /pt-BR
---

Test page in pt-BR
==================

This is a test page.
With that, I can test.

And [here][aaa] is a relative link to another page.

And [here][bbb] is an absolute link to another page.
And [here][bbb2] is another absolute link to another page.

And [here][ccc] is a relative link to the root directory of Doc.

And [here][ddd] is an absolute link to the root directory of Doc.
And [here][ddd2] is another absolute link to the root directory of Doc.

And [here][eee] is a relative link to the root directory.

And [here][fff] is an absolute link to the root directory.
And [here][fff2] is another absolute link to the root directory.

Bye!

[aaa]: ../testpage2/
[bbb]: /pt-BR/doc/testpage2/
[bbb2]: {{ page.langprefix }}/doc/testpage2/
[ccc]: ../
[ddd]: /pt-BR/doc/
[ddd2]: {{ page.langprefix }}/doc/
[eee]: ../../
[fff]: /pt-BR/
[fff2]: {{ page.langprefix }}/
