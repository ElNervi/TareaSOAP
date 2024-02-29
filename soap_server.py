from http.server import HTTPServer
from pysimplesoap.server import SoapDispatcher, SOAPHandler

def SumaDosNumeros(a,b):

    return "la suma de ambos es: ",a+b, "<-- resultado"

dispatcher = SoapDispatcher(
    "soap_server",
    location="http://localhost:8000/",
    action="http://localhost:8000/",
    namespace="http://localhost:8000/",
    trace=True,
    ns=True,
)

dispatcher.register_function(
    "SumaDosNumeros",
    SumaDosNumeros,
    returns={"suma: ": str},
    args={"suma": str},
)

server=HTTPServer(("0.0.0.0", 8000),SOAPHandler)
server.dispatcher=dispatcher
print("servidor soap iniciado en http://localhost:8000/")
server.serve_forever()