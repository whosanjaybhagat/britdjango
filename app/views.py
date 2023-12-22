from django.shortcuts import render,redirect, reverse
from django.http import HttpResponse
from django.contrib.auth import authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


from .forms import DynamicFormDataForm, DynamicFormDataFormSet
from .models import DynamicFormData, MyModel


def dynamic_form_view(request):
    request.session['total'] = 0
    total = 0
    try:
        if request.method == 'POST':
            formset = DynamicFormDataFormSet(request.POST, queryset=DynamicFormData.objects.none())
            if formset.is_valid():
                instances = []
                for form in formset:
                    if form.is_valid():
                        instance = form.save(commit=False)
                        instances.append(instance)
                        try:
                            # Create an instance of MyModel
                            new_data = MyModel()
                            item =  form.cleaned_data['item']
                            price =  form.cleaned_data['price']
                            total = total + float(price)
                            new_data.name = str(item)
                            new_data.description = str(price)
                            new_data.save()
                        except Exception as e:
                            print(e)
                        print(f"Form data1: {form.cleaned_data}")
                        print(f"Instance before save2: {instance}")
                        instance.save()
                        print(f"Instance after save3: {instance}")
                    else:
                        print(f"Form errors: {form.errors}")
                request.session['total'] = total        
                return redirect('successview/')  # Use the correct URL name here
            else:
                print(f"Formset errors: {formset.errors}")
        else:
            formset = DynamicFormDataFormSet(queryset=DynamicFormData.objects.none())

        return render(request, 'dynamic_form.html', {'formset': formset})

    except:
        # messages.warning(request, "Incorrect data")
        # return redirect(request.path)
        return redirect('successview/') 
        # return (render(request, "reload.html")) 




        

def success_view(request):
    context = {}
    data = (request.session.get('total', 'no data'))
    context['data'] = data
    return (render(request, "output.html", context=context)) 














def test(request):
    return (render(request, "login.html"))


def login_details(request):
    if request.method == "POST":
        data = request.POST.dict()
        user = data['user']
        pswd = data['pass']
        print("user--->", user)
        print("Password--->", pswd)




        user = authenticate(username=user, password=pswd)
        if user is not None:
            print("logged")
            messages.success(request, "Logged-In Successfully")
            return redirect('form_data/')
        
        else:
            messages.warning(request, "Incorrect Username or Password")

    return (render(request, "login.html"))        


        
          

