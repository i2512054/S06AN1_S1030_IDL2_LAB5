from zeep import Client

WSDL_URL = "http://127.0.0.1:8976/?wsdl"

def probar_conexion_base():
	print("[Cliente Zeep] Conectando al contrato WSDL...")
	client = Client(WSDL_URL)
	
	# Invocación del método remoto de prueba
	respuesta = client.service.saludar_centro_acopio(nombre_centro="Acopio Majes - Arequipa")
	print("\n--- Respuesta del Servidor SOAP ---")
	print(respuesta)
	
if __name__ == "__main__":
	probar_conexion_base()