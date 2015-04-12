from django.conf.urls import url

from crowdpact.apps.account.api import AccountDetailsView
from crowdpact.apps.account.views import AccountLoginView, AccountSignupView

urlpatterns = [
    url(r'^api/details/(?P<id>.+)/?$', AccountDetailsView.as_view(), name='account.api.details'),
    url(r'^login/?$', AccountLoginView.as_view(), name='account.login'),
    url(r'^signup/?$', AccountSignupView.as_view(), name='account.signup')
]
