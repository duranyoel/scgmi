#encoding:utf-8_
__author__ = 'admin'
from dajax.core import Dajax
from dajaxice.decorators import dajaxice_register
from smi.models import Estado,Municipio,Parroquia

@dajaxice_register
def updatecombomunicipio(request,option):
    dajax = Dajax()
    municipio =Municipio.objects.all()
    options = [['Seleccione Uno'],
               municipio
               ]
    out =[]

    for option in options[int(option)]:
        out.append("<option value='%s'>%s</option>" % option)

    dajax.assign('#id_municipio','innerHTML',''.join(out))
    return dajax.json()
