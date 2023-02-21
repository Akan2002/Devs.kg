from rest_framework.routers import DefaultRouter as DR
from apps.company.views import(
    companyView,
)

router=DR()

router.register('company', companyView, basename= 'company')

urlpatterns=[]
urlpatterns += router.urls