from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
def time_changes(req):
    current_time = datetime.now()
    time_ahead = current_time+ timedelta(hours=4)
    time_behind = current_time-timedelta(hours=4)
    return render(req, 'time.html',{'current_time':current_time,'time_ahead':time_ahead,'time_behind':time_behind})