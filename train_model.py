from pandas import DataFrame


def train_model(lhs: DataFrame, rhs: DataFrame, iterations: int) -> tuple:
    theta_0 = 0
    theta_1 = 0
    ntheta_0 = 0
    ntheta_1 = 0
    se = 0
    y = 0
    lst = [(0, 0, 0)]

    i = 0
    mse = 0
    minimum = float("inf")
    try:
        for i in range(iterations):
            theta_1 = i / iterations

            for j, (x_unit, y_unit) in enumerate(zip(lhs, rhs)):

                # y = ax + b
                # y - b = ax
                # -b = ax - y
                # b = -(ax - y)
                theta_0 = theta_1 * x_unit + y
                # y = ax + b
                #-ax = -y + b
                #-a = (-y + b) / x
                #a = -(-y + b) / x
                # theta_1 = y - theta_0 / x_unit

                y = -theta_1 * x_unit + theta_0

                # first square error calculation
                se = (y - y_unit) ** 2

                lst.append((theta_0, theta_1, se))

                if se < minimum:
                    minimum = se
                    print("min_sq_err", se)
            
            # Sort tuple list by Nth element of tuple
            # using sort() + lambda
            lst.sort(key = lambda x: x[2])
            # This reverses all the pairs, uses min() as normal (comparing the new first number
            # before comparing the second), and then un-reverses that resulting tuple back to the
            # original format.
            # ntheta_0, ntheta_1, min_value_tuple = min_tuple
            # mse = min_value_tuple ** 0.5
        print("0", lst[len(lst) - 1][0])
        print("0", lst[len(lst) - 1][1])
        print("0", lst[1][2])
        return lst[len(lst) - 1][0], lst[len(lst) - 1][1], lst[len(lst) - 1][2]

    except Exception as e:
        raise AssertionError(f"Error: {e}")
