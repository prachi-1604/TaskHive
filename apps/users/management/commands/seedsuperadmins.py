from django.core.management.base import BaseCommand

from apps.users.models import User

class Command(BaseCommand):
    """
    Command to seed two predefined Super Admins into the database.
    """
    help = "Seed two predefined Super Admins into the database"

    def handle(self, *args, **kwargs):
        super_admins = [
            {
                "name": "Admin One",
                "email": "admin1@taskhive.com",
                "password": "AdminPass123",
                "country": "India",
                "languages_known": ["Hindi", "English"],
                "role": "ADMIN"
            },
            {
                "name": "Admin Two",
                "email": "admin2@taskhive.com",
                "password": "AdminPass456",
                "country": "USA",
                "languages_known": ["English"],
                "role": "ADMIN"
            }
        ]

        for admin in super_admins:
            if not User.objects.filter(email=admin["email"]).exists():
                User.objects.create(**admin)
                self.stdout.write(self.style.SUCCESS(f'Super Admin {admin["email"]} created'))
            else:
                self.stdout.write(self.style.WARNING(f'{admin["email"]} already exists'))
