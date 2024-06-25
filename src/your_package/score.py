import argparse
import logging


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
    logging.info(f"Model scored successfully, results saved to {output_path}")


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
