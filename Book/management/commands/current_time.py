from django.core.management.base import BaseCommand
from django.utils import timezone

# creating the custom command for current time.
# Ex-  python manage.py current_time -----output -> current time.

class Command(BaseCommand):
    help = 'Displays current time'

    def handle(self, *args, **kwargs):
        time = timezone.now().strftime('%X')
        self.stdout.write("It's now %s" % time)