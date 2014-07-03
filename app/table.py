from django.shortcuts import render
from django.views.generic import TemplateView
from django.shortcuts import *
from app.models import *


def table_delete(request):

    TableEntry.objects.filter(title__iexact=request.GET.get("table_name","")).delete()
    return redirect("/")
 
def table_create(request):

    TableEntry.objects.create(title=request.GET.get("table_name",""))
    return redirect("/")


def table_read(request):


    TableList = []
    for TableEntryObject in TableEntry.objects.all():
        if ReservationEntry.objects.filter(table=TableEntryObject).count() == 0:
           TableList.append({'table': TableEntryObject.title, 'reserved': ''})
        else:
            TableList.append({'table': TableEntryObject.title, 'reserved': ReservationEntry.objects.get(table=TableEntryObject).name })

   
    return render(request, 'table/table_show.html',
          { 'page_active': 3,
          'res': TableList })