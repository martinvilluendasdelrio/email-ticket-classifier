import polars as pl
import logging

logger = logging.getLogger(__name__)

#CONSTANTS
CLEAN_SUBJECT_COL = "clean_subject"
CLEAN_BODY_COL = "clean_body"
FULL_TEXT_COL = "full_text"

#CLEAN EXPRESION
def clean_expr(expr: pl.Expr) -> pl.Expr:
    return(expr
           .fill_null("")
           .str.to_lowercase()
           .str.strip_chars()
           )

#CLEAN DATA
def clean_text(df: pl.DataFrame) -> pl.DataFrame:

    logger.info("Starting text cleaning process")

    df = df.with_columns(
        clean_expr(pl.col("subject")).alias(CLEAN_SUBJECT_COL),
        clean_expr(pl.col("body")).alias(CLEAN_BODY_COL),
    )

    logger.debug("Clean subject and body columns created")

    df = df.with_columns(
        pl.concat_str(
            [pl.col(CLEAN_SUBJECT_COL), pl.col(CLEAN_BODY_COL)],
            separator=" "
        ).alias("full_text")
    )

    logger.debug("Full text column created")

    logger.info("Text cleaning process finished")
    
    return df