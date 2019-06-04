from django.shortcuts import render
from django.template import Template, Context
from django.template.loader import get_template, render_to_string
from django.http import HttpResponse


def main(request):
    # template = Template(
    #     'Hello {{ name }}!'
    # )
    template = get_template('main/index.html')
    # context = Context({
    #     'title': 'Main page',
    #     'subtitle': 'This is main page',
    # })
    context = {
        'title': 'Service main page',
        'subtitle': 'This is main page',
        'username': 'Anton',
        'is_anon': False,
        # 'is_anon': True,
    }
    response_string = template.render(context)

    return HttpResponse(response_string)


def contacts(request):
    context = {
        'contacts': [
            'Contact 1',
            'Contact 2',
            'Contact 3',
        ]
    }

    response_string = render_to_string(
        'main/contacts.html',
        context
    )
    
    return HttpResponse(response_string)


def about(request):
    context = {
        'username': 'antonantonantonantonantonantonanton',
        'text': '''
            Апогей однородно представляет собой вращательный астероид. Движение перечеркивает перигелий. Звезда иллюстрирует
            случайный математический горизонт - это солнечное затмение предсказал ионянам Фалес Милетский. Магнитное поле, оценивая
            блеск освещенного металического шарика, пространственно неоднородно. Межзвездная матеpия, после осторожного анализа,
            жизненно выслеживает параллакс, таким образом, атмосферы этих планет плавно переходят в жидкую мантию. Элонгация
            последовательно колеблет болид .
        '''
    }
    return render(request, 'main/about.html', context)
