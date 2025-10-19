from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from .models import Item
from .forms import ItemForm

class ItemListView(ListView):
    model = Item
    paginate_by = 20
    template_name = "stock/item_list.html"
    context_object_name = "items"

    def get_queryset(self):
        qs = Item.objects.order_by("name")
        q = self.request.GET.get("q")
        if q:
            qs = qs.filter(Q(name__icontains=q) | Q(sku__icontains=q) | Q(location__icontains=q))
        active = self.request.GET.get("active")
        if active == "1":
            qs = qs.filter(is_active=True)
        elif active == "0":
            qs = qs.filter(is_active=False)
        return qs

class ItemCreateView(CreateView):
    model = Item
    form_class = ItemForm
    template_name = "stock/item_form.html"
    success_url = reverse_lazy("item-list")

class ItemUpdateView(UpdateView):
    model = Item
    form_class = ItemForm
    template_name = "stock/item_form.html"
    success_url = reverse_lazy("item-list")

class ItemDeleteView(DeleteView):
    model = Item
    template_name = "stock/item_confirm_delete.html"
    success_url = reverse_lazy("item-list")