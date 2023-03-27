from accounts.models import OtpCode
from datetime import datetime, timedelta
import pytz

def remove_exp_otp(self, *args, **options):
    exp_time = datetime.now(tz=pytz.timezone('Asia/Tehran')) - timedelta(minutes=2)
    OtpCode.objects.filter(created__lt=exp_time).delete()
        
        
    