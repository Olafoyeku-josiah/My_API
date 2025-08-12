from django.urls import path
from . import views


urlpatterns=[
    path("blogposts/", views.BlogpostListCreate.as_view(),name="blogpost-view-create")
]