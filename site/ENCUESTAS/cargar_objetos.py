import copy
from ENCUESTAS.models import Encuesta

objects_to_create = []
obj = Encuesta.objects.last()
for i in range(5):
   new_obj = copy.deepcopy(obj)
   new_obj.pk = None
   new_obj.cedula = i
   objects_to_create.append(new_obj)
Encuesta.objects.bulk_create(objects_to_create)