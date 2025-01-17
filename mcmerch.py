import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("price", type=float, help="The price of the item")
    args = parser.parse_args()
    price = args.price



    total = price * 1.13

    print(f"The total price is {total:.2f}")

if __name__ == '__main__':
    main()