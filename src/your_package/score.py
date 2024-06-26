import argparse
import logging
import pandas as pd
import joblib
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


def score_model(model_path, data_path, output_path):
    logging.info("Starting model scoring")
    # Add your model scoring logic here
    # Example: load model from model_path, load dataset from data_path
    #  score model, save results to output_path
    mlflow.start_run(nested=True)
    mlflow.log_param("model_path", model_path)
    mlflow.log_param("data_pat", data_path)
    mlflow.log_param("output_pat", output_path)

    # Load the model from model_path
    model = joblib.load(model_path)

    # Load the dataset from data_path
    data = pd.read_csv(data_path)

    # Score the model
    predictions = model.predict(data)

    # Save the results to output_path
    results = pd.DataFrame(predictions, columns=['predictions'])
    results.to_csv(output_path, index=False)
    mlflow.log_artifact(output_path)
    logging.info(f"Model scored successfully, results saved to {output_path}")
    mlflow.end_run()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Score Model")
    parser.add_argument(
        "--model-path", type=str, required=True, help="Model folder path"
    )
    parser.add_argument(
        "--data-path", type=str, required=True, help="Dataset folder path"
    )
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
    score_model(args.model_path, args.data_path, args.output_path)
