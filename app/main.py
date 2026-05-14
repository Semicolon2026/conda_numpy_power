import yaml
from app.utils import load_csv, clean_columns
from app.processor import add_features, handle_missing
from app.logger import get_logger

logger = get_logger()

CONFIG_PATH = "config/config.yaml"

def load_config():
    with open(CONFIG_PATH, "r") as f:
        return yaml.safe_load(f)

def main():
    config = load_config()
    logger.info("Pipeline started")

    input_path = config["data"]["input_path"]

    df = load_csv(input_path)
    logger.info(f"Loaded data shape: {df.shape}")

    df = clean_columns(df)
    df = handle_missing(df, config["processing"]["fillna_value"])
    df = add_features(df)

    logger.info("Pipeline completed successfully")
    logger.info(df.head().to_string())

if __name__ == "__main__":
    main()
