---
permalink: /test_translated_data/
layout: doc
---

Test Translated Data (original version)
=======================================

{% assign files = site.data-translated %}

{% assign en_files = files | where: 'lang', 'en-US' %}

{% assign en_test_files = en_files | where: 'type', 'test' %}

{% for en_test_file in en_test_files %}
  {% assign data = en_test_file.data %}
  **data:** {{ data }}

  **data[0].test:** {{ data[0].test }}
{% endfor %}

