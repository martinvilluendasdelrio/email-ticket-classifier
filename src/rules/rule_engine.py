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

    rules_dir = Path(path)

    rule_files = [
        rules_dir / "error_patterns_en.json",
        rules_dir / "error_patterns_es.json"
    ]

    all_rules: list[dict] = []

    for rule_file in rule_files:
        with open(rule_file, 'r', encoding='utf-8') as f:
            rules = json.load(f)

            patterns = rules.get('patterns', [])
    
            enabled_rules = [r for r in patterns if r.get("enabled", False)]
            
            all_rules.extend(enabled_rules)

    logger.info('Rules read successfully')

    return all_rules
    

def evaluate_rule(text: str, rules: dict) -> bool:
    """
    Evalúa si un texto cumple una regla concreta.

    Soporta:
    - contains
    - startswith
    - regex (opcional)
    """
    text = text.lower()
    pattern = rules.get("pattern", "").lower()

    return pattern in text

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