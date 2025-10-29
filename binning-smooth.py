import math

def get_data():
    raw = input("Enter dataset (comma-separated): ")
    data = list(map(int, raw.strip().split(',')))
    data.sort()
    return data

def create_bins(data, bin_size):
    return [data[i:i + bin_size] for i in range(0, len(data), bin_size)]

def smoothing_by_mean(bins):
    smoothed = []
    for b in bins:
        mean_val = sum(b) / len(b)
        smoothed.append([round(mean_val)] * len(b))
    return smoothed

def smoothing_by_median(bins):
    smoothed = []
    for b in bins:
        median_val = sorted(b)[len(b)//2]
        smoothed.append([median_val] * len(b))
    return smoothed

def smoothing_by_boundary(bins):
    smoothed = []
    for b in bins:
        first, last = b[0], b[-1]
        smoothed_bin = [first if abs(x - first) < abs(x - last) else last for x in b]
        smoothed.append(smoothed_bin)
    return smoothed

def print_bins(original, smoothed, method):
    print(f"\n--- {method} ---")
    for i, (orig, smooth) in enumerate(zip(original, smoothed), 1):
        print(f"Bin {i}: Original: {orig} -> Smoothed: {smooth}")

def main():
    data = get_data()
    # 12, 15, 24, 29, 35, 41, 47, 53, 62, 68, 77, 83, 91, 98, 100
    bin_size = int(input("Enter bin size: "))
    
    bins = create_bins(data, bin_size)
    
    mean_smoothed = smoothing_by_mean(bins)
    median_smoothed = smoothing_by_median(bins)
    boundary_smoothed = smoothing_by_boundary(bins)
    
    print_bins(bins, mean_smoothed, "Smoothing by Mean")
    print_bins(bins, median_smoothed, "Smoothing by Median")
    print_bins(bins, boundary_smoothed, "Smoothing by Boundary")

if __name__ == "__main__":
    main()

