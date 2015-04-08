from django.http import HttpResponse
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

try:
    from django.views.generic import View
except ImportError:
    pass
else:

    class RpcServerView(View):
        server_instance = None

        def __init__(self, *args, **kw):
            super(RpcServerView, self).__init__(*args, **kw)
            self._rpc_server = self.server_instance

        def post(self, request):
            result = self._rpc_server.handle_http_request(request)
            return HttpResponse(result)

        @method_decorator(csrf_exempt)
        def dispatch(self, *args, **kwargs):
            return super(RpcServerView, self).dispatch(*args, **kwargs)


def csrf_serve(request, service):
    result = service.handle_http_request(request)
    return HttpResponse(result)


@csrf_exempt
def serve(request, service):
    return csrf_serve(request, service)

