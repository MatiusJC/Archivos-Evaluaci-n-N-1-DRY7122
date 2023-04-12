# Ingreso de dirección IP octeto por octeto
octeto1 = input("Ingresa el primer octeto: ")
octeto2 = input("Ingresa el segundo octeto: ")
octeto3 = input("Ingresa el tercer octeto: ")
octeto4 = input("Ingresa el cuarto octeto: ")

# Union de,os octetos para formar la ip
direccion_ip = octeto1 + "." + octeto2 + "." + octeto3 + "." + octeto4

# Determinar si es una IP privada o pública
if direccion_ip.startswith("10.") or direccion_ip.startswith("172.16.") or direccion_ip.startswith("192.168."):
    tipo_ip = "privada"
else:
    tipo_ip = "pública"

# Mostrar la dirección IP y el tipo en pantalla
print("La dirección IP es: " + direccion_ip)
print("Siendo una dirección IP: " + tipo_ip)
