from typing import List


def show_menu():
    print('1. Citire date')
    print('2. Determinare cea mai lungă subsecvenţă cu proprietatea ca toate numerele sunt prime')
    print('3. Determinare cea mai lungă subsecvență cu proprietatea ca toate numerele sunt palindroame')
    print('4.Iesire')

def read_list() -> List[int]:
    lst = []
    lst_str = input('Dati numerele separate prin spatiu')
    lst_str_split = lst_str.split(' ')
    for num_str in lst_str_split:
        lst.append(int(num_str))
    return lst



def nr_prim(n) -> bool:
#functia determina daca un numar este prim sau nu
    if n < 2:
        return False
    for i in range(2,n//2 + 1):
        if n%i == 0:
            return False
    return True

def test_nr_prim():
    assert nr_prim(3) == True
    assert nr_prim(4) == False
    assert nr_prim(7) == True


test_nr_prim()


def toate_elementele_prime(lst):
#Determina daca toate numerele dintr-o secventa a listei lst sunt prime
    for x in lst:
        if nr_prim(x) is False:
            return False
    return True


def get_longest_all_primes(lst: List[int]) -> List[int]:
    '''
    Determina cea mai lungă subsecvenţă cu proprietatea ca toate numerele sunt prime.
    :param lst: lista in care se cauta subsecventa
    :return: subsecventa gasita
    '''

    result = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if toate_elementele_prime(lst[i:j+1]) and len(lst[i:j+1]) > len(result):
                result=lst[i:j+1]
    return result


def test_get_longest_all_primes():
    assert get_longest_all_primes([2,3,5,8,9,11]) == [2,3,5]
    assert get_longest_all_primes([5,7,13,11,45,67,20,]) == [5,7,13,11]


test_get_longest_all_primes()


def is_palindrome(n) ->bool:
    #Determina daca un numar este palindrom
    ogl = 0
    x = n
    while x > 0:
        c = x % 10
        ogl = ogl * 10 + c
        x = x // 10
    if (ogl == n):
        return True
    else:
        return False


def test_is_palindrome():
    assert is_palindrome(121) == True
    assert is_palindrome(123) == False
    assert is_palindrome(345) == False


test_is_palindrome()

def toate_elementele_palindroame(lst):
# Determina daca toate numerele dintr-o secventa a listei lst sunt palindroame
    for x in lst:
        if is_palindrome(x) is False:
            return False
    return True

def get_longest_all_palindromes(lst: list[int]) -> List[int]:
    """
    Determina cea mai lungă subsecvenţă cu proprietatea ca toate numerele sunt palindroame.
    :param lst: lista in care se cauta subsecventa
    :return: subsecenta gasita
    """
    result2 = []
    for i in range(len(lst)):
        for j in range(len(lst)):
            if toate_elementele_palindroame(lst[i:j + 1]) and len(lst[i:j + 1]) > len(result2):
                result2 = lst[i:j + 1]
    return result2

def test_get_longest_all_palindromes():
    assert get_longest_all_palindromes([22,145,209 ,676,909,555]) == [676,909,555]
    assert get_longest_all_palindromes([4,7,9,3,4567,10]) ==[4,7,9,3]


test_get_longest_all_palindromes()



def main():
    lst = []
    while True:
        show_menu()
        opt = input('Optiunea: ')
        if opt == '1':
            lst = read_list()
        elif opt == '2':
            print('Cea mai lunga subsecventa cu toate numerele prime este:',get_longest_all_primes(lst))
        elif opt == '3':
            print('Cea mai lunga subsecventa cu toate numerele palindroame este:',get_longest_all_palindromes(lst))
        elif opt =='4':
            break
        else:
            print('Optiune invalida.')

if __name__ == '__main__':
    main()