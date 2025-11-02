from django.urls import path
from . import views
app_name='Blogs'
urlpatterns = [
    path("MyScribe/",views.landing_page,name="landing"),
    path("", views.home_page, name="home"),
    path("<int:id>/",views.details_page,name="details"),
    path("create/",views.create_blog, name='create'),
    path("update/",views.update_page,name='update'),
    path("edit/<int:id>/",views.edit_blog,name='edit'),
    path("delete/",views.delete_blog,name='delete'),
    path("trash/<int:id>",views.trash_blog,name="trash"),
]
