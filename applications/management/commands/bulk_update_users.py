from django.core.management.base import BaseCommand
from applications.models import User

class Command(BaseCommand):
    help = 'Bulk update user details'

    def add_arguments(self, parser):
        parser.add_argument('--eligibility', type=str, help='Set eligibility for all users')
        parser.add_argument('--usernames', nargs='+', help='List of usernames to update')
        parser.add_argument('--field', type=str, help='Field to update')
        parser.add_argument('--value', type=str, help='New value')

    def handle(self, *args, **options):
        if options['eligibility']:
            User.objects.all().update(eligibility=options['eligibility'])
            self.stdout.write(f"Updated all users eligibility to {options['eligibility']}")
        
        if options['usernames'] and options['field'] and options['value']:
            users = User.objects.filter(username__in=options['usernames'])
            update_data = {options['field']: options['value']}
            users.update(**update_data)
            self.stdout.write(f"Updated {users.count()} users")