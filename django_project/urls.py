from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from django.conf import settings
admin.autodiscover()
urlpatterns = [
    # Examples:
    # url(r'^$', 'html.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'django_project.views.index', name='index'),
    url(r'^about-ssuns/', 'django_project.views.aboutssuns', name='about'),
    url(r'^about-irsam/', 'django_project.views.aboutirsam', name='about'),
    url(r'^about-montreal/', 'django_project.views.aboutmontreal', name='about'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^form/$', 'RegistrationForm.views.registration', name='registration'),
    # url(r'^countryassignment/$', 'RegistrationForm.views.CountryAssignmentView', name='CountryAssignment'),
    # url(r'^profile/$', 'RegistrationForm.views.profile', name='profile'),
    # url(r'^DelegateInput/$', 'RegistrationForm.views.DelegateInputView', name='DelegateInput'),
    # url(r'^positionpaper/$', 'RegistrationForm.views.positionpaper', name='positionpaper'),
    url(r'^team/', 'django_project.views.team', name='team'),
    url(r'^reg/$', 'django_project.views.reg', name='reg'),
    # url(r'^positionpaperReceived/$', 'django_project.views.positionpaperReceived', name='positionpaperReceived'),
    # url(r'^staff/', 'html.views.staff', name='staff'),
    # url(r'^committees/', 'django_project.views.committees', name='committees'),
    url(r'^contact/', 'django_project.views.contact', name='contact'),
    url(r'^sponsors/', 'django_project.views.sponsors', name='sponsors'),
    # url(r'^comingsoon/', 'django_project.views.comingsoon', name='comingsoon'),
    # url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^ga/', 'django_project.views.ga', name='ga'),
    url(r'^sa/', 'django_project.views.sa', name='sa'),
    url(r'^travel/', 'django_project.views.travel', name='travel'),
    url(r'^crisis/', 'django_project.views.crisis', name='crisis'),
    url(r'^faq/', 'django_project.views.faq', name='faq'),
    # url(r'^schedule/', 'django_project.views.schedule', name='schedule'),
    # url(r'^thankyou/', 'html.views.thankyou', name='thankyou'),
    # url(r'^faq/index', 'html.views.faq', name='faq'),






] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
	urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
