from django.conf import settings
from django.urls import translate_url


def site_context(request):
    """Expose SITE_URL and alternate-language URLs (for hreflang + switcher)."""
    site_url = f"{request.scheme}://{request.get_host()}"
    alts = []
    for code, _name in settings.LANGUAGES:
        alts.append((code, translate_url(request.path, code)))
    return {"SITE_URL": site_url, "ALT_LANG_URLS": alts}
