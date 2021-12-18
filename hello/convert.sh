#openssl pkcs12 -in ./voip.p12 -out voip.pem -nodes
openssl pkcs12 -in ./voip.p12 -out ./voip.pem -nodes -clcerts
