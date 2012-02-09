#!/bin/bash

# RingTheBell!: Llamar a que pongan un USB para que podamos hacer un backup
# Autor: Pato Valarezo(c) patovala@pupilabox.net.ec
export PGPASSWORD="0k9j8h7g"

MOUNTPOINT="/media/SGA-X"
TIEMPO_ESPERA=10 # el tiempo que espera entre prueba de montaje
MAXINTENTOS=10
S1="RE T RE T RE T RE SOL FA SOL FA SOL FA T T RE RE MI FA SOL SOL SOL T RE RE MI FA SOL SOL SOL"
S2="DO RE MI FA SOL LA SI DO DO SI LA SOL FA MI RE DO"
DBPWD="0k9j8h7g"

ringthebell(){
	ARGS=""
	SONG=$*
	for N in $SONG:
	do
		# Notas
		case "$N" in
                        "DO" )  ARGS="$ARGS -n -f 261.6 ";;
                        "T"  )  ARGS="$ARGS -n -f 450.0";;
                        "SI" )  ARGS="$ARGS -n -f 493.9 ";;
                        "LA" )  ARGS="$ARGS -n -f 440.0 ";;
                        "FA" )  ARGS="$ARGS -n -f 349.2 ";;
                        "RE" )  ARGS="$ARGS -n -f 293.7 ";;
                        "MI" )  ARGS="$ARGS -n -f 329.6 ";;
                        "SOL" )  ARGS="$ARGS -n -f 392.0 ";;

		esac
		
	done

	beep $ARGS
}

do_respaldo(){
	# respaldar las bases de datos!
	hoy=$(date +"%Y-%m-%d---%kh%M")
	#hoy=$(date +"%Y-%m-%d")
	#pg_dump --host=sgaapp -U dba --password $DBPWD sga2 -c --format=t | gzip > $MOUNTPOINT/respaldo-sga2-$hoy.tar.gz 
	#pg_dump --host=sgaapp -U dba --password $DBPWD sga -c --format=t | gzip > $MOUNTPOINT/respaldo-sga-$hoy.tar.gz
	#pg_dump --host=sgaapp -U dba --password $DBPWD sga3 -c --format=t | gzip > $MOUNTPOINT/respaldo-sga3-$hoy.tar.gz
	#pg_dump -h sgaapp -U dba -d sga3 -c --format=t | gzip > $MOUNTPOINT/respaldo-sga3-$hoy.tar.gz
	pg_dump -h sgaapp -U dba -d sga4 -c --format=t | gzip > $MOUNTPOINT/respaldo-sga4-$hoy.tar.gz
	echo "Se Hicieron los Respaldos"
}

intentos=0
while [ "$is_montado" != "si" ] && [ $intentos -lt  $MAXINTENTOS ]; do
	mount | grep $MOUNTPOINT && is_montado="si" && echo "sistema montado"

	if [ "$is_montado" == "si" ]
	then
		do_respaldo
		ringthebell $S2 && echo "Respaldos Terminados"
	else
		ringthebell $S1 && echo "Esperando el FLASH USB" && sleep $TIEMPO_ESPERA && intentos=$(($intentos + 1))
	fi
done

