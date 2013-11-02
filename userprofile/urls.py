from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
	url(r'^user/(?P<username>.+)/$', 'userprofile.views.view_member'),
	url(r'^profile/$', 'userprofile.views.user_profile'),
	url(r'^admin_member/$', 'userprofile.views.admin_member'),
	url(r'^list/$', 'userprofile.views.view_members'),
	
)