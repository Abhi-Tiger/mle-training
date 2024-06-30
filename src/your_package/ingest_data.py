import argparse
import logging
import mlflow.sklearn
import pandas as pd


def setup_logging(log_level, log_path, no_console_log):
    handlers = []
    if log_path:
        handlers.append(logging.FileHandler(log_path))
    if not no_console_log:
        handlers.append(logging.StreamHandler())

    logging.basicConfig(
        level=log_level,
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
        handlers=handlers,
    )


def ingest_data(output_path):
    logging.info("Starting data ingestion")
    mlflow.start_run(nested=True)
    mlflow.log_param("output_path", output_path)
    DOWNLOAD_ROOT = "https://raw.githubusercontent.com/ageron/handson-ml/master/"
    HOUSING_URL = DOWNLOAD_ROOT + "datasets/housing/housing.tgz"
    df = pd.read_csv(HOUSING_URL)
    df.to_csv(output_path, index=False)
    mlflow.log_artifact(output_path)
    # Add your data ingestion logic here
    # Example: download dataset and save to output_path
    logging.info(f"Data ingested successfully and saved to {output_path}")
    mlflow.end_run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Ingest Data")
    parser.add_argument(
        "--output-path", type=str, required=True, help="Output folder path"
    )
    parser.add_argument(
        "--log-level",
        type=str,
        default="INFO",
        help="Log level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)",
    )
    parser.add_argument("--log-path", type=str, help="Log file path")
    parser.add_argument(
        "--no-console-log", action="store_true", help="Disable console logging"
    )
    args = parser.parse_args()

    setup_logging(args.log_level, args.log_path, args.no_console_log)
    ingest_data(args.output_path)
