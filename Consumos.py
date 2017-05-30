class ConsumoBasico:	
	def __init__(self,hora,dia,mes):
		self.hora=hora
		self.dia=dia
		self.mes=mes
		self.prestacionBasica = None		
	
	def tipo(self):
		return("Basico")	
	
	def valorBasico(self):		
		Monto=0
		desde=8
		hasta=20
		fueraHora=0.35
		finde=0.5
		if self.dia != "Domingo" and self.dia != "Sabado":
			if desde<self.hora<hasta :
				Monto= self.prestacionBasica
			else:
				Monto= self.prestacionBasica + self.prestacionBasica*fueraHora
		else:
			Monto= self.prestacionBasica + self.prestacionBasica*finde
				
		return(Monto)
		
	def valor(self):				
		return self.valorBasico()

class ConsumoDomiciliario(ConsumoBasico):
	def __init__(self,hora,dia,mes,kms):
		self.hora=hora
		self.dia=dia
		self.mes=mes
		self.kms=kms
		self.prestacionBasica = None
		self.precioKm = None		
		
	def tipo(self):
		return("Domiciliario")	
		
	def valor(self):
		valorBasico  = self.valorBasico()				
		Monto=valorBasico+(valorBasico*0.25)+(self.kms*self.precioKm)
		return(Monto)
		

