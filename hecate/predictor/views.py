from django.shortcuts import render

# Create your views here.

def medicalnadhpred(request):
    predictor={
        "chronic diseases":{"1":17,"2":8},
        "age":{"1":1.5,"2":6,"3":2.5},
        "literacy":{"1":3,"2":2,"3":1,"4":1},
        "region":{"1":6.5,"2":3.5},
        "medicine store":{"1":1.5,"2":3.5},
        "yearly income":{"1":4,"2":3,"3":2,"4":1},
        "job":{"1":2,"2":1},
        "side effects":{"1":3,"2":2},
        "asymptomatic":{"1":14,"2":5},
        "ineffective":{"1":4,"2":2}
    }
    context={"score":""}
    if request.method == "POST":
        chronicdisease=str(request.POST.get("chronicdisease"))
        age=str(request.POST.get("age"))
        literacy=str(request.POST.get("literacy"))
        region=str(request.POST.get("region"))
        medicinestore=str(request.POST.get("medicinestore"))
        annualincome=str(request.POST.get("annualincome"))
        job=str(request.POST.get("job"))
        sideeffects=str(request.POST.get("sideeffects"))
        asymptomatic=str(request.POST.get("asymptomatic"))
        ineffective=str(request.POST.get("ineffective"))
        score=(predictor["chronic diseases"][chronicdisease]+predictor["age"][age]
               +predictor["job"][job]+predictor["side effects"][sideeffects]+predictor["asymptomatic"][asymptomatic]
               +predictor["medicine store"][medicinestore]+predictor["region"][region]+predictor["literacy"][literacy]
               +predictor["yearly income"][annualincome]+predictor["ineffective"][ineffective])
        context["score"]=score/80*100
        return render(request, 'predictor/predictor.html', context)
    else:
        return render(request, 'predictor/predictor.html', context)
    
    
