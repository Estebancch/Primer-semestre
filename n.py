sueldos=[]
for x in range(5):
    valor=int(input("ingrese sueldo: "))
    sueldos.append(valor)

print("Lista sin ordenar")
print(sueldos)

for i in range(len(sueldos)-1):
    for j in range(len(sueldos)-1):
        if sueldos[j]>sueldos[j+1]:
            aux=sueldos[j]
            sueldos[j]=sueldos[j+1]
            sueldos[j+1]=aux

print("Lista ordenada")
print(sueldos)

