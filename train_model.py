from pandas import DataFrame
from numpy import mean
from give_price import normalize, normalize_list

def find_intercept(a, x1, y1):
# Using the formula b = y1 - a * x1
    b = y1 - a * x1
    return b

def train_model(lhs: DataFrame, rhs: DataFrame):
    theta_0 = 0
    theta_1 = 0
    se = 0
    y = 0
    thetas_0 = []
    thetas_1 = []
    ses = []
    lst = [(0, 0, 0)]
    try:
        for i in range(1000):
            # if i == 500:
            #     break
            theta_1 = float(i / 1000)
            for j, (x_unit, y_unit) in enumerate(zip(lhs, rhs)):
                y = theta_1 * x_unit + theta_0
                if i == 0:
                    se = (y - y_unit) ** 2
                    theta_0 = - theta_1 * x_unit - y
                    lst.insert(j, (theta_0, theta_1, se))
                    sorted_list = sorted(lst, key=lambda x: x[2])
                    index = j

                elif ((y - y_unit) ** 2 < se):
                    se = (y - y_unit) ** 2
                    theta_0 = - theta_1 * x_unit - y
                    lst.insert(j, (theta_0, theta_1, se))
                    # Sort by the third element of the tuple (alphabetically)
                    sorted_list = sorted(lst, key=lambda x: x[2])
                    index = j
        theta0 = - sorted_list[index][0] / 10
        theta1 = - sorted_list[index][1] / len(lhs)
        return theta0, theta1
        # return 8499.6, -0.0214
    except Exception as e:
        raise AssertionError(f"Error: {e}")