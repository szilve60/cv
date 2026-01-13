import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','cvsite.settings')
import django
django.setup()
from resume.models import Profile, Experience, Education, Skill

profile, _ = Profile.objects.update_or_create(
    name='Tóth Szilveszter',
    defaults={'title':'Villamosmérnök hallgató','summary':'Villamosmérnök hallgató.\nTelefon: +36 70 406 7543\nLinkedIn: /tothszilveszter\nEmail: toth.szilveszter60@gmail.com'}
)
Education.objects.update_or_create(profile=profile,institution='Óbudai Egyetem',degree='BSc – Villamosmérnök',defaults={'year':'2018 - várható: 2022'})
Education.objects.update_or_create(profile=profile,institution='Vak Bottyán János Katolikus Szakgimnázium',degree='Elektronikai műszerész',defaults={'year':'2014 - 2018'})
Experience.objects.update_or_create(profile=profile,company='Centervill Kft.',role='Műszaki előkészítő',defaults={'start':'2020. máj.','end':'2020. szept.','description':'Ajánlat készítés'})
Experience.objects.update_or_create(profile=profile,company='Robert Bosch Kft.',role='Operátor (gyakorlat)',defaults={'start':'2017. jún.','end':'2017. szept.'})
Experience.objects.update_or_create(profile=profile,company='Origo Film Studio',role='Díszletépítő',defaults={'start':'2020. szept.','end':'2021. márc.'})
Skill.objects.update_or_create(profile=profile,name='PLC programozás',defaults={'level':'Siemens / Schneider / Omron'})
Skill.objects.update_or_create(profile=profile,name='Rugalmasság')
Skill.objects.update_or_create(profile=profile,name='Magas terhelhetőség')
print('Imported profile id',profile.id)
