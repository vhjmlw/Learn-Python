#! /bin/sh

count=0

while [ 1 -lt 2 ]; do
    echo "请输入密码："
    read tmp
    if [ "$tmp" != "python" ]; then
        if [ "$count" -lt 5 ]; then
            count=$(($count+1))
            echo "连续输错$count 次"
        else
            echo '连续输错超过5次，请稍后再试'
            break
        fi
    else
        echo '输入正确'
        break
    fi
done
