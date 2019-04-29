from django.shortcuts import render
from django.conf import settings
from SidApp.models import Motors
from SidApp import forms
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.contrib import messages
from django.http import *
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponse
from django.views.generic import View
# from .util import render_to_pdf
from django.template.loader import get_template
from django.template import context
import xhtml2pdf.pisa as pisa
from .util import link_callback
from SidApp import util

# business logic starts from here...
def index_view(request):
    return render(request,'SidApp/index.html')

# Consumer data storing from the form...
def CreateView(request):
    Form =forms.MotorsForm()
    if request.method == 'POST':
        Form = forms.MotorsForm(request.POST)
        if Form.is_valid():
            Form.save(commit=True)
            return render(request,'SidApp/index.html')
        else:
            Form = forms.MotorsForm()
    args ={'Form':Form}
    return render(request,'SidApp/services.html',args)

 #search the data from database....
def search_view(request,**kwargs):
    banner =("SIDHARTHA MOTORS",
    "SALES & SERVICES",
    "H.No.5-11-19 Plot No.61",
    "Beside SBI bank Moula Ali",
    "Hyd-40 PH.040-64533190  40023029,Cell:9392499190 Email:nbreddy909@gmail.com")
    if request.method =='POST':
        srch = request.POST['srh']
        if srch:
            match = Motors.objects.filter(Q(Mobile_Number__exact=srch )|
                                          Q(Customer_Name__iexact=srch))
            if match:
                try:
                    phn = match[0].Mobile_Number
                except Exception as e:
                    # print(e)
                    phn= None

                return render(request,'SidApp/search.html',{'sr':match,'banner':banner,'phn':phn})


            else:
                messages.error(request,'No Results Found!!')
        else:
            return HttpResponseRedirect('/search/')

    return render(request,'SidApp/search.html')


# rendering to pdf
def render_pdf_view(request):
    phno=request.GET.get('phn')
    match = Motors.objects.filter(Q(Mobile_Number__exact=phno))

    # match=search_view(request)
    template_path = 'SidApp/printpdf.html'

    context = {'sr':match,'myvar': "SIDHARTHA MOTORS"
    "SALES & SERVICES,"
    "H.No.5-11-19 Plot No.61"
    "Beside SBI bank Moula Ali"   "Hyd-40 PH.040-64533190  40023029 Cell:9392499190 Email:nbreddy909@gmail.com",
    }

    # Create a Django response object, and specify content_type as pdf
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="sidhartha.pdf"'
    # find the template and render it.
    template = get_template(template_path)
    html = template.render((context))
    # create a pdf
    pisaStatus = pisa.CreatePDF(
       html, dest=response, link_callback=link_callback)
    # if error then show some funy view
    if pisaStatus.err:
       return HttpResponse('We had some errors <pre>' + html + '</pre>')
    return response



# contact page view...
def contact_view(request):
    
    return render(request,'SidApp/contact.html')



























# result page...
# class Generate_pdf(View):
# def Generate_pdf(request):
#     template = get_template('SidApp/printpdf.html')
#     banner =("SIDHARTHA MOTORS",
#         "SALES & SERVICES",
#         "H.No.5-11-19 Plot No.61",
#         "Beside SBI bank Moula Ali",
#         "Hyd-40 PH.040-64533190  40023029,Cell:9392499190 Email:nbreddy909@gmail.com")
#     html = template.render({'banner':banner})
#
#     file = open('test.pdf',"w+b")
#     pisaStatus = pisa.CreatePDF(html.encode('utf-8'), dest=file,encoding='utf-8')
#
#     file.seek(0)
#     pdf =file.read()
#     file.close()
#
#     pdf = render_to_pdf('SidApp/printpdf.html',{'banner':banner})
#     return HttpResponse(pdf, content_type='application/pdf' )

#
# def print(request):
#     return render(request,'SidApp/testprint.html')
