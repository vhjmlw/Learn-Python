#! /bin/sh

echo '请输入YES or NO'
read tmp

if [ "$tmp" = 'yes' ]; then
    echo '您输出的是yes'
elif [ "$tmp" = 'no' ]; then
    echo '您输出的是no'
else
    echo '您输出的既不是yes也不是no，请输出正确的值'
    exit 1
fi
exit 0
