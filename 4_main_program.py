from random import randint

k = int(input("Enter number of k burnt out lights "))

n = int(input("Enter a length of street "))

print(f"k = {k}")

print(f"n = {n}")


def mean(mean_of_list):
    """
    This function counts the average value of the list.

    Args:
        mean_of_list (list): given list.

    Returns:
        _mean (float): average value.
    """
    _mean = sum(mean_of_list) / len(mean_of_list)
    return _mean


def burn_out_lights(length_of_street):
    """
    This function counts a number of burnt out lights.

    Args:
        length_of_street (int): n - number of lights in a street.

    Returns:
         burn_out (int): number of burnt out lights.
    """
    list_street = []
    for length_of_street in range(0, length_of_street):
        list_street.append(0)

    while True:
        index = randint(0, length_of_street)
        del list_street[index]
        list_street.insert(index, 1)
        if list_street[-1] == 1:
            if list_street[index] == list_street[index - 1]:
                burn_out = list_street.count(1)
                break
        elif list_street[index] == list_street[index - 1] or list_street[index] == list_street[index + 1]:
            burn_out = list_street.count(1)
            break
    return burn_out


def chance_of_k_burn_out_lights():
    """
    This function counts an approximate chance to fix k lights.

    Returns:
         chance_of_k (float): approximate chance of replacing k lights.
    """

    count = 1

    while True:
        if k == burn_out_lights(n):
            break
        else:
            count += 1
    chance_of_k = 1 / count
    return chance_of_k


def main():
    """
    This function counts mean for several attempts.
    """
    list_of_chances = []
    if 0 < k < n:
        for i in range(101):
            list_of_chances.append(chance_of_k_burn_out_lights())
    else:
        print('k cannot be higher equal to n')
    final_result = mean(list_of_chances)
    print(round(final_result, 2))


if __name__ == "__main__":
    main()
