import math

def get_user_data():
    raw_data = input("Enter dataset (comma-separated numbers): ")
    data = list(map(int, raw_data.strip().split(',')))
    data.sort()
    return data


def equal_width_partitioning(data, num_intervals, user_min=None, user_max=None):
    print("\n--- Equal Width Partitioning ---")

    data_min = user_min if user_min is not None else min(data)
    data_max = user_max if user_max is not None else max(data)
    data_range = data_max - data_min
    interval_width = math.ceil(data_range / num_intervals)

    print(f"Min: {data_min}, Max: {data_max}, Range: {data_range}, Interval Width: {interval_width}")

    intervals = []
    ranges_elements = []

    for i in range(num_intervals):
        lower = data_min + i * interval_width
        upper = lower + interval_width

        if i == num_intervals - 1:
            elements = [x for x in data if lower <= x <= upper]
        else:
            elements = [x for x in data if lower <= x < upper]

        intervals.append(f"[{lower} - {upper}]")
        ranges_elements.append(elements)

    print("\nRanges and Elements:")
    for i, (interval, elements) in enumerate(zip(intervals, ranges_elements), 1):
        print(f"Interval {i}: {interval} -> Frequency: {len(elements)}, Elements: {elements}")


def equal_frequency_partitioning(data, num_intervals):
    print("\n--- Equal Frequency Partitioning ---")

    data.sort()
    total = len(data)
    group_size = math.ceil(total / num_intervals)

    intervals = []
    ranges_elements = []

    for i in range(0, total, group_size):
        group = data[i:i + group_size]
        if group:
            lower = group[0]
            upper = group[-1]
            intervals.append(f"[{lower} - {upper}]")
            ranges_elements.append(group)

    print(f"\nGroup Size (approx): {group_size}")
    print("\nRanges and Elements:")
    for i, (interval, elements) in enumerate(zip(intervals, ranges_elements), 1):
        print(f"Interval {i}: {interval} -> Frequency: {len(elements)}, Elements: {elements}")


def main():
    data = get_user_data()
    num_intervals = int(input("Enter number of intervals: "))

    print("\nChoose partitioning method:")
    print("1. Equal Width Partitioning")
    print("2. Equal Frequency Partitioning")

    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        print("\nFor Equal Width Partitioning, you can provide min and max values (or press Enter to skip).")
        user_min_input = input("Enter minimum value (or press Enter to use dataset min): ")
        user_max_input = input("Enter maximum value (or press Enter to use dataset max): ")

        user_min = int(user_min_input) if user_min_input else None
        user_max = int(user_max_input) if user_max_input else None

        equal_width_partitioning(data, num_intervals, user_min, user_max)

    elif choice == "2":
        equal_frequency_partitioning(data, num_intervals)

    else:
        print("Invalid choice.")


if __name__ == "__main__":
    main()
