#!/bin/sh
NODO=
CLIENTE=
DATA=$(date +%F)
{
  zpool list &
  zfs list
} | mail -s "PVE_SPAZIO $CLIENTE $NODO $DATA" -r "pve@mailbo.it" monitoraggio@mailbo.it
zpool status | mail -s "PVE_DISCO $CLIENTE $NODO $DATA" -r "pve@mailbo.it" monitoraggio@mailbo.it
