from random import randrange

m = 2

number_k = input("Number from 01 to 99(k) ")


def len_rand(len_m):
    """
    This function generates random nuber including 01 etc.

    Args:
        len_m (int): number of digits.

    Returns:
        rand_num (str): random number with len_m digits, including 00, 01 etc.

    """
    random_m_digit_number = 10 ** len_m
    rand_num = f'{randrange(random_m_digit_number):0{len_m}}'
    return rand_num


def primitive(n, coefficient_k):
    """
    This function creates a list of unsorted primitive solutions.

    Args:
        n (int): n-digit number
        coefficient_k (str): 2-digit number you want to find according to the problem.

    Returns:
        list_of_primitive (list): unsorted list with primitive solutions.
    """

    coefficient_k = int(coefficient_k)

    list_of_primitive = []

    for i in range(5000001):

        number_a = len_rand(m)
        if number_a == "00":
            continue

        number_b = len_rand(n - m)

        conc_a_and_b = f'{number_a}{number_b}'

        conc_b_and_a = f'{number_b}{number_a}'

        k = int(f'{conc_b_and_a}{conc_b_and_a}') / int(f'{conc_a_and_b}{conc_a_and_b}')

        if k == coefficient_k:
            list_of_primitive.append(conc_a_and_b)
    return list_of_primitive


def sorted_primitive_list(unsorted_list):
    """
    This function cleans and sorts list.

    Args:
        unsorted_list (list): list you want to sort.

    Returns:
         clean_list_of_primitive (list): sorted list.
    """

    clean_list_of_primitive = []

    for b in unsorted_list:
        if b not in clean_list_of_primitive:
            clean_list_of_primitive.append(b)
    return sorted(clean_list_of_primitive)


def main():
    for n in range(3, 11):
        print(f'n = {n}')
        print(sorted_primitive_list(primitive(n, number_k)))


if __name__ == "__main__":
    main()
