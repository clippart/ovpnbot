rsapath = "/etc/openvpn/server/easy-rsa"

# корневой сертификат
ca = "/etc/openvpn/server/easy-rsa/pki/ca.crt"

# сертификат клиента
ca_cert = r"/etc/openvpn/server/easy-rsa/pki/issued/{user_id}.crt"

# приватный ключ клиента
private_key = r"/etc/openvpn/server/easy-rsa/pki/private/{user_id}.key"

# шаблон конфига
client_common = r"/etc/openvpn/server/client-common.txt/client-common.txt"

# Имя результирующего файла
sertificat = 'sertificat.ovpn'