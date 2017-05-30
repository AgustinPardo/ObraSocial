class Prestador:
	def __init__(self,name,prestacionBasica,precioKm,basicoMinimo):
		self.prestacionBasica = prestacionBasica
		self.precioKm = precioKm
		self.basicoMinimo=basicoMinimo
		self.listaConsumos=[]
		self.name=name
			
	def consumo(self,consu):	
		consu.prestacionBasica = self.prestacionBasica	
		if consu.tipo() == "Domiciliario":		
			consu.precioKm=self.precioKm
		return(self.listaConsumos.append(consu))
	
	def liquidar(self,mesLiquidar):
		sumaTotal=0
		for consumo in self.listaConsumos:
			if consumo.mes ==mesLiquidar:	
				sumaTotal=sumaTotal + consumo.valor()

		return(sumaTotal+self.basicoMinimo)
		
		
