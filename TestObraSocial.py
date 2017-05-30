#!/usr/bin/env python3
from Prestador import*
from Liquidacion import*	
from Consumos import*	

if __name__ == '__main__':
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
	
