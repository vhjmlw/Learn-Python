#! /bin/sh

echo '请输出yes or no'
read tmp
case "$tmp" in
    yes|y|Y|YES|Yes|YEs)
        echo '您输出的是yes';;
    no|NO|n|N)
        echo '您输入的是no';;
    *)
        echo '请输出yes or no'
        exit 1;;
esac
    echo 'done'
    exit 0
