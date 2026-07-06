import requests


def fetch_latest(code):
    response = requests.get(
        f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{code}/dados/ultimos/5",
        params={"formato": "json"},
        timeout=30,
    )
    response.raise_for_status()
    rows = response.json()
    assert len(rows) >= 1
    assert "data" in rows[-1]
    assert float(str(rows[-1]["valor"]).replace(",", ".")) == float(str(rows[-1]["valor"]).replace(",", "."))
    return rows


def test_bcb_sgs_core_series():
    for code in [433, 1, 11]:
        fetch_latest(code)


if __name__ == "__main__":
    test_bcb_sgs_core_series()
    print("BCB SGS returned IPCA, USD/BRL, and Selic observations.")
