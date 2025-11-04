from jsonrpcserver import Service

service = Service()

@service.method
def add(a, b):
    return a + b