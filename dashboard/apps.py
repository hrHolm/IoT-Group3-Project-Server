from django.apps import AppConfig


class DashboardConfig(AppConfig):
    name = 'dashboard'

    def ready(self):
        from . import mqtt_sub
        mqtt_sub.client.loop_start()

        #Used for evaluation
        #from . import dummy_data
        #dummy_data.insert_dummy_data_for_test(500000)