class Liquidacion:
	def __init__(self):		
		self.listaPrestadores=[]

	def asociarPrestador(self,presta):
		return(self.listaPrestadores.append(presta))
		
	def liquidacionMensual(self,mes):
		print("Liquidacion mes: "+str(mes)+"\n")
		sumaMontoFinal=0
		for presta in self.listaPrestadores:
			print(presta.name)
			print("Consumo Valor Hora Dia")						
			for consumo in presta.listaConsumos:
				
				if mes == consumo.mes:			
					print(str(consumo.tipo())+" "+ str(consumo.valor())+ " "+ str(consumo.hora)+" "+ str(consumo.dia))
					
			print("Basico minimo: "+str(presta.basicoMinimo))
			print("Monto Final Prestador: "+str(presta.liquidar(mes))+"\n")			
			sumaMontoFinal=sumaMontoFinal+presta.liquidar(mes)

		print("Monto Final mes"+ "    |" +str(sumaMontoFinal))	
		print("""----------------------------------------------""")	


