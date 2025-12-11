def is_perfect(n,c,t):           #функция проверки на совершенность числа
    if c==1:
        return False
    elif n==1:
        return c==t
    else:
        for i in range(2,int(n/2)+1):
            if n%i==0:
                t+=i
        return is_perfect(1,c,t)

def main():
    n=int(input('Введите число для проверки: '))
    t=1
    c=n
    List=is_perfect(n,c,t)
    print(List)
    
if __name__=='__main__':
    main()