from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect

# Create your views here.
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView

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


class UpdateYacht(View):
    def get(self, request, id):
        yacht = Yacht.objects.get(pk=id)
        form = YachtModelForm(instance=yacht)
        return render(request, 'forms.html', {"form": form})

    def post(self, request, id):
        yacht = Yacht.objects.get(pk=id)
        form = YachtModelForm(request.POST, instance=yacht)
        if form.is_valid():
            yacht = form.save()
        return redirect("view_yacht")


class DeleteYacht(View):

    def get(self, request, id):
        yacht = Yacht.objects.get(id=id)
        yacht.delete()
        return redirect("view_yacht")


class AddYacht(View):

    def get(self, request):
        form = YachtModelForm()
        return render(request, 'forms.html', {'form': form})

    def post(self, request):
        form = YachtModelForm(request.POST)
        if form.is_valid():
            yacht = Yacht()
            yacht.name = form.cleaned_data.get('name')
            yacht.year = form.cleaned_data.get('year')
            yacht.length = form.cleaned_data.get('length')
            yacht.max_person = form.cleaned_data.get('max_person')
            yacht.price = form.cleaned_data.get('price')
            yacht.yacht_category = form.cleaned_data.get('yacht_category')
            yacht.charter_company = form.cleaned_data.get('charter_company')
            yacht.save()
            return redirect('view_yacht')
        return render(request, 'forms.html', {'form': form})
