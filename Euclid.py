def gcd(a,b):           #функция вычисления НОДа по алгоритму Евклида
    if a==0:
        return 0
    elif b%a==0:
        return a
    else:
        r=b-int(b/a)*a
        return gcd(r,a)
    
def main():
    a=int(input("Введите первое число для нахождения НОДа: "))
    b=int(input("Введите второе число для нахождения НОДа: "))
    a,b=min(a,b),max(a,b)
    NOD=gcd(a,b)
    print("Ваш НОД:",NOD)

if __name__=='__main__':
    main()

    """
    b=aq+r
    a=rq1+r1
    r=r1q2+r2
    
    r=b-aq
    r1=a-rq1
    .........
    """