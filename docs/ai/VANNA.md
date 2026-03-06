# 🗄️ Guía de Uso: Vanna AI (SQL Agent)

Vanna es el componente especializado que convierte preguntas en lenguaje natural a consultas SQL precisas sobre tu esquema de Superset/SalesDB.

## 🛠️ Cómo entrenar el agente

Vanna necesita "aprender" la estructura de tus tablas. Sigue estos pasos:

1. Inicia el stack con `docker compose up -d`.
2. Llama al endpoint de entrenamiento con `curl` o un cliente de REST:
   ```bash
   curl -X POST http://TU_IP/vanna/train/schema
   ```
   *Este paso leerá el esquema de PostgreSQL e informará a Vanna sobre las tablas y columnas disponibles.*

## ❔ Cómo preguntar

Puedes enviar preguntas directamente a la API o usarlas desde Flowise:
```bash
curl -X POST http://TU_IP/vanna/ask -H "Content-Type: application/json" -d '{"question": "¿Cuál es la última venta realizada?"}'
```

---

### Detalles de la Implementación (vanna-ai/)

- **Vector Store**: Usa una base de datos local **ChromaDB** persistente en el volumen `vanna_data`.
- **LLM**: Por defecto utiliza OpenAI `gpt-4o-mini`. Puedes cambiarlo a **Ollama** o **Anthropic** en el archivo `main.py`.
- **Persistencia**: Todos los "conocimientos" entrenados están en `./vanna_db/`.

---

Para más información, visita la [Documentación oficial de Vanna](https://vanna.ai/docs/).
