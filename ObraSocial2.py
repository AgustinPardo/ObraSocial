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



# Ingreso de datos:
# Prestador(Nombre,Prestacion basica,Precio por km, Basico minimo)
# ConsumoBasico(Hora,Dia,Mes,Prestacion basica)
# ConsumoDomiciliario(Hora,Dia,Mes,Prestacion basica,Precio por km)
Prestador1=Prestador("Prestador1",1000,50,100)
Prestador1.consumo(ConsumoBasico(14,"Lunes",1))
Prestador1.consumo(ConsumoDomiciliario(10,"Martes",1,20))
Prestador1.consumo(ConsumoBasico(16,"Sabado",2))

Prestador2=Prestador("Prestador2",1500,75,200)
Prestador2.consumo(ConsumoBasico(5,"Lunes",1))
Prestador2.consumo(ConsumoDomiciliario(10,"Jueves",2,10))
Prestador2.consumo(ConsumoDomiciliario(18,"Domingo",2,12))
Prestador2.consumo(ConsumoDomiciliario(9,"Miercoles",1,20))
Prestador2.consumo(ConsumoDomiciliario(20,"Jueves",3,15))

Salida=Liquidacion()
Salida.asociarPrestador(Prestador1)
Salida.asociarPrestador(Prestador2)
Salida.liquidacionMensual(1)
Salida.liquidacionMensual(2)
Salida.liquidacionMensual(3)
	
