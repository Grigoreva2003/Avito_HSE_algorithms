def max_even_sum(lst):
    sum_ = 0
    min_odd = None

    for x in lst:
        if x % 2 == 1:
            if min_odd is None:
                min_odd = x
            else:
                min_odd = min(min_odd, x)
        sum_ += x

    if sum_ % 2 == 1:
        return sum_ - min_odd
    return sum_

if __name__ == "__main__":
    lst = map(int, input().split())
    print(max_even_sum(lst))
