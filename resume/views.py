from django.shortcuts import render
from .models import Profile


def index(request):
    # show the most recently added profile (prevents duplicates showing)
    profile = Profile.objects.order_by('-id').first()
    # Debug: log cookies and detected cv_lang for troubleshooting language rendering
    try:
        cv_lang = request.COOKIES.get('cv_lang')
        print('DEBUG: request.COOKIES =', request.COOKIES)
        print('DEBUG: cv_lang =', cv_lang)
    except Exception as _:
        # don't break production; just ignore logging errors
        pass
    return render(request, 'resume/index.html', {'profile': profile})


def english_index(request):
    # Render a dedicated English template that directly uses the _en fields
    profile = Profile.objects.order_by('-id').first()
    # Log cv_lang and cookies for debugging as well
    try:
        print('DEBUG english page request.COOKIES =', request.COOKIES)
    except Exception:
        pass
    return render(request, 'resume/index_en.html', {'profile': profile})
