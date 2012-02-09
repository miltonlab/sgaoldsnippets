#!/bin/bash

# Realizará una copia de sga4 en sga3
# Autor: marcoxavi
export PGPASSWORD="0k9j8h7g"
cd /home/postgres/respaldos
TIEMPO_ESPERA=10 # el tiempo que espera entre prueba de montaje
MAXINTENTOS=10
S1="RE T RE T RE T RE SOL FA SOL FA SOL FA T T RE RE MI FA SOL SOL SOL T RE RE MI FA SOL SOL SOL"
S2="DO RE MI FA SOL LA SI DO DO SI LA SOL FA MI RE DO"
DBPWD="0k9j8h7g"

do_copia(){
	# genera el sql la base de datos
	pg_dump -c sga3 > datos.sql
	# regenera sga3 es decir la elimina y la vuelve a crear desde cero
	dropdb sga2
	createdb -O dba sga2	
	#llena sga3 con el sql generado desde sga4
	cat datos.sql | psql sga2	
	echo "Se Hicieron los Respaldos"
}

intentos=0
while [ "$is_libre" != "si" ] && [ $intentos -lt  $MAXINTENTOS ]; do
	#antes de pasar al if debo preguntar si el sga3 esta libre para poder hacer el proceso y setear $is_libre =""si, si no esta libre debo forzar a que libere sga3.
	if [ "$is_libre" == "si" ]
	then
		do_copia
		ringthebell $S2 && echo "Copiado sga4 en sga3"
	else
		ringthebell $S1 && echo "Esperando que sga3 este libre" && sleep $TIEMPO_ESPERA && intentos=$(($intentos + 1))
	fi
done

