from django import template

register = template.Library()

black_list = ['блин','дзюдо', 'нафиг', 'щука', 'лопата']


@register.filter()
def censor(value):
    te = str(value)
    text=te.lower()
    text_split = text.split()
    cen = {"дзюдо": "д****"}
    for key, value in cen.items():
        for i in range(len(text_split)):
            if text_split[i] == key:
                text_split[i] = value


    return f'{" ".join(map(str,text_split))} '