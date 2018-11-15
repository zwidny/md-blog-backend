# My blog backend

## requirements

 1. python3.5+


## 说明
 本项目采用微服务架构， 每个部分均使用token来通信



## X.509 certificate-based authentication

>
 1. openssl req -x509 -newkey rsa:4096 -keyout key.pem -out cert.pem -days 365
 1. openssl x509 -pubkey -noout -in cert.pem > pubkey.pem
 1. openssl rsa -in key.pem -out privkey.pem