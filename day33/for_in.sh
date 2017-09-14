#! /bin/sh

for tmp in `ls ~/Desktop`; do
    if [ -d ~/Desktop/$tmp ]; then
        echo "$tmp--文件夹"
    elif [ -f ~/Desktop/$tmp ]; then
        echo "$tmp--文件"
    else
        echo 'shit'
    fi
done
