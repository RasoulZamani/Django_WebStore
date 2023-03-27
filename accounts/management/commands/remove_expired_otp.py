from django.core.management.base import BaseCommand
from accounts.models import OtpCode
from datetime import datetime, timedelta
import pytz
class Command(BaseCommand):
    help='remove expired otp codes'
    
    def handle(self, *args, **options):
        exp_time = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)
        exp_opt = OtpCode.objects.filter(created__lt=exp_time)
        exp_opt.delete()
        if exp_opt:
            self.stdout.write('expired otp code(s) removed')
        
        
        
    