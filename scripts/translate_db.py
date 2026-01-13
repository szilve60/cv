"""
Translate DB text fields to English using LibreTranslate and populate *_en fields.

Usage:
  python scripts/translate_db.py

Requirements:
  pip install requests

Notes:
  - This script uses the public LibreTranslate instance at libretranslate.de by default.
    You can set environment variable LIBRETRANSLATE_URL to override, and LIBRETRANSLATE_API_KEY
    if you have a key for a paid/private instance.
  - It will only translate fields that are empty in their *_en counterpart.
  - Review results before publishing.
"""
import os
import sys
import time
import requests

if __name__ == '__main__':
    # Setup Django environment
    proj_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
    sys.path.insert(0, proj_root)
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'cvsite.settings')
    import django
    django.setup()

    from resume.models import Profile, Experience, Education, Skill, ProgrammingSkill

    API_URL = os.environ.get('LIBRETRANSLATE_URL', 'https://libretranslate.de/translate')
    API_KEY = os.environ.get('LIBRETRANSLATE_API_KEY')

    def translate_text(text, source='hu', target='en'):
        if not text or not text.strip():
            return ''
        payload = {
            'q': text,
            'source': source,
            'target': target,
            'format': 'text',
        }
        if API_KEY:
            payload['api_key'] = API_KEY
        try:
            r = requests.post(API_URL, data=payload, timeout=20)
            r.raise_for_status()
            data = r.json()
            return data.get('translatedText') or ''
        except Exception as e:
            print('Translation error:', e)
            return ''

    print('Translating Profiles...')
    for p in Profile.objects.all():
        changed = False
        if not p.title_en and p.title:
            t = translate_text(p.title)
            if t:
                p.title_en = t
                changed = True
                print('Profile title ->', t)
        if not p.summary_en and p.summary:
            t = translate_text(p.summary)
            if t:
                p.summary_en = t
                changed = True
                print('Profile summary ->', (t[:80] + '...') if len(t) > 80 else t)
        if changed:
            p.save()
            time.sleep(1)

    print('Translating Experiences...')
    for e in Experience.objects.all():
        changed = False
        if not e.role_en and e.role:
            t = translate_text(e.role)
            if t:
                e.role_en = t
                changed = True
        if not e.company_en and e.company:
            t = translate_text(e.company)
            if t:
                e.company_en = t
                changed = True
        if not e.description_en and e.description:
            t = translate_text(e.description)
            if t:
                e.description_en = t
                changed = True
        if changed:
            e.save()
            print('Translated experience id', e.id)
            time.sleep(1)

    print('Translating Education...')
    for ed in Education.objects.all():
        changed = False
        if not ed.degree_en and ed.degree:
            t = translate_text(ed.degree)
            if t:
                ed.degree_en = t
                changed = True
        if not ed.institution_en and ed.institution:
            t = translate_text(ed.institution)
            if t:
                ed.institution_en = t
                changed = True
        if changed:
            ed.save()
            print('Translated education id', ed.id)
            time.sleep(1)

    print('Translating Skills...')
    for s in Skill.objects.all():
        if not s.name_en and s.name:
            t = translate_text(s.name)
            if t:
                s.name_en = t
                s.save()
                print('Skill ->', t)
                time.sleep(0.6)

    print('Translating ProgrammingSkill languages...')
    for p in ProgrammingSkill.objects.all():
        if not p.language_en and p.language:
            t = translate_text(p.language)
            if t:
                p.language_en = t
                p.save()
                print('Prog lang ->', t)
                time.sleep(0.6)

    print('Done. Review translations in admin before publishing.')
