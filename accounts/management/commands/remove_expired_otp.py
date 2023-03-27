from django.core.management.base import BaseCommand
from accounts.models import OtpCode
from datetime import datetime, timedelta

class Command(BaseCommand):
    help='remove expired otp codes'
    
    def handle(self, *args, **options):
        exp_time = datetime.now() - timedelta(minutes=1)
        OtpCode.objects.filter(created__lt=exp_time).delete()
        self.stdout.write('expired otp code(s) removed')
        
        
        
    