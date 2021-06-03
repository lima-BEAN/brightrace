from django.urls import path

from blog import views

app_name='blog'

#URLPatterns for function based views
urlpatterns = [
    path('', views.BlogList.as_view(), name='blog_list'),
    path('<int:pk>/', views.BlogDetail.as_view(), name='blog_detail'),
    path('new/', views.BlogCreate.as_view(), name='blog_new'),
    path('<int:pk>/update/', views.BlogUpdate.as_view(), name='blog_update'),
]
