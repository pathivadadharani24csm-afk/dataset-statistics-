"""
Dataset Statistics Calculator
------------------------------
Computes Mean, Median, Mode, Variance, Standard Deviation,
Quartiles (Q1, Q3), and Interquartile Range (IQR) for a given dataset.
"""


def get_stats(data):
    n = len(data)
    data.sort()

    # Mean
    mean = sum(data) / n

    # Median
    if n % 2 == 0:
        median = (data[n // 2 - 1] + data[n // 2]) / 2
    else:
        median = data[n // 2]

    # Mode
    freq = {}
    for x in data:
        freq[x] = freq.get(x, 0) + 1
    mode = max(freq, key=freq.get)

    # Variance & Standard Deviation
    variance = sum((x - mean) ** 2 for x in data) / n
    std_dev = variance ** 0.5

    # Quartiles
    lower_half = data[:n // 2]
    upper_half = data[(n + 1) // 2:]
    q1 = lower_half[len(lower_half) // 2]
    q3 = upper_half[len(upper_half) // 2]
    iqr = q3 - q1

    return mean, median, mode, variance, std_dev, q1, q3, iqr


if __name__ == "__main__":
    # Example dataset - replace with your own
    data = [12, 15, 12, 18, 21, 15, 19, 22, 15, 25, 30, 12, 18]

    mean, median, mode, var, std, q1, q3, iqr = get_stats(data)

    print("Mean:", mean)
    print("Median:", median)
    print("Mode:", mode)
    print("Variance:", var)
    print("Std Dev:", std)
    print("Q1:", q1)
    print("Q3:", q3)
    print("IQR:", iqr)
