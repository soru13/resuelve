#!/usr/bin/env python
#-*-coding:utf-8-*-
from flask import Flask,url_for,request
from flask import render_template #para renderizar templates
import datetime #para el manejo de fechas
from datetime import datetime,timedelta,date
import calendar
import requests  #para hacer la peticion a una URL
from dateutil import relativedelta
app = Flask(__name__)


#solo cuenta los meses no es exacto (solo cuenta los meses)
def numero_de_meses_contar(start,end):
	r = relativedelta.relativedelta(end, start)
	return r.months + 1

def llamar(user,inicio,fin):
	print '-------------------------------------------'
	print inicio
	print fin
	print "http://34.209.24.195/facturas?id=%s&start=%s&finish=%s" % (user,inicio,fin)
	print '-------------------------------------------'

	r = requests.get("http://34.209.24.195/facturas?id=%s&start=%s&finish=%s" % (user,inicio,fin))

	try:
	   val = int(r.content)
	   return val
	except ValueError:
	   return False

#iteracion de fechas para retornar generators objetos iteradores
def daterange(start_date,rango_dias):
	for n in range(int (rango_dias)):
	        yield start_date + timedelta(n)

def por_semana(user_id,start,finish):
	suma_7_dias_fecha = start
	contador = 1;
	Total_facturas = 0
	while (suma_7_dias_fecha < finish):
		el_final_tope = suma_7_dias_fecha +timedelta(days=7)
		if el_final_tope > finish:
			break
		r =''
		
		if contador == 1:
			# si es la primera ves le mandamos las fechas normales con el aumento de 7 dias
		   	print 'fecha iterando en 7 dás: %s    %s' % (suma_7_dias_fecha.strftime("%Y-%m-%d"),el_final_tope.strftime("%Y-%m-%d"))
			r = llamar(user_id,suma_7_dias_fecha.strftime("%Y-%m-%d"),el_final_tope.strftime("%Y-%m-%d"))
		else:
			# si no es la primera ves le sumamos un dia mas a la fecha de inicio par ano volver a repetir ciertos dias
			mas_1_dia =suma_7_dias_fecha + timedelta(days=1)
			print 'fecha iterando en 7 dás mas 1 dias: %s    %s' % (mas_1_dia.strftime("%Y-%m-%d"),el_final_tope.strftime("%Y-%m-%d"))
			r = llamar(user_id,mas_1_dia.strftime("%Y-%m-%d"),el_final_tope.strftime("%Y-%m-%d"))
		if r:
			#sumamos las facturas
			Total_facturas += r 
		contador +=1
		suma_7_dias_fecha = suma_7_dias_fecha +timedelta(days=7)
	diferencia_dias_restantes = finish - suma_7_dias_fecha
	print "diferencia_dias_restantes---------- %s" % diferencia_dias_restantes
	for single_date in daterange(suma_7_dias_fecha + timedelta(days=1),diferencia_dias_restantes.days):
		print "dia---------- %s" % single_date.strftime("%Y-%m-%d")
		r = llamar(user_id,single_date.strftime("%Y-%m-%d"),single_date.strftime("%Y-%m-%d"))
		if r:
			#sumamos las facturas
			Total_facturas += r
	return Total_facturas

