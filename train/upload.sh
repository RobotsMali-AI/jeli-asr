#!/usr/bin/sh

for i in `seq 30`;
do
	if [ $i == 6 ];
	then
		name="griots_r${i}b"
	else
		name="griots_r${i}"
	fi
	gcloud compute scp --recurse $name bayel-griots-node:~/$name
done


echo "UPLOAD COMPLETED!"
