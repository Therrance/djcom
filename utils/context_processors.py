from catalog.models import Category
from djcom import settings

def djcom(request):
    return {
        'active_categories': Category.object.filter(is_active=True),
        'site_name': settings.SITE_NAME,
        'meta_keywords': settings.META_KEYWORDS,
        'meta_description': settings.META_DESCRIPTION,
        'request': request
    }