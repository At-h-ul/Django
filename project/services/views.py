from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect
import time 
from .models import ServiceEnquiry, NewProducts, UsedProducts, OnDmndLap, OnDmndOth, OnDmndPc

def service(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        pro_name = request.POST.get('product', '')
        pro_manuf = request.POST.get('manufacturer', '')
        pro_issue = request.POST.get('issue', '')
        u_phone = request.POST.get('phone', '')
        u_address = request.POST.get('address', '')
        enq_date = request.POST.get('date', '')
        enq_time = request.POST.get('time', '')


        enquiry = ServiceEnquiry(product_name = pro_name, product_manuf = pro_manuf, product_issue = pro_issue, user_phone = u_phone, user_address = u_address, enquiry_date = enq_date, enquiry_time = enq_time)
        enquiry.save()
     

        time.sleep(2)
        response =  HttpResponse('Thank you for your enquiry! We will get back to you soon.')
        response['Refresh'] = '2;url=dashboard'
        return response

    
    else:
        return render(request, 'servenq.html')


def newproduct(request):
    newproducts = NewProducts.objects.all()
    return render(request, 'newprod.html', {'newproducts': newproducts})

def oldproduct(request):
    oldproducts = UsedProducts.objects.all()
    return render(request, 'oldprod.html', {'oldproducts': oldproducts})

def demandlaptop(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        lap_brnd = request.POST.get('brand', '')
        lap_model = request.POST.get('model', '')
        lap_processor = request.POST.get('processor', '')
        lap_ram = request.POST.get('ram', '')
        lap_storage = request.POST.get('storage', '')
        lap_budget = request.POST.get('budget', '')
        


        dmndlaptop = OnDmndLap(dmndlap_brand = lap_brnd, dmndlap_model = lap_model, dmndlap_proce = lap_processor, dmndlap_ram = lap_ram, dmndlap_stor = lap_storage, dmndlap_budg = lap_budget)
        dmndlaptop.save()
     

        time.sleep(2)
        resp =  HttpResponse('Thank you for your request! We will get back to you soon.')
        resp['Refresh'] = '2;url=dashboard'
        return resp
    else:
        return render(request, 'dmndlap.html')

def demandpc(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        pc_processor = request.POST.get('proce', '')
        pc_motherboard = request.POST.get('motherboard', '')
        pc_ram = request.POST.get('ram1', '')
        pc_storage = request.POST.get('storage1', '')
        pc_gfxcard = request.POST.get('gfxcard', '')
        pc_cabinet = request.POST.get('cabinet', '')
        pc_psu = request.POST.get('psu', '')
        pc_budget = request.POST.get('budget1', '')


        dmndpc = OnDmndPc(dmndpc_proc = pc_processor, dmndpc_mobo = pc_motherboard, dmndpc_ram = pc_ram, dmndpc_stor = pc_storage, dmndpc_gfx = pc_gfxcard, dmndpc_cab = pc_cabinet, dmndpc_psu = pc_psu, dmndpc_budg = pc_budget)
        dmndpc.save()
     

        time.sleep(2)
        res =  HttpResponse('Thank you for your request! We will get back to you soon.')
        res['Refresh'] = '2;url=dashboard'
        return res
    else:
        return render(request, 'dmndpc.html')

def demandothers(request):
    if request.method == 'POST':
        # Retrieve form data from POST request
        oth_prod = request.POST.get('prod', '')
        oth_desc = request.POST.get('proddesc', '')
        oth_budg = request.POST.get('bud', '')

        dmndoth = OnDmndOth(dmndoth_prod = oth_prod, dmndoth_desc = oth_desc, dmndoth_budg = oth_budg)
        dmndoth.save()
     

        time.sleep(2)
        re =  HttpResponse('Thank you for your request! We will get back to you soon.')
        re['Refresh'] = '2;url=dashboard'
        return re
    else:
        return render(request, 'dmndoth.html')