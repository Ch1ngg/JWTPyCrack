# JWTPyCrack
 JWT 弱口令 Key 爆破以及生成 NONE 加密的无 Key 的 JWTString。

![](./PIC/Snipaste_2019-09-05_15-42-06.png)

# 环境
> Python >= 3 

卸载所有的jwt包
> pip3 uninstall pyjwt pip3 uninstall jwt

安装 jwt 包
> pip3 install pyjwt==1.6.4 --user -i https://pypi.douban.com/simple

# 使用

该脚本能实现两种攻击方式：禁用哈希重新生成JWT字符串攻击、批量爆破弱密钥
## 禁用哈希
> python jwtcrack.py -m generate -s {\"admin\":\"True\"}

![](./PIC/Snipaste_2019-09-05_16-09-31.png)


## 批量爆破弱密钥

> python jwtcrack.py -m blasting -s eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiaWF0IjoxNTE2MjM5MDIyfQ.keH6T3x1z7mmhKL1T3r9sQdAxxdzB6siemGMr_6ZOwU --kf C:\Users\Ch1ng\Desktop\2.txt

![](./PIC/Snipaste_2019-09-05_16-07-58.png)

# 感谢
https://www.freebuf.com/vuls/211842.html

# 法律
> 该项目仅供合法的渗透测试以及爱好者参考学习，请勿用于非法用途，否则自行承担相关责任！
