from django.shortcuts import render,redirect
from accounts.models import Medical,Patient
from .models import Prescription,Medicine
from django.contrib import messages

# Create your views here.
def addnewpatient(request):
    if request.user.is_anonymous or request.user.is_active == False:
        return redirect('/')
    if Medical.objects.filter(medical=request.user).exists()==False:
        return redirect('/')
    if request.method =="POST":
        medical=Medical.objects.get(medical=request.user)
        literacy=request.POST.get('literacy')
        age=request.POST.get('age')
        sex=request.POST.get('sex')
        full_name=request.POST.get('fullname')
        region=request.POST.get('region')
        patient_email_id=request.POST.get('email')
        doctor_name=request.POST.get('doctorname')
        new_prescription=Prescription(medical=medical,literacy=literacy,age=age,sex=sex,full_name=full_name,region=region,patient_email_id=patient_email_id,doctor_name=doctor_name)
        new_prescription.save()
        messages.success(request, 'Prescription saved successfully')
        return redirect('/')
    return render(request,'eprescribe/recep.html')

def doctorform(request,prescriptionid):
    if request.user.is_anonymous or request.user.is_active == False:
        return redirect('/')
    if (Medical.objects.filter(medical=request.user).exists() and Prescription.objects.filter(medical=Medical.objects.get(medical=request.user)).exists()):
        if request.method=='POST':
            edit_prescription = Prescription.objects.get(id=prescriptionid)
            edit_prescription.disease_description=request.POST.get('disease_description')
            edit_prescription.save()

            name1=request.POST.get('name1')
            frequency1=request.POST.get('frequency1')
            duration1=request.POST.get('duration1')
            food1=request.POST.get('food1')
            new_medicine1=Medicine(prescription=edit_prescription, name=name1, frequency=frequency1,duration=duration1,food=food1)
            new_medicine1.save()

            name2=request.POST.get('name2')
            frequency2=request.POST.get('frequency2')
            duration2=request.POST.get('duration2')
            food2=request.POST.get('food2')
            new_medicine2=Medicine(prescription=edit_prescription, name=name2, frequency=frequency2, duration=duration2,food=food2)
            new_medicine2.save()

            name3=request.POST.get('name3')
            frequency3=request.POST.get('frequency3')
            duration3=request.POST.get('duration3')
            food3=request.POST.get('food3')
            new_medicine3=Medicine(prescription=edit_prescription,name=name3,frequency=frequency3,duration=duration3,food=food3)
            new_medicine3.save()

            return redirect(f'/eprescribe/prescription/{prescriptionid}')
        
        context = {
            "prescription": Prescription.objects.get(id=prescriptionid)
        }
        return render(request,'eprescribe/prescription.html',context)

    return redirect('/')

def prescription(request,prescriptionid):
    if request.user.is_anonymous or request.user.is_active == False:
        return redirect('/')
    if ((Medical.objects.filter(medical=request.user).exists() and Prescription.objects.filter(medical=Medical.objects.get(medical=request.user)).exists()) or Prescription.objects.filter(patient_email_id=request.user.email).exists()):
        context={
            "prescription": Prescription.objects.get(id=prescriptionid),
            "medicines": Medicine.objects.filter(prescription=Prescription.objects.get(id=prescriptionid))
        }
        return render(request,'eprescribe/pres-details.html',context)
    
    return redirect('/')

