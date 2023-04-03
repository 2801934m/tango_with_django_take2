import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tango_with_django_project.settings')

import django
django.setup()
from rango.models import Category, Page

def populate():
    # Create list of dictionaries containing pages we want to add for each
    # category. Then create dictionary of dictionaries for categories. This will
    # allow us to iterate through each data structure, and add the data to our
    # models.

    python_pages = [
        {'title': 'Official Python Tutorial',
        'url':'http://docs.python.org/3/tutorial/',
        'views': 13},
        {'title':'How to Think like a Computer Scientist',
        'url':'http://www.greenteapress.com/thinkpython/',
        'views': 12},
        {'title':'Learn Python in 10 Minutes',
        'url':'http://www.korokithakis.net/tutorials/python/',
        'views': 11} ]
        # ADDED VIEWS FIELD TO PAGES

    django_pages = [
        {'title':'Official Django Tutorial',
        'url':'https://docs.djangoproject.com/en/2.1/intro/tutorial01/',
        'views': 10},
        {'title':'Django Rocks',
        'url':'http://www.djangorocks.com/',
        'views': 9},
        {'title':'How to Tango with Django',
        'url':'http://www.tangowithdjango.com/',
        'views': 8} ]
        # ADDED VIEWS FIELD TO PAGES

    other_pages = [
        {'title':'Bottle',
        'url':'http://bottlepy.org/docs/dev/',
        'views': 7},
        {'title':'Flask',
        'url':'http://flask.pocoo.org',
        'views': 6} ]
        # ADDED VIEWS FIELD TO PAGES

    cats = {'Python': {'pages': python_pages, 'views': 128, 'likes': 64},
            'Django': {'pages': django_pages, 'views': 64, 'likes': 32},
            'Other Frameworks': {'pages': other_pages, 'views': 32, 'likes': 16} }

    # If you want to add more categories or pages, add them to the dictionaries
    # above.

    # The code below goes through the cats dictionary, then adds each category,
    # and then adds all the associated pages for that category.
    for cat, cat_data in cats.items():
        c = add_cat(cat, views=cat_data['views'], likes=cat_data['likes'])
        for p in cat_data['pages']:
            add_page(c, p['title'], p['url'], p['views'])
            # ADDED AN ADDITIONAL p['views'] PARAMETER TO ABOVE LINE. LOOK HERE
            # IF TEST FAILS.

    # Print out the categories we have added.
    for c in Category.objects.all():
        for p in Page.objects.filter(category=c):
            print(f'- {c}: {p}')
    # CHECK THIS SPOT FIRST IF THERE ARE ANY ERRORS/TEST FAILURES.

def add_page(cat, title, url, views=0):
    p = Page.objects.get_or_create(category=cat, title=title)[0]
    p.url=url
    p.views=views
    p.save()
    return p
    # CURRENT ASSUMPTION IS THAT THIS FUNCTION DOES NOT NEED TO BE MODIFIED.

def add_cat(name, views=0, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.views = views
    c.likes = likes
    c.save()
    return c

# Start execution here!
if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
