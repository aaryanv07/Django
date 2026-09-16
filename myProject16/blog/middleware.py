import datetime
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin # Helper class for backward compatibility. Helps to write middleware code shorter.

class SimpleLogMiddleware(MiddlewareMixin):
    def process_request(self,request):
        print(f"[LOG {datetime.datetime.now()}] Request url : {request.path}")
    def process_response(self,request,response):
        print(f'[Response {datetime.datetime.now()} Status] : {response.status_code}')
        return response

class BlockIPMiddleware(MiddlewareMixin):
    BLOCKED_IPS = ['127.0.0.1', '[IP_ADDRESS]', '[IP_ADDRESS]']

    def process_request(self, request):
        remote_address = request.META.get('REMOTE_ADDR')

        if remote_address in self.BLOCKED_IPS:
            return HttpResponse("<h1>Access Denied</h1><p>Your IP has been blocked.</p>")

