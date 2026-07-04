import pandas as pd


DATA_URL = "https://raw.githubusercontent.com/YuluDuan/Hypothesis-Testing-Data-Science-salary-comparison-in-different-location/main/ds_salaries.csv"
REQUIRED_COLUMNS = {
    "work_year",
    "experience_level",
    "employment_type",
    "job_title",
    "salary_in_usd",
    "employee_residence",
    "remote_ratio",
    "company_location",
    "company_size",
}


def test_salary_dataset_shape():
    df = pd.read_csv(DATA_URL)
    missing = REQUIRED_COLUMNS.difference(df.columns)
    assert not missing, f"Missing columns: {sorted(missing)}"
    assert len(df) >= 500
    assert {0, 100}.issubset(set(df["remote_ratio"].dropna().unique()))
    assert df["salary_in_usd"].gt(0).all()


if __name__ == "__main__":
    test_salary_dataset_shape()
    df = pd.read_csv(DATA_URL)
    print(
        f"Loaded {len(df):,} rows with remote_ratio values "
        f"{sorted(df['remote_ratio'].dropna().unique().tolist())}"
    )
