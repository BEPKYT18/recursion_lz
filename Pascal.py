def factorial(n):           #функция для вычисления факториала
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

def C(n,k):                                                     #функция для вычисления сочетания из n элементоа по k
    C=int(factorial(n)/(factorial(k)*factorial(n-k)))
    return C

def pascal_triangle(n,t, pasc_tr):              #функция для построения треугольника Паскаля
    List=[]
    if t==n:
        return pasc_tr
    else:
        for i in range(0,t+1):
            c=C(t,i)
            List.append(c)
        pasc_tr.append(List)
        return pascal_triangle(n,t+1, pasc_tr)

def main():
    t=0
    pasc_tr=[]
    n=int(input("введите, какого уровня будет треугольник Паскаля: "))
    pasc_tr=pascal_triangle(n,t,pasc_tr)
    for i in range(len(pasc_tr)):
        print((pasc_tr[i]))
    
if __name__=='__main__':
    main()