from .models import Location

def menu_links(request):
    links = Location.objects.all()
    return {'links':links}