from random import randint

n = int(input("Enter n "))

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


def main():
    """
    This function counts mean for several attempts.
    """
    list_of_chances = []

    for i in range(1001):
        list_of_chances.append(burn_out_lights(n))
    final_result = mean(list_of_chances)
    a = round(final_result, 2)
    print(f"Average number that have to be replaced for each repair = {a}")
    print(f"Percent of fixed lights to n = {a * 100 / n}%")


if __name__ == "__main__":
    main()
