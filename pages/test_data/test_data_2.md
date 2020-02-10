---
permalink: /test_data_2/
layout: doc
---

Test Data 2
===========

{% assign langs = site.data.translation.langs %}

**langs:** {{ langs }}

foo
---

{% for lang in langs %}
  {% assign l = lang.langcode %}
  **l:** {{ l }}
  {% assign ll = "lang_" | append: l %}
  **ll:** {{ ll }}
  {% assign d = site.data.l10n[ll].mydata %}
  **d:** {{ d }}
  {% assign d0 = d[0] %}
  {% assign d1 = d[1] %}
  **d0:** {{ d0 }}
  **d1:** {{ d1 }}
{% endfor %}

