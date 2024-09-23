def test(x: int):
    num_type = None
    if x % 2 == 0:
        num_type = "even"
    else:
        num_type = "odd"
    return num_type


if __name__ == "__main__":
    print(test(5))
    