from quart import Quart, jsonify
from openai import OpenAI
from quart_cors import cors
from dotenv import load_dotenv
import asyncio, json, os, tempfile



app = Quart(__name__)
app = cors(app, allow_origin="*")
load_dotenv()

DEEKSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=f"{DEEKSEEK_API_KEY}", base_url="https://api.deepseek.com")


@app.route('/api/test', methods=['GET'])
async def test():
    """Test endpoint to verify the backend is running."""
    return jsonify({"message": "Backend is running successfully!"})

@app.route('/api/createvideo/<prompt>', methods=['GET'])
async def create_video(prompt):
    print()
    response = client.chat.completions.create(
        model="deepseek-chat",
        messages=[
            {"role": "system", "content": f"{"hello monkey"}"},
            {"role": "user", "content": "Hello"},
        ],
        temperature=1.4,
        stream=False
    )
    result = response.choices[0].message.content
    print(result)
    return response.choices[0].message.content
    
    

if __name__ == '__main__':
    app.run()