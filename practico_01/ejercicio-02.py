# Implementar la función mayor, que reciba tres números y devuelva el mayor de ellos.


def mayor(a, b, c):
   if(a > b and a > c):
       return(a)
   else:
       if(b > a and b > c):
           return(b)
       else:
           return(c)


assert mayor(10, 15, 20) == 20
assert mayor(1, 2, 0) == 2

