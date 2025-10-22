import logging
import json

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_record = {
            'timestamp': self.formatTime(record, self.datefmt),
            'level': record.levelname,
            'message': record.getMessage(),
            'logger': record.name,
            'line': record.lineno,
        }
        # Optionally, add more context (e.g., module, function, exception)
        if record.exc_info:
            log_record['exception'] = self.formatException(record.exc_info)
        return json.dumps(log_record)

def get_logger(name: str, level=logging.INFO):
    logger = logging.getLogger(name)
    # Prevent adding multiple handlers in interactive environments
    if not logger.handlers:
        handler = logging.StreamHandler()
        formatter = JSONFormatter(datefmt='%Y-%m-%dT%H:%M:%S')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
    logger.setLevel(level)
    return logger
