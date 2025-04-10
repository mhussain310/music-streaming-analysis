from etl.extract import extract_data
from etl.transform import transform_data
from etl.load import load_data


def run_etl():
    print("Extracting data...")
    extracted_data = extract_data()
    print("Data extraction complete.")

    print("Transforming data...")
    transformed_data = transform_data(extracted_data)
    print("Data transformation complete.")

    print("Loading data...")
    load_data(transformed_data)
    print("Data loading complete.")

    print("ETL pipeline ran successfully!")


if __name__ == "__main__":
    run_etl()
