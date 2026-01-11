import polars as pl 
from pathlib import Path
import logging

REQUIRED_COLUMNS = {'id_email', 'user_email','subject', 'body', 'date', 'language'}

logger = logging.getLogger(__name__)

def read_emails(path: Path) -> pl.DataFrame | None:
    try:
        emails_df = pl.read_csv(path)
        logger.info(f"CSV charged done: {path}")

        if not REQUIRED_COLUMNS.issubset(set(emails_df.columns)):
            missing = REQUIRED_COLUMNS - set(emails_df.columns)
            logger.error(f"Columns missed in emails.csv: {missing}")
            return None
        
        if emails_df.height == 0:
            logger.warning(f"CSV is charged but it's empty: {path}")
        
        return emails_df
    
    except FileNotFoundError:
        logger.error(f"File not found: {path}")
        return None
    except pl.exceptions.PolarsError as e:
        logger.error(f"Error found reading CSV with Polars: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error reading CSV: {e}")
        return None