import logging
from wsgiref.simple_server import make_server
from spyne import Application #, Wsdl11, Soap11
from spyne.interface.wsdl import Wsdl11
from spyne.protocol.soap import Soap11
from spyne.server.wsgi import WsgiApplication
from services.acopio_service import HolaMundoService, AcopioLecheService

# Configuración de Logging
logging.basicConfig(level=logging.INFO)

# Definicion de la Aplicación Spyne con múltiples servicios
application = Application(
	[HolaMundoService, AcopioLecheService],
	tns='gloria.erp.acopio',
	in_protocol=Soap11(validator='lxml'),
	out_protocol=Soap11()
)

wsgi_app = WsgiApplication(application)

if __name__ == '__main__':
	HOST = '127.0.0.1'
	PORT = 8976
	
print(f"===================================================================================")
print(f"WSDL disponible en: http://{HOST}:{PORT}/?wsdl")
print(f"===================================================================================")
server = make_server(HOST, PORT, wsgi_app)
server.serve_forever()