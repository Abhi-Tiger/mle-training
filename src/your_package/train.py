import argparse
import logging
import pandas as pd
from sklearn.linear_model import LinearRegression
import mlflow
import mlflow.sklearn


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


def train_model(data_path, model_path):
    logging.info("Starting model training")
    # Add your model training logic here
    # Example: load dataset from data_path
    #  train model, save model to output_path
    mlflow.start_run(nested=True)
    mlflow.log_param("data_path", data_path)
    mlflow.log_param("model_path", model_path)
    df = pd.read_csv(data_path)
    X = df.drop('target', axis=1)
    Y = df['target']

    model = LinearRegression()
    model.fit(X, Y)

    mlflow.sklearn.load_model(model, "model")
    mlflow.log_artifact(model_path)
    logging.info(f"Model train successful and savedto {model_path}")
    mlflow.end_run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Train Model")
    parser.add_argument(
        "--data-path", type=str, required=True, help="Dataset folder path"
    )
    parser.add_argument(
        "--model_path-path", type=str,
        required=True, help="Model output folder path"
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
    train_model(args.data_path, args.model_path)
