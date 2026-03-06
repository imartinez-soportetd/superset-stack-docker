import os
from vanna.chromadb.chromadb_vector import ChromaDB_VectorStore
from vanna.remote import VannaDefault
from flask import Flask, request, jsonify
from flask_cors import CORS
from vanna.openai import OpenAI_Chat
import psycopg2

# Basic Setup
# For a full local setup, we'd use Ollama, but let's assume OpenAI/Anthropic/VannaCloud for the demo
# Or use Vanna's built-in remote LLM if no key is provided
class MyVanna(ChromaDB_VectorStore, OpenAI_Chat):
    def __init__(self, config=None):
        ChromaDB_VectorStore.__init__(self, config=config)
        OpenAI_Chat.__init__(self, config=config)

vn = MyVanna(config={
    'api_key': os.getenv('OPENAI_API_KEY', 'sk-None'),
    'model': 'gpt-4o-mini',
    'path': './vanna_db'
})

# Database Connection
def connect_db():
    vn.connect_to_postgres(
        host=os.getenv('POSTGRES_HOST', 'postgres'),
        dbname=os.getenv('POSTGRES_DB', 'superset'),
        user=os.getenv('POSTGRES_USER', 'superset'),
        password=os.getenv('POSTGRES_PASSWORD', 'superset'),
        port=5432
    )

app = Flask(__name__)
CORS(app)

@app.route('/ask', methods=['POST'])
def ask():
    data = request.json
    question = data.get('question', '')
    if not question:
        return jsonify({"error": "No question provided"}), 400
    
    try:
        connect_db()
        sql = vn.generate_sql(question)
        df = vn.run_sql(sql)
        # Convert df to JSON
        results = df.to_dict(orient='records')
        return jsonify({
            "sql": sql,
            "results": results
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/train/schema', methods=['POST'])
def train_schema():
    # Helper to train on the database schema
    try:
        connect_db()
        df_information_schema = vn.run_sql("SELECT * FROM information_schema.tables WHERE table_schema = 'public'")
        vn.train(ddl=df_information_schema.to_string())
        return jsonify({"status": "Schema training samples added"})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8011)
