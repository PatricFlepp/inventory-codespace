from django.contrib import admin
from django.urls import path
from stock.views import ItemListView, ItemCreateView, ItemUpdateView, ItemDeleteView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", ItemListView.as_view(), name="item-list"),
    path("items/new/", ItemCreateView.as_view(), name="item-create"),
    path("items/<int:pk>/edit/", ItemUpdateView.as_view(), name="item-edit"),
    path("items/<int:pk>/delete/", ItemDeleteView.as_view(), name="item-delete"),
]