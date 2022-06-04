from django import template
from django.db.models.lookups import LessThanOrEqual
from app.models import *
import random
register = template.Library()

tags_names_test = ['perl', 'Python', 'TechnoPark'],
                    

best_user_names_test = ['Mr.Freeman', 'Dr.House', 'Bender', 'Queen Victoria', 'V.Pupkin']

questions_list = User.objects.filter(id__gte = 10010)
questions_list = list(questions_list) 
questions_list2 = []
n = 0
for i in reversed(questions_list):
    if n < 5:
        questions_list2.append(i)
        n = n + 1

for i in questions_list2:
    print(i)

tags_list = Tag.objects.popular()
tags_list1 = tags_list[0:3]
tags_list2 = tags_list[4:6]
tags_list3 = tags_list[7:10]


@register.simple_tag()
def show_tags():
    tags = {"str1":tags_list1, "str2": tags_list2, "str3": tags_list3}
    return tags

@register.simple_tag()
def show_best_users():
    
    usnames = questions_list2
    
    return usnames