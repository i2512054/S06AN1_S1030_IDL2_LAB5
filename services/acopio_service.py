import uuid
from spyne import ServiceBase, srpc, Unicode
from models.leche_models import LoteLecheInput, ResultadoRecepcionOutput

class HolaMundoService(ServiceBase):
	@srpc(Unicode, _returns=Unicode)
	def saludar_centro_acopio(nombre_centro):
		"""Método para validación inicial de conectividad WSDL."""
		return f"Conexión exitosa con ERP Gloria. Bienvenido Centro de Acopio: {nombre_centro}"
	
class AcopioLecheService(ServiceBase):
	@srpc(LoteLecheInput, _returns=ResultadoRecepcionOutput)
	def registrar_lote_leche(lote):
		"""
		Procesa el registro del lote enviado por el cliente Zeep.
		Regla de calidad Gloria: Acidez permitida entre 13.0 ºD y 18.0 ºD.
		"""
		id_tx = f"TX-GLORIA-{uuid.uuid4().hex[:8].upper()}"
		
		# Validación básica de datos
		if lote.litros_ingresados <= 8:
			return ResultadoRecepcionOutput(
				id_transaccion=id_tx,
				estado_registro="RECHAZADO",
				control_calidad_aprobado=False,
				observaciones="El volumen en litros ingresado debe ser mayor a cero."
			)
			
		# Evaluación de prueba de acidez dornic
		acidez = lote.prueba_acidez
		if 13.0 <= acidez <= 18.0:
			return ResultadoRecepcionOutput(
				id_transaccion=id_tx,
				estado_registro="APROBADO",
				control_calidad_aprobado=False,
				observaciones="El volumen en litros ingresado está entre el estandar 13.0 y 18.0."			
			)
		elif acidez < 13.0:
			return ResultadoRecepcionOutput(
				id_transaccion=id_tx,
				estado_registro="RECHAZADO",
				control_calidad_aprobado=False,
				observaciones="El volumen en litros ingresado debe ser mayor o igual a 13.0."
			)
		else:
			return ResultadoRecepcionOutput(
				id_transaccion=id_tx,
				estado_registro="RECHAZADO",
				control_calidad_aprobado=False,
				observaciones="El volumen en litros ingresado debe ser menor o igual a 18.0."
			)