import argparse
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("price", type=float, help="The price of the item")
    parser.add_argument(
        "--province",
        type=str,
        default="Ontario",
        choices=["Ontario", "Quebec"],
        help="THe province where the tax is applied (default: Ontario)"
    )
    args = parser.parse_args()

    tax_rate = 1.13

    if args.province == "Ontario":
        tax_rate = 1.13
    elif args.province == "Quebec":
        tax_rate = 1.14975

    price = args.price
    total = price * tax_rate

    print(f"The total price is {total:.2f}")

if __name__ == '__main__':
    main()