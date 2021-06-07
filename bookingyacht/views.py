import datetime

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import LoginRequiredMixin

from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import View
from django.views.generic import CreateView, UpdateView

from bookingyacht.forms import YachtModelForm
from bookingyacht.models import Yacht, Marina, CharterCompany, YachtReservation


class IndexView(View):

    def get(self, request):
        return render(request, 'base.html')


class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'registration/login.html'


class YachtView(View):

    def get(self, request):
        return render(request, 'yacht_view.html', {"yacht": Yacht.objects.all()})


class YachtViewDetail(View):
    def get(self, request, id):
        yacht = Yacht.objects.get(pk=id)
        return render(request, 'YachtDetails.html', {'yacht': yacht})


class UpdateYacht(LoginRequiredMixin, UpdateView):
    model = Yacht
    template_name = 'forms.html'
    fields = "__all__"


class DeleteYacht(LoginRequiredMixin, View):

    def get(self, request, id):
        yacht = Yacht.objects.get(id=id)
        yacht.delete()
        return redirect("view_yacht")


class AddYacht(LoginRequiredMixin, CreateView):
    form_class = YachtModelForm
    template_name = 'forms.html'
    success_url = reverse_lazy('view_yacht')


# def get_context_data(self, **kwargs):
#    data = super().get_context_data(**kwargs)
#   data['yacht'] = Yacht.objects.all()
#  return data


class MarinaView(View):

    def get(self, request):
        return render(request, 'marina_view.html', {"marina": Marina.objects.all()})


class MarinaViewDetail(View):
    def get(self, request, id):
        marina = Marina.objects.get(pk=id)
        return render(request, 'MarinaDetails.html', {'marina': marina})


class CharterCompanyView(View):

    def get(self, request):
        return render(request, 'CharterCompany_view.html', {"charter": CharterCompany.objects.all()})


class CharterCompanyViewDetail(View):
    def get(self, request, id):
        charter = CharterCompany.objects.get(pk=id)

        return render(request, ' CharterCompanyDetails.html', {'charter': charter})


class ReservationView(LoginRequiredMixin, View):
    def get(self, request, id):
        yacht = Yacht.objects.get(id=id)
        reservations = yacht.yachtreservation_set.filter(date__gte=str(datetime.date.today())).order_by('date')
        return render(request, "reservation.html", context={"yacht": yacht, "reservations": reservations})

    def post(self, request, id):
        yacht = Yacht.objects.get(id=id)
        date = request.POST.get("reservation-date")
        user = request.user
        reservations = yacht.yachtreservation_set.filter(date__gte=str(datetime.date.today())).order_by('date')

        if date is "":
            return render(request, "reservation.html",
                          context={"yacht": yacht,
                                   "reservations": reservations,
                                   "error": "podaj date!!"})

        if YachtReservation.objects.filter(yacht=yacht, date=date):
            return render(request, "reservation.html",
                          context={"yacht": yacht,
                                   "reservations": reservations,
                                   "error": "yacht jest już zarezerwowany!"})
        if date < str(datetime.date.today()):
            return render(request, "reservation.html",

                          context={"yacht": yacht,
                                   "reservations": reservations,
                                   "error": "Data jest z przeszłości!"})

        YachtReservation.objects.create(yacht=yacht, date=date, user=user)
        return redirect("view_yacht")


class Contact(View):
    def get(self, request):
        return render(request, 'contact.html')
