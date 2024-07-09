# ingresar vlan
vlan = int(input("Ingrese el número de VLAN: "))

# codigo para comparar las vlns
if 1 <= vlan <= 1005:
    print("La VLAN", vlan, "pertenece al rango normal.")
elif 1006 <= vlan <= 4094:
    print("La VLAN", vlan, "pertenece al rango extendido.")
else:
    print("Número de VLAN inválido. Debe estar entre 1 y 4094.")
