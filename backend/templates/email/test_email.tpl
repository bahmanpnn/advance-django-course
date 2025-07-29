{% extends "mail_templated/base.tpl" %}

{% block subject %}
Hello {{ name }}
{% endblock %}

{% block html %}
<h2>this is a test email</h2>
<p>This is an <strong>html</strong> message.</p>
<img src="https://www.google.com/url?sa=i&url=https%3A%2F%2Fbitfieldconsulting.com%2Fposts%2Frandom-testing&psig=AOvVaw0LR-kVHXUc74qYaiWS5clT&ust=1753907399445000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCNifma704o4DFQAAAAAdAAAAABAL" alt="golang image">
<img src='https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.reddit.com%2Fr%2FPixelArt%2Fcomments%2F15z47dt%2Fi_got_bored_so_i_decided_to_draw_a_random_image%2F&psig=AOvVaw3JdiKBZjzPN-5QRL_iw5PH&ust=1753907642190000&source=images&cd=vfe&opi=89978449&ved=0CBUQjRxqFwoTCNiyhKL14o4DFQAAAAAdAAAAABAE' alt="pumpkin and cat">
{% endblock %}
