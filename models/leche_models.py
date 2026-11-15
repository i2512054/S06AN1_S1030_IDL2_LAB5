from spyne import ComplexModel, Unicode, Float, Boolean

class LoteLecheInput(ComplexModel):
	__namespace__ = "gloria.erp.acopio"
	id_ganadero = Unicode(min_len=1, nullable=False)
	litros_ingresados = Float(nullable=False)
	prueba_acidez = Float(nullable=False)
	
class ResultadoRecepcionOutput(ComplexModel):
	__namespace__ = "gloria.erp.acopio"
	id_transaccion = Unicode
	estado_registrado = Unicode
	control_calidad_aprobado = Boolean
	observaciones = Unicode