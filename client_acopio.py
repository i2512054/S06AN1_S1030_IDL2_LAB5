from zeep import Client
WSDL_URL = "http://127.0.0.1:8976/?wsdl"
def enviar_lotes_acopio():
	client = Client(WSDL_URL)
	
	# Lotes de prueba a enviar desde el Centro de Acopio
	lotes_prueba = [
		{"id_ganadero": "GAN-101", "litros_ingresados": 500.0, "prueba_acidez": 15.5}, # Óptimo
		{"id_ganadero": "GAN-102", "litros_ingresados": 350.0, "prueba_acidez": 11.8}, # Acidez Baja
		{"id_ganadero": "GAN-103", "litros_ingresados": 1200.0, "prueba_acidez": 19.5} # Acidez Alta
	]
	
	print("ENVIANDO LOTES DE LECHE AL ERP GLORIA (SOAP/ZEEP)")
	
	for i, datos in enumerate(lotes_prueba, start=1):
		print(f"--- Procesando Lote #{i} (Ganadero: {datos['id_ganadero']}) ---")
		
		# Zeep instancia automáticamente el tipo complejo definido en Spyne
		lote_type = client.get_type('ns0:LoteLecheInput')
		lote_obj = lote_type(
			id_ganadero=datos["id_ganadero"],
			litros_ingresados=datos["litros_ingresados"],
			prueba_acidez=datos["prueba_acidez"]
		)
		
		# LLamada remota RPC
		resultado = client.service.registrar_lote_leche(lote=lote_obj)
		
		# Lectura de respuesta SOAP mapeada
		print(f"ID Transacción ERP	:	{resultado.id_transaccion}")
		print(f"Estado Registro		:	{resultado.estado_registro}")
		print(f"Control Calidad		:	{'APROBADO' if resultado.control_calidad_aprobado else 'RECHAZADO'}")
		print(f"Observaciones		:	{resultado.observaciones}")
		
	if __name__ == "__main__":
		enviar_lotes_acopio()