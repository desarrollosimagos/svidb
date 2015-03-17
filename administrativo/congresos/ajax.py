from django.utils import simplejson
from dajaxice.decorators import dajaxice_register

@dajaxice_register
def args_example(request, text):
    return simplejson.dumps({'message':'Your message is %s!' % text})