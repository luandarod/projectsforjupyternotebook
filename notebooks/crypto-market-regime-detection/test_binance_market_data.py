import pandas as pd
import requests


BASE_URL = "https://api.binance.com/api/v3/klines"


def test_binance_daily_klines_endpoint():
    start_ms = int(pd.Timestamp("2024-01-01", tz="UTC").timestamp() * 1000)
    response = requests.get(
        BASE_URL,
        params={"symbol": "BTCUSDT", "interval": "1d", "startTime": start_ms, "limit": 10},
        timeout=30,
    )
    response.raise_for_status()
    rows = response.json()
    assert len(rows) == 10
    assert len(rows[0]) >= 11
    assert float(rows[0][4]) > 0
    assert float(rows[0][5]) > 0


if __name__ == "__main__":
    test_binance_daily_klines_endpoint()
    print("Binance daily kline endpoint returned BTCUSDT candles.")
