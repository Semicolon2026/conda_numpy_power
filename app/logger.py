from loguru import logger

def get_logger():
    logger.remove()
    logger.add(
        sink=lambda msg: print(msg, end=""),
        format="{time} | {level} | {message}",
        level="INFO"
    )
    return logger
