{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ name }}
{% endblock %}

{% block html %}
<h2>Activation account email</h2>
<a href="http://127.0.0.1:8000/accounts/api/v1/activation/confirm/{{user_token}}">active account</a>
<hr>
<br>
{{user_token}}
{% endblock %}
