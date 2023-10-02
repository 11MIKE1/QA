from django.shortcuts import render
from webapp.models import First_Title, Second_Title, Title, Third_title, Forth_title, Fifth_title, Sixth_title, Seventh_title,Eighth_title,Footer

def post(request):
    first_Title = First_Title.objects.all()
    second_Title = Second_Title.objects.all()
    title = Title.objects.all()
    third_title = Third_title.objects.all()
    forth_Title = Forth_title.objects.all()
    fifth_Title = Fifth_title.objects.all()
    sixth_Title = Sixth_title.objects.all()
    seventh_Title = Seventh_title.objects.all()
    footer = Footer.objects.all()
    eighth_title = Eighth_title.objects.all()


    context={
        'first_titles':first_Title, 'second_titles':second_Title, 'titles':title, 'third_titles':third_title, 'forth_titles':forth_Title,
            'fifth_titles':fifth_Title, 'sixth_titles':sixth_Title, 'seventh_titles':seventh_Title, 'eighth_titles':eighth_title, 'footers':footer
             }
    return render(request, 'index.html', context)

