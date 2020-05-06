# Setup
You need to setup an environmental variable on your computer called 'CLOUDMQTT_URL', which holds the authentication and host info of the MQTT broker. 

**Important**: You must sign out and in again on your computer before any changes to your environmental values will take effect!
# Development
To avoid multiple mqtt callbacks happening at once:
```bash
python manage.py runserver --noreload
```
