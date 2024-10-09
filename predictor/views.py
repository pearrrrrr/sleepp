from django.shortcuts import render
from .forms import SleepDisorderForm
import pickle

def predict(request):
    if request.method == 'POST':
        form = SleepDisorderForm(request.POST)
        if form.is_valid():
            # โหลดโมเดลที่ถูกฝึกไว้
            with open('predictor/Sleep_Dtree_Model.pickle', 'rb') as model_file:
                model = pickle.load(model_file)

            # ดึงข้อมูลจากฟอร์ม
            gender = form.cleaned_data['gender']
            if gender == 'Male':
                gender_encoded = 0
            elif gender == 'Female':
                gender_encoded = 1
            else:
                gender_encoded = -1  # หรือค่าที่เหมาะสมสำหรับ 'Other'

            # แปลงค่า BMI Category
            bmi_category = form.cleaned_data['bmi_category']
            if bmi_category == 'Normal':
                bmi_category_encoded = 0
            elif bmi_category == 'Normal Weight':
                bmi_category_encoded = 1
            elif bmi_category == 'Overweight':
                bmi_category_encoded = 2
            elif bmi_category == 'Obese':
                bmi_category_encoded = 3
            
            # สร้างข้อมูลที่ใช้สำหรับการทำนาย
            input_data = [
                gender_encoded,
                form.cleaned_data['age'],
                form.cleaned_data['sleep_duration'],
                form.cleaned_data['quality_of_sleep'],
                form.cleaned_data['physical_activity_level'],
                form.cleaned_data['stress_level'],
                bmi_category_encoded,
                form.cleaned_data['heart_rate'],
                form.cleaned_data['daily_steps'],
                form.cleaned_data['systolic_bp'],
                form.cleaned_data['diastolic_bp']
            ]
            
            # แปลงข้อมูลให้เหมาะสมกับโมเดล
            prediction = model.predict([input_data])

            # แปลงผลลัพธ์ให้เป็นชื่อ Sleep Disorder
            sleep_disorder_map = {0: 'None', 1: 'Sleep Apnea', 2: 'Insomnia'}
            sleep_disorder_result = sleep_disorder_map.get(prediction[0], 'Unknown')

            # ส่งผลลัพธ์ไปยังเทมเพลต
            return render(request, 'predictor/result.html', {'form': form, 'prediction': sleep_disorder_result})
    else:
        form = SleepDisorderForm()

    return render(request, 'predictor/form.html', {'form': form})
