from django.shortcuts import render
from datetime import datetime
# Create your views here.
def current_time_date(req):
    current_time = datetime.now()
    return render(req,'date_time.html',{'current_time':current_time})