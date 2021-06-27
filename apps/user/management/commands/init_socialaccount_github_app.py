from django.core.management.base import BaseCommand

from django.contrib.sites.models import Site

from allauth.socialaccount.models import SocialApp

from django.conf import settings

class Command(BaseCommand):

    def handle(self, *args, **options):
        site, site_created = Site.objects.update_or_create(
            id=1,
            name = 'http://127.0.0.1:8099',
            domain = 'http://127.0.0.1:8099'
        )
        app, app_created = SocialApp.objects.update_or_create(
            id=1,
            provider = 'github',
            name = 'gitscore',
            key = settings.SOCIAL_OAUTH_GITHUB_CLIENT_ID,
            client_id  = settings.SOCIAL_OAUTH_GITHUB_CLIENT_ID,
            secret = settings.SOCIAL_OAUTH_GITHUB_SCRET_KEY
        )
        # update socialapp
        site = Site.objects.get(id=1)
        app = SocialApp.objects.get(id=1)
        app.sites.add(site)
        app.save()
