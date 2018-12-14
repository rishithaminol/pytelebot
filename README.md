ssl generate command
openssl req -x509 -nodes -days 365 -newkey rsa:2048 -keyout localhost.key -out localhost.crt -config certconf.conf

server.py - Initial execution file.
certconf.conf - Certificate generation config.
config.py - Global project configuration.
