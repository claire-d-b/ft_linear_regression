
from give_price import load, get_values, display_points

def main():
    df = load('data.csv')
    lhs = get_values(df, "km")
    rhs = get_values(df, "price")
    display_points(lhs, rhs)


if __name__ == "__main__":
    try:
        main()
    except AssertionError as e:
        print(f"{e}")