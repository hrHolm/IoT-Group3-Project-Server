from django.apps import AppConfig


class DashboardConfig(AppConfig):
    name = 'dashboard'

    def ready(self):
        from . import mqtt_sub
        mqtt_sub.client.loop_start()
        #return super().ready()