# metodo que posea la logica de como lo vamos a hacer
def iterar_recursivo(user_id,start,finish,diferencia):
	Total_facturas = 0
	dias_del_mes=calendar.monthrange(start.year,start.month)[1]
	numero_de_meses = numero_de_meses_contar(start,finish)
	#por semana
	print '-------------------------------------------'
	print start.strftime("%Y-%m-%d")
	print finish.strftime("%Y-%m-%d")
	print '-------------------------------------------'
	if diferencia < 8:
		r = llamar(user_id,start.strftime("%Y-%m-%d"),finish.strftime("%Y-%m-%d"))
		if r:
			return r
		else:
			#lo iteramos por día
			for single_date in daterange(start,diferencia):
				r = llamar(user_id,single_date.strftime("%Y-%m-%d"),single_date.strftime("%Y-%m-%d"))
				if r:
					#sumamos las facturas
					Total_facturas += r
    		return Total_facturas
	#por 1 mes
	
	if diferencia <= dias_del_mes:
		r = llamar(user_id,start.strftime("%Y-%m-%d"),finish.strftime("%Y-%m-%d"))
		if r:
			return r
		else:
			respuesta_numero_facturas = por_semana(user_id,start,finish)
    		return respuesta_numero_facturas
				
	#por mas de 1 mes
	if numero_de_meses > 1:
		#significa que es superior al mes y es mas probable que tenga mas de 100 facturas
		r = llamar(user_id,start.strftime("%Y-%m-%d"),finish.strftime("%Y-%m-%d"))
		if r:
			return r
		else:
			suma_dias_fecha = start
			romper_por_mes = False #si falla en mes lo pasamos a True para hacerlo en semanas y luego en días
			contador = 1;
			# intentamos por mes
			while (suma_dias_fecha < finish):
				el_final_tope = suma_dias_fecha +timedelta(days=calendar.monthrange(suma_dias_fecha.year,suma_dias_fecha.month)[1])
				if el_final_tope > finish:
					break
				r =''
				if contador == 1:
					print 'fecha iterando en dás: %s    %s' % (suma_dias_fecha.strftime("%Y-%m-%d"),el_final_tope.strftime("%Y-%m-%d"))
					r = llamar(user_id,suma_dias_fecha.strftime("%Y-%m-%d"),el_final_tope.strftime("%Y-%m-%d"))
				else:
					mas_1_dia = suma_7_dias_fecha + timedelta(days=1)
					print 'fecha iterando en dás: %s    %s' % (mas_1_dia.strftime("%Y-%m-%d"),el_final_tope.strftime("%Y-%m-%d"))
					r = llamar(user_id,mas_1_dia.strftime("%Y-%m-%d"),el_final_tope.strftime("%Y-%m-%d"))
				if r:
					#sumamos las facturas
					Total_facturas += r
				else:
					Total_facturas = 0
					romper_por_mes = True
					break
				contador +=1
				suma_dias_fecha = suma_dias_fecha +timedelta(days=calendar.monthrange(suma_dias_fecha.year,suma_dias_fecha.month)[1])

			if romper_por_mes:
				#lo hacemos por semana
				print "se romprio ahora es por semana----------" 
				respuesta_numero_facturas = por_semana(user_id,start,finish)
				return respuesta_numero_facturas
			else:
				diferencia_dias_restantes = finish - suma_dias_fecha
				print "diferencia_dias_restantes---------- %s" % diferencia_dias_restantes
				for single_date in daterange(suma_dias_fecha + timedelta(days=1),diferencia_dias_restantes.days):
					print "dia---------- %s" % single_date.strftime("%Y-%m-%d")
					r = llamar(user_id,single_date.strftime("%Y-%m-%d"),single_date.strftime("%Y-%m-%d"))
					if r:
						#sumamos las facturas
						Total_facturas += r
	    		return Total_facturas



def validateDateEs(date):
    """
    Funcion para validar una fecha en formato:
        yyyy-mm-dd
    """
    try:
        datetime.strptime(str(date), "%Y-%m-%d")
        return False
    except:
   		pass
    return True

# cuando el usuario entre a la ruta normal el /
#Ha esto se le conoce como decorador
@app.route("/")
@app.route("/numero_facturas/",methods=['GET','POST'])
def id_cliente():
	if request.method == 'POST':
		print '-------------------------------------------'
		print request.form['inicio']
		print request.form['fin']
		print '-------------------------------------------'
		# Guardamos las fechas y el id
		user_id = request.form['id_cliente'] #id del cliente a sacar facturas
		start = request.form['inicio'] #fecha inicio
		finish =request.form['fin']	#fecha fin
		if start!= None and finish != None and user_id != None :

			# Validamos las fechas que tengan el formato correcto
			if validateDateEs(start) or validateDateEs(finish):
				if validateDateEs(start):
					return render_template("hello.html",error="Formato de fecha INICIO invalido")
				if validateDateEs(finish):
					return render_template("hello.html",error="Formato de fecha FIN invalido")
				if str(finish) < str(start):
					return render_template("hello.html",error="Fecha Final no puede ser menor a la fecha de Inicio")
			else:
				# Si las fechas estan bíen procedemos hacer la consulta a la url proporcionada
				fecha_inicial = datetime.strptime(str(start), "%Y-%m-%d")
				fecha_final = datetime.strptime(str(finish), "%Y-%m-%d")

				#pues de igual manera nunca se sabe que tanta actividad tenga el cliente y necesitamos siempre
				# hacer una llamada para ver  si tiene mas de 100
				#sacamos la diferencia en dias
				diferencia = fecha_final -fecha_inicial
				#si el rango de fechas solo es un mes es posible que tenga menos de 100 facturas
				resultado=iterar_recursivo(user_id,fecha_inicial,fecha_final,diferencia.days+1)
				if resultado:
					return render_template("hello.html",id_cliente = user_id,fecha_inicio=start,fecha_fin=finish,numero_facturas=resultado)
				else:
					return render_template("hello.html",error="Hubo algun error inesperado. :(")



		else:
			return render_template("hello.html")
	else:
		# return "Bienvenido Resuelve"
		# return "ID Cliente! %s" % post_id
		return render_template("hello.html")
# esto de aqui es lo primero que se ejecuta y validar que esta corriendo por primera vez
if __name__== "__main__":
	app.debug = True #detecta el cambio y los errores, tambien tira las pantallas de debugin y te dice el error
	app.run()