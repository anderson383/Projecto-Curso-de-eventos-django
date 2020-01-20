from django.shortcuts import render, redirect, get_object_or_404
from apps.users.models import User
from .forms import EventoForm
from .models import Category, Event
from django.views import View
# Create your views here.

class IndexView(View):
    def get(self,request):
        events = Event.objects.all().order_by("-created")[:6]
        categories = Category.objects.all()
        contexto = {
            'events': events,
            'categories': categories
        }
        return render(request,"events/index.html", contexto)
class PanelView(View):
    def get(self,request):
        events = Event.objects.filter(organizer=request.user).order_by('is_free','-created')
        cantidad_eventos = events.count()
        context={'events':events,'cantidad':cantidad_eventos}
        return render(request, "events/panel.html",context)

class CrearEventView(View):
    def get(self,request):
        modelform = EventoForm()
        return render(request, 'events/crear_evento.html',{'form':modelform})
    
    def post(self,request):
        organizador = request.user
        even_organizer = Event()
        even_organizer.organizer = organizador
        modelform = EventoForm(request.POST, request.FILES, instance=even_organizer)
        if modelform.is_valid():
            modelform.save()
            return redirect("panel")

class DetalleEventView(View):
    def get(self,request, pk):
        evento = get_object_or_404(Event, pk=pk)
        return render(request, "events/detalle_evento.html",{'evento':evento})  


class EditarEventView(View):
    def get(self,request,pk):
        evento = get_object_or_404(Event, pk=pk)
        modelform = EventoForm(instance=evento)
        return render(request, "events/editar_evento.html",{'form':modelform,'evento':evento})
    
    def post(self,request, pk):
        evento = get_object_or_404(Event, pk=pk)
        modelform = EventoForm(request.POST, instance=evento)
        if modelform.is_valid():
            modelform.save()
            return redirect("panel")
class EliminarEventView(View):
    def get(self,request,pk):
        evento = get_object_or_404(Event, pk=pk)
        return render(request, "events/eliminar_evento.html",{'evento':evento})
    
    def post(self,request, pk):
        evento = get_object_or_404(Event, pk=pk)
        evento.delete()
        return redirect("panel")
        
    