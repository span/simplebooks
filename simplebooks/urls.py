from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'simplebooksform.views.home', name='home'),
    url(r'^add-verification$', 'simplebooksform.views.add_verification', name='add_verification'),
    url(r'^view-verifications$', 'simplebooksform.views.view_verifications', name='view_verifications'),
    url(r'^result$', 'simplebooksform.views.result', name='result'),
    url(r'^api/get_verifications/', 'simplebooksform.views.get_verifications', name='get_verifications'),
    
    # url(r'^simplebooks/', include('simplebooks.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
