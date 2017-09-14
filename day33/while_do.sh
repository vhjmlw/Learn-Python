#! /bin/sh

echo "请输入密码"
read passwd
while [ "$passwd" != "python" ]; do
    echo "密码错误，请重新输入"
    read passwd
done
echo "输入正确"
exit 0
