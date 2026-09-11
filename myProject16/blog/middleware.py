import datetime
from django.http import HttpResponse
from django.utils.deprecation import MiddlewareMixin # Helper class for backward compatibility. Helps to write middleware code shorter.

class SimpleLogMiddleware(MiddlewareMixin):
    def process_request(self,request):
        print(f"[LOG {datetime.datetime.now()}] Request url : {request.path}")
    def process_response(self,request,response):
        print(f'[Response {datetime.datetime.now()} Status] : {response.status_code}')
        return response


