---
permalink: /test_data/
layout: doc
---

Test Data
=========

{% assign langs = site.data.translation.langs %}

**langs:** {{ langs }}

foo
---

{% for lang in langs %}
  {% assign l = lang.langcode %}
  **l:** {{ l }}
  {% assign d = site.data.l10n[l] %}
  **d:** {{ d }}
  {% assign dd = d[0] %}
  **Warning-Message:** {{ dd.warningmsg }}
  **Number:** {{ dd.number }}
{% endfor %}

