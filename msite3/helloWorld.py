import sys, os
sys.path.append('/Users/stephenyau/Documents/SP16/InfoSec/msite3')
os.environ['DJANGO_SETTINGS_MODULE']='settings'
from django.conf import settings


print ('This line will be printed.')
