from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView, CreateView, ListView, DetailView, UpdateView, DeleteView
from . import models
from serial.tools.list_ports import comports


# Create your views here.
class HomeView(TemplateView):
    template_name = 'app/home.html'


def list_ports(request):
    ports = []
    for n, (port, desc, hid) in enumerate(sorted(comports()), 1):
        # sys.stderr.write('{:2}: {:20} {!r}\n'.format(n, port, desc))
        if 'NULL' not in port:
            ports.append(port)

    context = {'all_ports': ports}
    return render(request, 'app/list.html', context=context)
