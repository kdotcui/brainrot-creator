from quart import Quart, jsonify, request
from openai import OpenAI
from quart_cors import cors
from dotenv import load_dotenv
import asyncio, json, os, tempfile
from video_creator import VideoCreator



app = Quart(__name__)
app = cors(app, allow_origin="*")
load_dotenv()

DEEKSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
client = OpenAI(api_key=f"{DEEKSEEK_API_KEY}", base_url="https://api.deepseek.com")

video_creator = VideoCreator()


@app.route('/api/test', methods=['GET'])
async def test():
    """Test endpoint to verify the backend is running."""
    return jsonify({"message": "Backend is running successfully!"})

@app.route('/api/createvideo', methods=['GET'])
async def create_video():
    prompt = request.args.get('prompt')  # Grabs ?prompt=... from the URL
    print("sent: ", prompt)
    generated_story = await video_creator.generate_story(prompt)
    print(generated_story)

    return jsonify(generated_story)

    
    

if __name__ == '__main__':
    app.run()