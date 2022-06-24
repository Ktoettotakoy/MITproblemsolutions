from random import randint

steps = int(input("Enter a number of steps(n) "))

limit = int(input("Enter an upper limit(m) "))


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


def score(n, m):
    """
    This function makes a random list and count points according to the problem.
    Args:
        n (int): number of steps.
        m (int): upper limit according to the problem( 0<= k <= m).
    Returns:
        score (int): number of points you`ve earned.
    """

    list_a = []

    for n in range(0, n):
        rand = randint(0, m)
        list_a.append(rand)

    score_ = list_a[0]

    min_num = list_a[0]

    for num in list_a[1:]:
        if num <= min_num:
            score_ += num
            min_num = num
    return score_


def main():
    """
    This function counts an average number of points
    you`ve earned.
    Returns:
        average_number (float): average value of earned points.
    """

    list_b_average = []

    for repeat in range(1000001):
        list_b_average.append(score(steps, limit))

    average_number = mean(list_b_average)
    print(average_number)


if __name__ == "__main__":
    main()
