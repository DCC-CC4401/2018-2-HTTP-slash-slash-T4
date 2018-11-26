from django.contrib import admin
from .models import Curso
from .models import Coevaluacion
from .models import Equipo
from .models import Info_Coevaluacion
from .models import Integrante_Curso
from .models import Integrante_Equipo
from .models import Pendiente
from .models import Pregunta
# Register your models here.
admin.site.register(Curso)
admin.site.register(Coevaluacion)
admin.site.register(Equipo)
admin.site.register(Info_Coevaluacion)
admin.site.register(Integrante_Equipo)
admin.site.register(Integrante_Curso)
admin.site.register(Pendiente)
admin.site.register(Pregunta)