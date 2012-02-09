#!/bin/bash

# RingTheBell!: Llamar a que pongan un USB para que podamos hacer un backup
# Autor: Pato Valarezo(c) patovala@pupilabox.net.ec


MOUNTPOINT="/media/SGA-X"
TIEMPO_ESPERA=10 # el tiempo que espera entre prueba de montaje
MAXINTENTOS=10
S1="DO RE MI FA SOL LA SI DO DO RE MI FA SOL LA SI DO"
S2="DO SI LA SOL FA MI RE DO DO SI LA SOL FA MI RE DO"

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

vaciar_respaldos(){
	mv /media/SGA-X/respaldo-sga4-*.* /home/respaldos/respaldos/respaldos/
	echo "Se copiaron los respaldos con satisfacciòn"
}

intentos=0
while [ "$is_montado" != "si" ] && [ $intentos -lt  $MAXINTENTOS ]; do
	mount | grep $MOUNTPOINT && is_montado="si" && echo "sistema montado"

	if [ "$is_montado" == "si" ]
	then
		vaciar_respaldos
		ringthebell $S2 && echo "Respaldos Terminados"
	else
		ringthebell $S1 && echo "Esperando el FLASH USB" && sleep $TIEMPO_ESPERA && intentos=$(($intentos + 1))
	fi
done

