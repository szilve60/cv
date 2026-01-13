def cv_lang(request):
    """Expose the desired UI language from cookie to templates as `cv_lang`.

    Expected cookie values: 'en' for English, anything else or missing -> default (Hungarian/original).
    """
    lang = request.COOKIES.get('cv_lang')
    return {'cv_lang': lang}
