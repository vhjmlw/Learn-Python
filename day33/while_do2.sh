#! /bin/sh

count=1

while [ "$count" -lt 10 ]; do
    echo "$count"
    count=$(($count+1))
done
echo 'over'
exit 0
