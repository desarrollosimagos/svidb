from django.db.models import Q
from django.utils.html import escape
from especies.models import *
from posiciones.models import *
from ajax_select import LookupChannel


class ClasesLookup(Clases):
    def get_query(self,q,request):
        return Clases.objects.filter(Q(name__istartswith=q))

    def format_result(self,clase):
        return u'%s' % (clase.name)

    def format_item(self,Clases):
        return unicode(Clases)

    def get_objects(self,ids):
        return Clases.objects.filter(pk__in=ids).order_by('name')



