FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Set dynamic port via ENV
ENV MCP_PORT=8010
EXPOSE 8010

CMD ["python", "main.py"]
