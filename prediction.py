from give_price import load, get_values, display_points
from train_model import train_model

def main():
    theta_0 = 0
    theta_1 = 0
    print("Please enter a mileage:")
    mileage = input()
    df = load('data.csv')
    lhs = get_values(df, "km")
    rhs = get_values(df, "price")
    ret = theta_0 + theta_1 * float(mileage)
    print("Before training: ", ret)
    theta_0, theta_1 = train_model(lhs, rhs, 1000)
    print("After training: ", theta_0 + theta_1 * float(mileage))


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")