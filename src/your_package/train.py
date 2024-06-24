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
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=handlers
    )

def train_model(data_path, output_path):
    logging.info("Starting model training")
    # Add your model training logic here
    # Example: load dataset from data_path, train model, save model to output_path
    logging.info(f"Model trained successfully and saved to {output_path}")

if _name_ == "_main_":
    parser = argparse.ArgumentParser(description="Train Model")
    parser.add_argument('--data-path', type=str, required=True, help='Dataset folder path')
    parser.add_argument('--output-path', type=str, required=True, help='Model output folder path')
    parser.add_argument('--log-level', type=str, default='INFO', help='Log level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL)')
    parser.add_argument('--log-path', type=str, help='Log file path')
    parser.add_argument('--no-console-log', action='store_true', help='Disable console logging')
    args = parser.parse_args()

    setup_logging(args.log_level, args.log_path, args.no_console_log)
    train_model(args.data_path, args.output_path)
