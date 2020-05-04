from django import forms

class SetpointForm(forms.Form):
    device_id = forms.IntegerField()
    setpoint_value = forms.IntegerField()

class IntensityForm(forms.Form):
    device_id = forms.IntegerField()
    intensity_value = forms.IntegerField(min_value=0, max_value=100)

    