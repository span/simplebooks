import logging
import json
from django.db.models import Sum
from django.http import HttpResponse
from django.shortcuts import render_to_response
from django.template import RequestContext
from simplebooksform.models import verification
from simplebooksform.forms import verification_form

def home(request):
    return render_to_response("index.html")
    
def add_verification(request):
    # Create new verification form model
    if request.method == "POST":
        form = verification_form(request.POST, request.FILES)
        if form.is_valid():
            # Create new verification
            form.save()
            message = "Verification was saved!"
        else:
            message = "Invalid form!"
    else:
        form = verification_form()
        message = "Add a title and press Enter"
        
    variables = RequestContext(request, {'form' : form, 'message' : message})
    
    return render_to_response('verification_form.html', variables)
    
def view_verifications(request):
    # Use imported verifications model for data
    verifications = verification.objects.all()#[:10] # first 10
    return render_to_response("verifications.html", {"verifications" : verifications})
    
def get_verifications(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        verifications = verification.objects.filter(title__icontains = q )[:20]
        results = []
        for v in verifications:
            verification_json = {}
            verification_json['id'] = v.id
            verification_json['label'] = v.title
            verification_json['value'] = v.title
            results.append(verification_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)
    
def result(request):
    expense = verification.objects.filter(account = 'expense').aggregate(Sum('amount'))
    income = verification.objects.filter(account = 'income').aggregate(Sum('amount'))    
    tax6in = verification.objects.filter(account = 'expense').aggregate(Sum('tax6'))
    tax12in = verification.objects.filter(account = 'expense').aggregate(Sum('tax12'))
    tax25in = verification.objects.filter(account = 'expense').aggregate(Sum('tax25'))
    tax25out = verification.objects.filter(account = 'income').aggregate(Sum('tax25'))
    
    # TODO
    # Refactor these requests to a single db query and pass in a better structure
    # to the template.
    results = {}
    results['expense'] = xstr(expense['amount__sum'])
    results['income'] = xstr(income['amount__sum'])
    results['tax6in'] = xstr(tax6in['tax6__sum'])
    results['tax12in'] = xstr(tax12in['tax12__sum'])
    results['tax25in'] = xstr(tax25in['tax25__sum'])
    results['tax25out'] = xstr(tax25out['tax25__sum'])
    results['tax_in_total'] = str_to_int(results['tax6in']) + str_to_int(results['tax12in']) + str_to_int(results['tax25in'])
    results['tax_out_total'] = results['tax25out']
    results['tax_subtotal'] = str_to_int(results['tax_out_total']) - results['tax_in_total']
    results['subtotal'] = str_to_int(results['income']) - str_to_int(results['expense'])
    
    return render_to_response('result.html', {'results' : results})
    

def str_to_int(s):
    try:
        x = int(s)
    except ValueError:
        x = 0
    return x

def int_to_str(i):
    try:
        s = str(i)
    except ValueError:
        s = ''
    return s

def xstr(s):
    return '0' if s is None else str(s)

