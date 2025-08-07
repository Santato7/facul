n = int(input("Quantas ocorrencias você vai fazer: "))

for j in range(0,n):
    R1 = int(input("Valor de R1: "))
    R2 = int(input("Valor de R2: "))
    V = int(input("Valor da tensão: "))



i = V / (R1 + R2)
vr1 = R1 * i 
vr2 = R2 * i 

print(f"I={i} \n VR1 ={vr1} \n VR2 ={vr2}")
 