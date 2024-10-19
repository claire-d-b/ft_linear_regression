
from give_price import load, get_values, display_points
from train_model import train_model

def main():
    df = load('data.csv')
    lhs = get_values(df, "km")
    rhs = get_values(df, "price")
    theta_0, theta_1 = train_model(lhs, rhs)
    display_points(lhs, rhs, theta_0, theta_1)
    print("theta_0", theta_0)
    print("theta_1", theta_1)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")