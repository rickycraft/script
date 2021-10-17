#!/bin/sh
NODO=
CLIENTE=
DATA=$(date +%F)
zfs list -t snap | mail -s "PVE_SNAP $CLIENTE $NODO $DATA" -r "pve@mailbo.it" monitoraggio@mailbo.it
