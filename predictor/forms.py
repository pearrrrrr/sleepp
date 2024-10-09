from django import forms

class SleepDisorderForm(forms.Form):
    gender = forms.ChoiceField(choices=[('Male', 'Male'), ('Female', 'Female')])
    age = forms.IntegerField()
    sleep_duration = forms.FloatField()
    quality_of_sleep = forms.FloatField()
    physical_activity_level = forms.FloatField()
    stress_level = forms.FloatField()
    bmi_category = forms.ChoiceField(choices=[('Normal', 'Normal'), ('Normal weight', 'Normal weight'), ('Overweight', 'Overweight'), ('Obese', 'Obese')])
    heart_rate = forms.FloatField()
    daily_steps = forms.IntegerField()
    systolic_bp = forms.FloatField()
    diastolic_bp = forms.FloatField()
