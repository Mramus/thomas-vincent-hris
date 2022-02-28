from django.contrib import admin

from .models import UserT
admin.site.register(UserT)

from .models import WorkerT
admin.site.register(WorkerT)

from .models import ProjectT
admin.site.register(ProjectT)

from .models import EvaluationReportT
admin.site.register(EvaluationReportT)

from .models import AssignmentT
admin.site.register(AssignmentT)
