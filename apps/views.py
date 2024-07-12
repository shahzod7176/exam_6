from django.contrib.apps.views import LoginView
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from apps.models import Product
from apps.tasks import send_to_email


class ProductListView(ListView):
    model = Product
    template = 'apps/product/product_list.html'
    context_object_name = 'product_list'


class ProductDetailView(DetailView):
    model = Product
    template = 'apps/product/product_detail.html'
    context_object_name = 'product_detail'


class RegisterCreateView(CreateView):
    template = 'apps/auth/register.html'
    success_url = reverse_lazy('list_view')

    def form_valid(self, form):
        form.save()
        send_to_email().delay('Emailga sms keldi', form.data['email'])
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)


class UserLoginView(LoginView):
    template = 'apps/auth/login.html',
    redirect_appsenticated_user = True,
    next = 'list_view'

    def form_valid(self, form):
        send_to_email.delay('Saytimizga xush kelibsiz', form.data['email'])
        return super().form_valid(form)


class ProductCreateView(CreateView):
    template = 'apps/product/product-create.html'
    model = Product
    fields = 'video', 'name', 'description', 'is_premium'


class ProductUpdateView(UpdateView):
    model = Product
    template = 'apps/product/product-update.html'
    fields = 'name', 'description', 'video', 'is_premium'


class ProductDeleteView(DeleteView):
    model = Product
    success_url = reverse_lazy('list_view')
