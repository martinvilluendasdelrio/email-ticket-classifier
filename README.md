# Email Ticket Classifier

Sistema híbrido para clasificar correos de soporte en categorías como **bug**, **feature request**, etc., usando un enfoque **rule-based + NLP**.

El objetivo de este proyecto es **aprender IA y procesamiento de texto** mientras se construye una arquitectura **profesional y escalable**, que podría integrarse en un entorno laboral.

---

## 🔹 Arquitectura

El sistema funciona en **pipeline**:

Email entrante
↓
Preprocesamiento (limpieza de texto)
↓
Rule Engine (JSON)
↓
¿Match con confianza ≥ 0.8?
├─ Sí → Resultado final (source = rule)
└─ No → Modelo NLP (próximamente)

### Flujo conceptual

- Primero se buscan **patrones conocidos** definidos en un JSON (`error_patterns_en.json`, `error_patterns_es.json`)  
- Si no hay coincidencias confiables, el **modelo NLP** entra como fallback  
- Cada email procesado devuelve un **JSON con etiqueta, confianza y fuente**  
- Sistema pensado con **human-in-the-loop** para agregar nuevas reglas de manera segura

---

## 🔹 Estructura del proyecto
email-ticket-classifier/
├── data/
│ ├── raw/ # Emails crudos (mock)
│ ├── processed/ # Emails preprocesados
│ └── dictionaries/ # Reglas JSON por idioma
├── src/
│ ├── config/ # Configuración global
│ │ └── settings.py
│ ├── ingestion/ # Lectura de emails
│ │ └── email_reader.py
│ ├── preprocessing/ # Limpieza de texto
│ │ └── text_cleaner.py
│ ├── rules/ # Rule engine
│ │ └── rule_engine.py
│ ├── ml/ # Entrenamiento y predicción NLP
│ │ ├── train.py
│ │ ├── evaluate.py
│ │ └── predict.py
│ ├── pipeline/ # Orquestación del flujo
│ │ └── classify_email.py
│ └── utils/
│ └── logger.py
├── tests/ # Tests iniciales
├── notebooks/ # Exploración / pruebas
├── .gitignore
├── README.md
└── requirements.txt


---

## 🔹 CSV de Emails

Formato de ejemplo (`data/raw/emails.csv`):

| id_email | user_email       | subject                      | body                               | date       | language |
|----------|-----------------|-----------------------------|-----------------------------------|------------|---------|
| 1        | user@example.com | Error 500 al guardar pedido  | La aplicación se cierra al guardar | 2026-01-06 | es      |
| 2        | user2@example.com| Feature request: nueva función | Me gustaría que la app haga X     | 2026-01-06 | es      |
| 3        | user3@example.com| App crashes                  | App crashes when saving invoice    | 2026-01-06 | en      |

---

## 🔹 JSON de reglas (`data/dictionaries/`)

- error_patterns_en.json → Reglas en inglés
- error_patterns_es.json → Reglas en español
---

## 🔹Estructura de ejemplo:

{
  "version": "1.0",
  "last_updated": "2025-01-01",
  "patterns": [
    {
      "id": "ERR_001",
      "pattern": "error 500",
      "label": "bug",
      "confidence": 0.95,
      "match_type": "contains",
      "enabled": true,
      "source": "manual"
    },
    {
      "id": "REQ_002",
      "pattern": "me gustaría que",
      "label": "feature_request",
      "confidence": 0.8,
      "match_type": "contains",
      "enabled": true,
      "source": "manual"
    }
  ]
}
Cada patrón tiene un id, un texto a buscar (pattern), una label, confidence, tipo de coincidencia, si está enabled y la fuente (manual o suggested).
---

## 🔹Salida del sistema
Cada email procesado devuelve un JSON con este formato:
{
  "email_id": 1,
  "label": "bug",
  "confidence": 0.95,
  "source": "rule",
  "rule_id": "ERR_001"
}

Si no hay coincidencia:

{
  "email_id": 4,
  "matched": false
}
---

## 🔹 Umbral de confianza
- Umbral inicial: 0.8
- Si una regla tiene confidence >= 0.8, el resultado se toma directamente
- Si no, se pasa al modelo NLP (futuro)
---
## 🔹 Reglas del proyecto
- Separación reglas vs código → cambios sin tocar lógica
- JSON por idioma → evitar traducciones automáticas
- Human-in-the-loop → agregar nuevas reglas de manera segura
---
## 🔹 Requisitos / Base técnica
Python 3.10+

Librerías mínimas:
    pandas
    scikit-learn
    numpy
Futuro:
    transformers
    langdetect
---
## 🔹Próximos pasos

1. Implementar rule engine mínimo
2. Preprocesar emails y unir con pipeline
3. Validar resultados JSON con emails mock
4. Más adelante:
    - Añadir modelo NLP
    - Evaluación de métricas
    - Integración con APIs de correo real
    - Escalabilidad y logging avanzado

---

## 🔹 Notas

- Las carpetas data/raw y data/processed contienen .gitkeep para mantener la estructura sin subir datos sensibles
- .gitignore preparado para no subir CSVs ni datos privados