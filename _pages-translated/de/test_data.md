---
permalink: /de-DE/test_translated_data/
layout: doc
---

Test Translated Data (de version)
=================================

{% assign files = site.data-translated %}

{% assign de_files = files | where: 'lang', 'de-DE' %}

{% assign de_test_files = de_files | where: 'type', 'test' %}

{% for de_test_file in de_test_files %}
  {% assign data = de_test_file.data %}
  **data:** {{ data }}

  **data[0].test:** {{ data[0].test }}
{% endfor %}

