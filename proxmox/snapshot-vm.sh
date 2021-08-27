#!/bin/bash

# arg1 is the number of snapshot
# arg2-n is the vm number

if [[ $# -lt 2 ]]; then
	echo "Please provide more arguments"
	exit 1
fi

cd /tmp || exit 1

today=SNAP_$(date +"%m_%d_%H_%M")
nsnap=$1
echo "Keeping $nsnap snapshots"
shift

for vmid in "$@"
do
	#make new snap
	echo "Snap vm-$vmid"
	qm snapshot "$vmid" "$today"

	# list current snapshots
	qm listsnapshot "$vmid" | awk '{print $2}' | grep -v current | sort -r > "$vmid-snap"
	cat "$vmid-snap"

	#delete old snap
	n=1
	while read -r snapname
	do
		if [ "$n" -gt "$nsnap" ]; then
				qm delsnapshot "$vmid" "$snapname"
		fi
		n=$((n + 1))
	done < "$vmid-snap"
done
