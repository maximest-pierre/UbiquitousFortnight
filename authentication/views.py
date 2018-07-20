from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views.generic.edit import CreateView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UserCreateView(CreateView):
    model = User

    template_name = 'authentication/create_user.html'
    form_class = UserCreationForm

    def post(self, request, *args, **kwargs):
        form_class = self.get_form_class()
        form = self.get_form(form_class)

        user = User()
        if form.is_valid():

            user.username = form.cleaned_data['username']
            user.password = form.cleaned_data['password2']
            user.set_password(user.password)
            user.save()

            return HttpResponseRedirect(reverse("authentication:login"))

        else:
            return render(request, self.template_name, {'form': form})

