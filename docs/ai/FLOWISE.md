# 🌊 Guía de Uso: Flowise AI

Flowise es la herramienta de orquestación visual que conecta el LLM con tus servicios.

## ⚡ Cómo empezar

1. Accede a `http://TU_IP/flowise/`.
2. Crea un nuevo **Canvas**.
3. Añade componentes clave:
   - **Chat Model**: OpenAI (GPT-4o) u Ollama (Llama 3).
   - **Custom Tool**: Crea una herramienta llamada `Vanna_Chat` que haga un POST HTTP a `http://vanna-ai:8011/ask` con el esquema JSON `{"question": "$input"}`.
   - **Conversation Agent**: Conecta el modelo y la herramienta anterior.

## 🛠️ Casos de Uso integrales

1. **Dashboard Assistant**: Crea un flujo que tome una pregunta y use el **Superset MCP** para listar los cuadros de mando relevantes y mostrarlos al usuario.
2. **SQL Assistant**: Pregunta *"¿Cuántos usuarios se registraron hoy?"*. El flujo enviará la pregunta a Vanna, Vanna generará y ejecutará el SQL sobre PostgreSQL, y Flowise te mostrará el resultado en lenguaje natural.

---

### Mantenimiento

- Todos los flujos se guardan en el volumen de Docker `flowise_data`.
- Las variables de entorno en el `.env` (como API Keys) son automáticamente inyectadas en los nodos.
