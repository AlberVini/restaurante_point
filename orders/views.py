from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse
from django.views.generic import CreateView

from cart.cart import Cart

from .forms import OrderCreateForm
from .models import Item, Order
from users.models import User


class OrderCreateView(CreateView):
    model = Order
    form_class = OrderCreateForm

    def form_valid(self, form):
        cart = Cart(self.request)

        user = get_object_or_404(User, username=self.request.user)

        if cart:
            #new_form = form.save(commit=False)
            #new_form.user = user
            order = form.save(commit=False)
            order.user = user
            order.save()

            for item in cart:
                Item.objects.create(
                    order=order,
                    product=item["product"],
                    price=item["price"],
                    quantity=item["quantity"],
                )
            cart.clear()
            self.request.session["order_id"] = order.id
            return render(self.request, "orders/order_created.html", {"order":order})
        return redirect(reverse("pages:home"))

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cart"] = Cart(self.request)
        return context