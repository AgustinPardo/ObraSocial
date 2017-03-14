#!/usr/bin/env python3
# Monto fijo es el mimso para todas los prestadores
class Prestador:
	def __init__(self,name,prestacionBasica,precioKm,montoFijo):
		self.prestacionBasica = prestacionBasica
		self.precioKm = precioKm
		self.montoFijo=montoFijo
		self.listaConsumos=[]
		self.name=name
			
	def consumo(self,consu):
		return(self.listaConsumos.append(consu))
	
	def liquidar(self,mesLiquidar):
		sumaTotal=0
		for consumo in self.listaConsumos:
			if consumo.mes ==mesLiquidar:	
				sumaTotal=sumaTotal + consumo.valor()

		return(sumaTotal+self.montoFijo)	
		
class Liquidacion:
	def __init__(self):		
		self.listaPrestadores=[]

	def asociarPrestador(self,presta):
		return(self.listaPrestadores.append(presta))
		
	def liquidacionMensual(self,mes):
		print("Liquidacion mes: "+str(mes))
		print("Consumo Valor Hora Dia Mes")
		sumaMontoFinal=0
		for presta in self.listaPrestadores:							
			for consumo in presta.listaConsumos:
				if mes == consumo.mes:			
					print(str(consumo.tipo())+" "+ str(consumo.valor())+ " "+ str(consumo.hora)+" "+ str(consumo.dia)+" "+ str(consumo.mes))
		
			print(presta.name+"    |"+str(presta.liquidar(mes))+"\n")
			sumaMontoFinal=sumaMontoFinal+presta.liquidar(mes)
		print("MontoFinal"+ "    |" +str(sumaMontoFinal))	
		print("""----------------------------------------------""")			
			
class ConsumoBasico:	
	def __init__(self,hora,dia,mes,prestacionBasica):
		self.hora=hora
		self.dia=dia
		self.mes=mes
		self.prestacionBasica = prestacionBasica		
		
	def tipo(self):
		return("Basico")	
	
	def valorBasico(self):		
		Monto=0
		if self.dia != "Domingo" or self.dia != "Sabado":
			if 8<self.hora<20 :
				Monto= self.prestacionBasica + self.prestacionBasica*0.35
			else:
				Monto= self.prestacionBasica + self.prestacionBasica*0.5
		else:
			Monto= self.prestacionBasica + self.prestacionBasica*0.5
				
		return(Monto)
		
	def valor(self):				
		return self.valorBasico()

class ConsumoDomiciliario(ConsumoBasico):
	def __init__(self,hora,dia,mes,kms,prestacionBasica,precioKm):
		self.hora=hora
		self.dia=dia
		self.mes=mes
		self.prestacionBasica = prestacionBasica
		self.kms=kms
		self.precioKm=precioKm		
		
	def tipo(self):
		return("Domiciliario")	
		
	def valor(self):
		valorBasico  = self.valorBasico()				
		Monto=valorBasico+(valorBasico*0.25)+(self.kms*self.precioKm)
		return(Monto)
		
# Ingreso de datos
Galeno=Prestador("Galeno",1000,5,100)
A=ConsumoBasico(5,"Lunes",1,Galeno.prestacionBasica)
B=ConsumoDomiciliario(10,"Martes",1,20,Galeno.prestacionBasica,Galeno.precioKm)
C=ConsumoBasico(16,"Sabado",2,Galeno.prestacionBasica)
Galeno.consumo(A)
Galeno.consumo(B)
Galeno.consumo(C)

OSS=Prestador("OSS",1500,75,200)
D=ConsumoBasico(5,"Lunes",1,OSS.prestacionBasica)
E=ConsumoDomiciliario(10,"Jueves",2,10,OSS.prestacionBasica,OSS.precioKm)
F=ConsumoDomiciliario(18,"Domingo",2,50,OSS.prestacionBasica,OSS.precioKm)
OSS.consumo(D)
OSS.consumo(E)
OSS.consumo(F)

Salida=Liquidacion()
Salida.asociarPrestador(Galeno)
Salida.asociarPrestador(OSS)
Salida.liquidacionMensual(1)
Salida.liquidacionMensual(2)
