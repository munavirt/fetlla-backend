from django.urls import path
from .views import LoginView,DetailBatchAV,ListBatchAV,ListStudent,StudentDetails


urlpatterns = [
    path('login/',LoginView.as_view(),name='login-view'),
    
    path('batch/',ListBatchAV.as_view(),name='batch-list'),
    # path('batch/create/',CreateBatchAv.as_view(),name="create-batch"),
    path('batch/<int:pk>/',DetailBatchAV.as_view(),name='update-batch'),
    
    path('students/',ListStudent.as_view(),name='list-student'),
    path('students/<int:pk>/',StudentDetails.as_view(),name='detail-student')

]