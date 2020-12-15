from math import sqrt

print("Enter quadratic equation in format:")
print("a*x^2+b*x+c=0 or -a*+-x^2-b*-x+-c=-0 or 1*x^2+1*x+0=2")

enter = input('Quadratic equation: ')

def solution(enter):
    
    left, right = enter.split('=')
    a, b, c =left.split('+')

    right = float(right)

    a = float(a.split('*')[0])
    b = float(b.split('*')[0])
    c = float(c)
    
    if right != 0:
        c += float(right)*-1.0
        right = 0

    print(left, right)
    print(a,b,c, right)

    D=b**2.0-4.0*a*c

    print(D)

    if D < 0:
        return ((complex(-b)+sqrt(D*-1.0)*1j)/complex(2*a), 
            (complex(-b)-sqrt(D*-1.0)*1j)/complex(2*a))

    if D == 0:
        return -b/(2*a)
    if D > 0:
        return (-b+sqrt(D))/(2*a), (-b-sqrt(D))/(2*a)

print('ANSVER: ', solution(enter))