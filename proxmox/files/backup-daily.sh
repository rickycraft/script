#!/bin/bash

setsnap=14

while read -r datastore; do
	snapshot_today=$datastore@backup_$(date +"%m-%d-%H-%M")

	zfs snapshot -r "$snapshot_today"

	zfs list -H -o name -t snapshot | sort -r | grep "$datastore@backup" >list_snap

	n=1
	while read -r snap; do
		if [ "$n" -gt "$setsnap" ]; then
			zfs destroy -r "$snap"
		fi
		n=$((n + 1))
	done <list_snap

	zfs list -t snapshot "$datastore"

done <list_datastore
