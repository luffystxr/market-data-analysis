import matplotlib.pyplot as plt

def plot_price(df):
    plt.figure(figsize=(12,6))
    plt.plot(df["timestamp"], df["close"], label="Closing Price")
    plt.title("Price Trend")
    plt.xlabel("Time")
    plt.ylabel("Price (USDT)")
    plt.legend()
    plt.show()

def plot_sma(df):
    plt.figure(figsize=(12,6))
    plt.plot(df["timestamp"], df["close"], label="Price", alpha=0.5)
    plt.plot(df["timestamp"], df["SMA20"], label="SMA20")
    plt.plot(df["timestamp"], df["SMA50"], label="SMA50")
    plt.title("SMA Crossover Strategy")
    plt.xlabel("Time")
    plt.ylabel("Price (USDT)")
    plt.legend()
    plt.show()
