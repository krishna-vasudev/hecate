from django.shortcuts import render,redirect
from accounts.models import Patient,Medical
from eprescribe.models import Prescription,Medicine
# Create your views here.
def home(request):
    if request.user.is_anonymous or request.user.is_active == False:
        return render(request,"home/new-user.html")
    if request.method =='POST':
        prescriptionid = request.POST.get('prescriptionid')
        return redirect(f'/eprescribe/doctorform/{prescriptionid}')
    if Patient.objects.filter(patient=request.user).exists():
        return render(request,"home/patient-home.html")
    elif Medical.objects.filter(medical=request.user).exists():
        return render(request,"home/medicalHome.html")
    else:
        return render(request, "home/new-user.html")

def myprofile(request):
    if request.user.is_anonymous or request.user.is_active == False:
        return redirect('/')
    all_prescriptions=Prescription.objects.filter(patient_email_id=request.user.email)
    return render(request,"home/profile.html",{"prescriptions":all_prescriptions})
