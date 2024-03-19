

#Resposta - 1
a=13
soma=0
k=0

while k < a:
  k=k+1
  soma=soma+k
  print(soma)


#Resposta - 2

#OBS: essa resposta eu tive que ver um video pra tentar resolver eu tive o entendimento da logica porém não sabia coloca-la como código
def is_fibonacci(num):
   n1, n2 = 0, 1
   while n2 < num:
      n1, n2 = n2, n1 + n2
   return n2 == num
  
numero = int(input('Digite o numero desejado: '))
if is_fibonacci(numero):
    print('e fibonacci')
else:
    print('não e fibonacci')
    
#Resposta - 3 = 9, 128, 49, 100, 13, 23

#Resposta - 4 = eu já havia visto essa questão em estudos, porém nas resposta que eu já vi, sempre me questionei, como saberei se a lampada esta quente? la teria uma escada para caso a lampado fosse no teto para eu verificar, ou se ela estava em uma mesa para eu verificar sua temperatura?
    

#respota - 5 = 

nome = str(input('Digite se nome: '))

print(nome[::-1]) 

