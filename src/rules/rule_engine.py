from pathlib import Path
import json
import polars as pl
import logging

logger = logging.getLogger(__name__)

#Constantes
RULE_LABEL_COL = 'rule_label'
RULE_CONFIDENCE_COL = 'rule_confidence'
RULE_ID_COL = 'rule_id'
RULE_SOURCE_COL = 'rule_source'

def load_rule(path: Path | str) -> list[dict]:
    """
    Carga las reglas desde un archivo JSON.

    - Lee el archivo
    - Filtra reglas habilitadas
    - Devuelve lista de dicts
    """
    logger.info("Loading rules")

def evaluate_rule(text: str, rule: dict) -> bool:
    """
    Evalúa si un texto cumple una regla concreta.

    Soporta:
    - contains
    - startswith
    - regex (opcional)
    """

def match_rule(text: str, rules: list[dict]) -> dict | None:
    """
    Devuelve la primera regla que matchea con el texto.
    """

def apply_rules(df: pl.DataFrame, rules: list[dict]) -> pl.DataFrame:
    """
    Aplica las reglas a un DataFrame con columna full_text
    y añade columnas de resultado.
    """
    logger.info("Applying rule engine")