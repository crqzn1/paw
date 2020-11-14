from django.shortcuts import render

# Create your views here.

from django.template import loader  # 导入loader方法
from django.http import HttpResponse, HttpResponseRedirect
from django.template import Template,Context


def greet(request):
    t = loader.get_template('greet.html')
    html = t.render({'name': 'xyz'})  # 以字典形式传递数据并生成html
    return HttpResponse(html)  # 以 HttpResponse方式响应html


def firstpage(request):
    # 调用template()方法生成模板
    t1 = Template("""
        {% for item in list %}
            <li>{{ item }}</li>
        {% empty %}
            <h1>If not, come here to PAW</h1>
        {% endfor %}

        <h1> Testing ifeuqal tag </h1>
        {% for item in list %}
            {% ifequal item "C" %}
                <h2> this is C </h2>
            {% else %}
                <h2> {{ item }} is not C </h2>
            {% endifequal %}
        {% empty %}
             <h2> try C </h1>
        {% endfor %}

        {# This is a comment #}

        {% for i in list %}
            <tr class="{% cycle 'lang1' 'lang2' %}">
                <p>{{ i }} {{ i }}</p>
            </tr>
        {% endfor %}
        """)
    # 调用 Context()方法
    c1 = Context({'list': ['Python', 'Java', 'C', 'Javascript', 'C++']})
    html = t1.render(c1)
    return HttpResponse(html)
