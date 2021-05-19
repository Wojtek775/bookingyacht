from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from bookingyacht.forms import YachtModelForm
from bookingyacht.models import Yacht


class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/login.html'


class YachtPersonView(View):

    def get(self, request):
        return render(request, 'yacht_view.html', {"yacht": Yacht.objects.all()})


class YachtViewDetail(View):
    def get(self, request, id):
        yacht = Yacht.objects.get(pk=id)
        return render(request, 'YachtDetails.html', {'yacht': yacht})


class UpdateYacht(UpdateView):
    model = Yacht
    template_name = 'forms.html'
    fields = "__all__"


class DeleteYacht(View):

    def get(self, request, id):
        yacht = Yacht.objects.get(id=id)
        yacht.delete()
        return redirect("view_yacht")


class AddYacht(CreateView):
    model = Yacht
    template_name = 'forms.html'
    success_url = reverse_lazy('view_yacht')
    fields = "__all__"

    def get_context_data(self, **kwargs):
        data = super().get_context_data(**kwargs)
        data['yacht'] = Yacht.objects.all()
        return data


