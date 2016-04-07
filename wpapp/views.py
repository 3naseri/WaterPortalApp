from django.http import HttpResponse
from django.http import Http404
from django.template import loader
from django.shortcuts import render
from .models import Wstation, Wproperty
import datetime
import csv
from ftplib import FTP
from StringIO import StringIO
from django.utils.dateparse import parse_datetime
import matplotlib
matplotlib.use('TkAgg') 
matplotlib.use('Agg')
import numpy as np
import matplotlib.pyplot as plt
#
ftp = FTP('ftp.artemislab.ca')     
ftp.login('artemislab.ca', 'ArtAdmin49') 
ftp.cwd('SecureFtp/MET/CastleData/')
ftp.retrlines('LIST')
dataf = StringIO()
ftp.retrbinary('RETR Ridge.dat', dataf.write)
ftp.retrbinary('RETR Ridge.dat', open('/home/centos/waterportal/wproot/wpapp/static/Ridge.dat', 'wb').write)
ftp.quit()
#
file= open('/home/centos/waterportal/wproot/wpapp/static/Ridge.dat', 'rb')
data = csv.reader(file, delimiter=',')
table = [row for row in data]
di=92
daytable= table[len(table)-di:len(table)]
r_date=range(di)
r_temp=range(di)
r_rh=range(di)
for i in range(di):
	r_date[i] = parse_datetime(daytable[i][0])
	r_temp[i]=float(daytable[i][5])
	r_rh[i]=float(daytable[i][6])
#
#
plt.figure(1)
plt.subplot(211)
plt.plot( r_date, r_temp, 'bo')
plt.gcf().autofmt_xdate()

plt.subplot(212)
plt.plot(r_date, r_rh, 'r--')
plt.gcf().autofmt_xdate()
plotroot=plt.savefig('/home/centos/waterportal/wproot/wpapp/static/images/plot.png')
#
#
def index(request):
	station_list = Wstation.objects.all()
	template = loader.get_template('index.html')
	context = {'station_list': station_list,}
	return HttpResponse(template.render(context, request))

def wplots(request, station_id):
    try:
        station = Wstation.objects.get(pk=station_id)
    except Wstation.DoesNotExist:
        raise Http404("Station is not updated")
    return render(request, 'wplots.html', {'station': station})
