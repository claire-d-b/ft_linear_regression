from matplotlib.pyplot import subplots
from give_price import load, get_values, display_points, create_figure
from train_model import train_model


def main():
    df = load('data.csv')
    lhs = get_values(df, "km")
    rhs = get_values(df, "price")

    theta_0 = 0
    theta_1 = 0
    exp = 2

    print("Please enter a mileage:")
    mileage = input()

    print("Before training: ", theta_0 + theta_1 * float(mileage))
    theta_0, theta_1, mse = create_figure(exp, lhs, rhs)
    print("After training: ", theta_0 + theta_1 * float(mileage))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")
