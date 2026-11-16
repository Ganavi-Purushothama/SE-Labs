
def parse_request(text):
    """Parse an elevator request in FROM->TO format."""
    if not isinstance(text, str):
        return None

    try:
        parts = text.split("->")

        if len(parts) != 2:
            return None

        start, end = parts

        start = int(start.strip())
        end = int(end.strip())

        if start < 0 or end < 0:
            return None

        return start, end

    except (ValueError, TypeError):
        return None


def total_travel(floors_csv):
    """Calculate total distance travelled between consecutive floors."""
    if not isinstance(floors_csv, str) or not floors_csv.strip():
        return None

    try:
        floors = [int(f.strip()) for f in floors_csv.split(",")]

        if any(f < 0 for f in floors):
            return None

        return sum(
            abs(floors[i + 1] - floors[i])
            for i in range(len(floors) - 1)
        )

    except (ValueError, TypeError):
        return None


def load_percent(text):
    """Calculate elevator load percentage."""
    if not isinstance(text, str):
        return None

    try:
        parts = text.split(" of ")

        if len(parts) != 2:
            return None

        load, capacity = [int(x.strip()) for x in parts]

        if load < 0 or capacity <= 0:
            return None

        return load * 100 // capacity

    except (ValueError, TypeError):
        return None


def main():
    print("==== Running parse_request ====")
    user_input = input("Enter a request as FROM->TO (e.g. 5->9): ")
    result = parse_request(user_input)
    print("From and To:", result)

    print("\n==== Running total_travel ====")
    user_input = input("Enter floors visited as CSV (e.g. 1,5,3,9): ")
    result = total_travel(user_input)
    print("Floors Travelled:", result)

    print("\n==== Running load_percent ====")
    user_input = input("Enter load as 'X of Y' (e.g. 450 of 630): ")
    result = load_percent(user_input)
    print("Load Percent:", result)


if __name__ == "__main__":
    main()
