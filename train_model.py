from pandas import DataFrame


def train_model(lhs: DataFrame, rhs: DataFrame, iterations: int) -> tuple:
    theta_0 = 0
    theta_1 = 0
    se = 0
    y = 0
    lst = [(0, 0, 0)]
    index = 0
    i = 0
    mse = 0
    try:
        for i in range(iterations):
            theta_1 = float(i / iterations)

            for j, (x_unit, y_unit) in enumerate(zip(lhs, rhs)):
                y = theta_1 * x_unit + theta_0
                # at first iteration, affect a first value / state
                # to the se (square error) variable
                if i == 0:
                    # first square error calculation
                    se = (y - y_unit) ** 2
                    theta_0 = - theta_1 * x_unit - y
                    lst.insert(j, (theta_0, theta_1, se))
                    # sets the index at which the square error is
                    # the smallest
                    index = j

                elif ((y - y_unit) ** 2 < se):
                    # take the smaller value of the square error to minimize
                    # the sse (sum of square errors)
                    se = (y - y_unit) ** 2
                    theta_0 = - theta_1 * x_unit - y
                    lst.insert(j, (theta_0, theta_1, se))
                    # sets the index at which the square error is
                    # the smallest
                    index = j

        # take smallest square error value and set the related theta_0
        ntheta_0 = - lst[index][0] * 0.1  # step unit in the graph normalized
        # (btw 0 and 1)
        # same with the theta_1
        ntheta_1 = - lst[index][1] / len(lhs)

        _, _, max_value_tuple = max(lst, key=lambda x: x[2])
        _, _, min_value_tuple = min(lst, key=lambda x: x[2])
        mse = ((max_value_tuple + min_value_tuple) / len(lst)) ** 0.5

        return ntheta_0, ntheta_1, 100 - mse / 100
        # return 8499.6, -0.0214
    except Exception as e:
        raise AssertionError(f"Error: {e}")
