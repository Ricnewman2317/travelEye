from django.contrib.auth import authenticate,login,logout,get_user_model # Required for Authentication System. RN.
from django.contrib.auth.decorators import login_required  # Enforce Login. RN.
from django.shortcuts import get_object_or_404,render,redirect,render_to_response
from django.core.urlresolvers import reverse
from django.utils.decorators import method_decorator

from django.forms import ValidationError
from django.views.generic import TemplateView
from django.views.generic.base import View
from django.views.generic.edit import FormView,UpdateView,CreateView,DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView

from . import forms

from rest_framework import generics
from guides.models import PointsOfInterest, Streets
from guides.serializers import PointsOfInterestSerializer, StreetsSerializer


# Create your views here.
def index_page(request):
    return render(request, "guides/index.html")


class PointsOfInterestList(generics.ListCreateAPIView):
    queryset = PointsOfInterest.objects.all()
    serializer_class = PointsOfInterestSerializer


class PointsOfInterestDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset = PointsOfInterest.objects.all()
     serializer_class = PointsOfInterestSerializer


class StreetsList(generics.ListCreateAPIView):
     queryset = Streets.objects.all()
     serializer_class = StreetsSerializer


class StreetsDetail(generics.RetrieveUpdateDestroyAPIView):
     queryset = Streets.objects.all()
     serializer_class = StreetsSerializer


@login_required
def logout_view(request):
    logout(request)
    return redirect(reverse('guides:login'))

@login_required
def landing(request):
    return render(request, 'guides/index.html')

def login_view(request):
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)

            if user:
                if user.is_active:
                    login(request, user)
                    return redirect(reverse('guides/index.html'))

                else:
                    form.add_error(None, ValidationError(
                        "Your account is inactive."
                    ))

            else:
                form.add_error(None, ValidationError(
                    "Invalid Username and/or Password"
                ))

    else:
        form = forms.LoginForm()

    return render(request, 'guides/index.html', {'form': form})


