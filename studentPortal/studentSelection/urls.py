from .views import register , mylogin , home,profile,entekhabVahed,mylogout,choiceCourse , deleteCourse ,menu ,amozesh,setgrades,hometeacher,registerCourse
from django.urls import path
from studentPortal import settings
from django.contrib.staticfiles.urls import static ,staticfiles_urlpatterns

urlpatterns = [
    path('register/',register.as_view() , name='register'),
    path('login/',mylogin.as_view() , name='mylogin'),
    path('home/',home.as_view() , name='home'),
    path('Home/',home.as_view() , name='home'),
    path('profile/',profile.as_view() , name='profile'),
    path('entekhabVahed/',entekhabVahed.as_view() , name='entekhabVahed'),
    path('logout/',mylogout , name='mylogout'),
    path('choiceCourse/',choiceCourse , name='choiceCourse'),
    path('deleteCourse/',deleteCourse , name='deleteCourse'),
    path('menu/',menu , name='menu'),
    path('hometeacher/',hometeacher.as_view() , name='hometeacher'),
    path('setgrades/',setgrades.as_view() , name='setgrades'),
    path('amozesh/',amozesh.as_view() , name='amozesh'),
    path('registerCourse/',registerCourse.as_view() , name='registerCourse'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)