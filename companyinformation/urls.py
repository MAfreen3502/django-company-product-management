from  django.urls import path
from .views import CompanyDetails,Products,companyInfo,AddNewCompany,editCompany,RemoveCompany
from .views import emiCalculator

urlpatterns=[
   path('', CompanyDetails.as_view(), name='company_list'),
    path('products/', Products.as_view(), name='product_list'),
    path('<int:pk>/', companyInfo.as_view(), name='company_detail'),
    path('create',AddNewCompany.as_view(),name='create'),
    path('edit/<int:pk>/',editCompany.as_view(),name='edit'),
    path('delete/<int:pk>/',RemoveCompany.as_view(),name='delete'),
    path('emi/<int:pk>/', emiCalculator, name='emi_calci'),
    


    
]