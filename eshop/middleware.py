import re
from django.http import Http404
from django.core.exceptions import PermissionDenied
from django.conf import settings


class IsIPAdressAllowedAllowed:

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):

        client_IP_adress = request.META.get('REMOTE_ADDR')
        allowed_IP_adresses = settings.IS_IPADRESS_ALLOWED_MIDDLEWARE['ALLOWED_IP_ADDRESSES']

        if not client_IP_adress in allowed_IP_adresses:
            raise PermissionDenied

        response = self.get_response(request)
        response['X-IP-FILTER'] = 'Allowed IP Adress'
        return response


SELLER_URLS = []

if hasattr(settings, 'SELLER_URLS'):
    SELLER_URLS += [re.compile(url) for url in settings.SELLER_URLS]


class IsSellerMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        return response

    def process_view(self, request, view_func, view_args, view_kwargs):
        assert hasattr(request, 'user')
        user = request.user
        path = request.path_info.lstrip('/')
        print(path)
        print(SELLER_URLS)
        if not (request.user.groups.filter(name="seller").exists()):
            if any(url.match(path) for url in SELLER_URLS):
                raise Http404("Not found")
