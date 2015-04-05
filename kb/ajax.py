from dajaxice.decorators import dajaxice_register
#from django.utils import simplejson
import json
import logging
import datetime

# Create your views here.
logger = logging.getLogger('my_log')

@dajaxice_register
def sayhello(request):
#    return simplejson.dumps({'message':'Hello World'})
    logger.debug("*** Hi I am in sayhello")
    return json.dumps({'message':'Hello World'})

@dajaxice_register
def nowtime(request):
    now = datetime.datetime.now()    
    return json.dumps({'dt':now.strftime('%Y-%m-%d %H:%M:%S')})
    
    