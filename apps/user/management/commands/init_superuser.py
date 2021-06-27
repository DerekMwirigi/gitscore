from django.core.management.base import BaseCommand

from django.conf import settings

from apps.user.models import User

class Command(BaseCommand):

    def handle(self, *args, **options):
        if User.objects.count() == 0:
            for admin in settings.ADMINUSERS:
                user = User(
                    username=admin['username'],
                    email=admin['email'],
                    is_active=True,
                    is_staff=True,
                    is_superuser=True
                )
                user.set_password(admin['password'])
                user.save()
        else:
            print('Admin accounts can only be initialized if no Accounts exist')