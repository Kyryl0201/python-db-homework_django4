from django.apps import AppConfig
from django.db.models.signals import post_save


from common.signals import grade_update_handler
class CommonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'common'

    def ready(self):
        from common.models import StudentStatistics
        post_save.connect(grade_update_handler, sender="common.StudentStatistics")


