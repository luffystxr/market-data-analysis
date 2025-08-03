def apply_sma_strategy(df, short_window=20, long_window=50):
    df["SMA20"] = df["close"].rolling(window=short_window).mean()
    df["SMA50"] = df["close"].rolling(window=long_window).mean()

    df["signal"] = 0
    df.loc[df["SMA20"] > df["SMA50"], "signal"] = 1
    df.loc[df["SMA20"] <= df["SMA50"], "signal"] = -1

    df["returns"] = df["close"].pct_change()
    df["strategy_returns"] = df["signal"].shift(1) * df["returns"]
    df["cumulative_returns"] = (1 + df["strategy_returns"]).cumprod()

    return df
