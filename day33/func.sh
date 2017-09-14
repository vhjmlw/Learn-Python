#! /bin/sh

fun(){
    echo $0
    echo $1
    echo $2
    echo $3
    echo "参数列表$@"
    echo "传参$#个"
}

fun a b c
