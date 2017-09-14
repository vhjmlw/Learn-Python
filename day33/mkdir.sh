#! /bin/sh

is_dir(){
    if [ ! -d $1 ]; then
        return 1
    else
        return 0
    fi
}

for dir in $@; do
    if is_dir $dir;
    then
        echo "$dir 已经存在"
    else
        echo "$dir 不是文件夹，新创建一个"
        mkdir $dir > /dev/null 2>&1
        if [ "$?" -ne 0 ]; then
            echo "创建出错"
        elif [ "$?" -eq 0 ]; then
            echo "创建成功"
        else
            echo "$?"
        fi
    fi
done
