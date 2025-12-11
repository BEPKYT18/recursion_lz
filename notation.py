
def convert_to_base(number:int, system:int,new_number=''): #функция для приведения числа в другую систему счисления
    if number<system:
        if number==10:                      #если перевод в 16-ричную систему, то остатки нужно привести к нужному виду
            number='A'

        if number==11:
            number='B'

        if number==12:
            number='C'

        if number==13:
            number='D'

        if number==14:
            number='E'

        if number==15:
            number='F'

        new_number+=str(number)
        return new_number
    else:
        if number%system==10:                   
            new_number+='A'

        elif number%system==11:
            new_number+='B'

        elif number%system==12:
            new_number+='C'

        elif number%system==13:
            new_number+='D'

        elif number%system==14:
            new_number+='E'

        elif number%system==15:
            new_number+='F'
        
        else:
            new_number+=str(number%system)
        
        return convert_to_base(int(number/system), system, new_number)
        
def reverse(a,num):             #функция переворота строки
    if a=='':
        return num
    else:
        num+=a[-1]
        a=a[:-1]
        return reverse(a,num)

def main():
    a=int(input('Введите число для перевода в другую систему счисления: '))
    b=int(input("Введите систему счисления: "))

    a=convert_to_base(a,b)
    num='' 
    num=reverse(a,num)
    print(f"ваше число в {b}-ичной системе счисления:",num)
    
if __name__=='__main__':
    main()