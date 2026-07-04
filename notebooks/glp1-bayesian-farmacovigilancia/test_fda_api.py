from datetime import date

import requests


BASE_URL = "https://api.fda.gov/drug/event.json"
START_DATE = "20240101"
END_DATE = date.today().strftime("%Y%m%d")
DRUGS = ("SEMAGLUTIDE", "TIRZEPATIDE")


def fetch_seriousness_counts(drug_name):
    params = {
        "search": (
            f'patient.drug.medicinalproduct:"{drug_name}" '
            f"AND receiptdate:[{START_DATE} TO {END_DATE}]"
        ),
        "count": "serious",
    }
    response = requests.get(BASE_URL, params=params, timeout=30)
    response.raise_for_status()
    payload = response.json()
    counts = {item["term"]: item["count"] for item in payload.get("results", [])}
    return counts, payload.get("meta", {})


def test_openfda_seriousness_endpoint():
    for drug_name in DRUGS:
        counts, meta = fetch_seriousness_counts(drug_name)
        assert meta.get("last_updated"), f"{drug_name}: missing last_updated metadata"
        assert counts.get(1, 0) > 0, f"{drug_name}: missing serious reports"
        assert counts.get(2, 0) > 0, f"{drug_name}: missing non-serious reports"


if __name__ == "__main__":
    test_openfda_seriousness_endpoint()
    for drug_name in DRUGS:
        counts, meta = fetch_seriousness_counts(drug_name)
        total = counts.get(1, 0) + counts.get(2, 0)
        rate = counts.get(1, 0) / total
        print(
            f"{drug_name}: {counts.get(1, 0)} serious / {total} total "
            f"({rate:.1%}); openFDA last_updated={meta.get('last_updated')}"
        )
