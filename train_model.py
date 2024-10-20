from pandas import DataFrame
from give_price import normalize, normalize_list


def train_model(lhs: DataFrame, rhs: DataFrame, iterations: int) -> tuple:
    theta_0 = 0
    theta_1 = 0
    se = 0
    y = 0
    thetas_0 = []
    thetas_1 = []
    ses = []
    lst = [(0, 0, 0)]
    sorted_list = []
    index = 0
    i = 0
    mse = 0
    try:
        for i in range(iterations):
            theta_1 = float(i / iterations)
            print("t1", theta_1)
            for j, (x_unit, y_unit) in enumerate(zip(lhs, rhs)):
                y = theta_1 * x_unit + theta_0
                if i == 0:
                    se = (y - y_unit) ** 2
                    theta_0 = - theta_1 * x_unit - y
                    lst.insert(j, (theta_0, theta_1, se))
                    # sorted_list = sorted(lst, key=lambda x: x[2])
                    index = j

                elif ((y - y_unit) ** 2 < se):
                    se = (y - y_unit) ** 2
                    theta_0 = - theta_1 * x_unit - y
                    lst.insert(j, (theta_0, theta_1, se))
                    # Sort by the third element of the tuple (alphabetically)
                    # sorted_list = sorted(lst, key=lambda x: x[2])
                    index = j
        theta0 = - lst[index][0] * 0.1 # step unit in the graph normalized (btw 0 and 1)
        theta1 = - lst[index][1] / len(lhs)
        print(theta0)
        print(theta1)
        a, b, max_value_tuple = max(lst)
        a, b, min_value_tuple = min(lst)
        mse = ((max_value_tuple + min_value_tuple) / len(lst)) ** 0.5

        return theta0, theta1, 100 - mse / 100
        # return 8499.6, -0.0214
    except Exception as e:
        raise AssertionError(f"Error: {e}")