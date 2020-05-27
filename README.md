# Content of repository
This is a Django Framework project. The 'dashboard'-folder holds the web pages used in the project, such as commanding the setpoint and intensity of a device, and seeing historical values.

# Setup
You need to setup an environmental variable on your computer called 'CLOUDMQTT_URL', which holds the authentication and host info of the MQTT broker. 

**Important**: You must sign out and in again on your computer before any changes to your environmental values will take effect!
# Development
To avoid multiple mqtt callbacks happening at once:
```bash
python manage.py runserver --noreload
```
