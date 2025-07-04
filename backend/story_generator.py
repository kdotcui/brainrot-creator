from openai import OpenAI
import os, re, json
from dotenv import load_dotenv

class StoryGenerator:
    def __init__(self):
        load_dotenv()
        self.DEEKSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
        if not self.DEEKSEEK_API_KEY:
            raise ValueError("Missing DEEPSEEK_API_KEY environment variable")
        
        print(f"Initializing DeepSeek client with API key starting with: {self.DEEKSEEK_API_KEY[:4]}...")
        self.client = OpenAI(
            api_key=f"{self.DEEKSEEK_API_KEY}", 
            base_url="https://api.deepseek.com"
        )

    async def generate_story(self, prompt_text: str) -> str:
        """
        Generates a structured story based on the given prompt.
        Returns the story as a formatted JSON string.
        """
        response = self.client.chat.completions.create(
            model="deepseek-chat",
            messages=[
                {
                    "role": "system",
                    "content": """You are a master storyteller writing cinematic scripts for 37second-47second short videos.
Each story must be structured as a series of emotionally charged visual scene depctions, with each scene lasting exactly 5 seconds of screen time.
These stories must take the viewer on a dramatic rollercoaster — filled with sensational highs (e.g. victory, joy, surprise)
and miserable lows (e.g. betrayal, defeat, sorrow), while remaining tight, vivid, and emotionally gripping.
The scene_count should count up the total number of scenes created, total_duration should be the total number of seconds of the scenes
The summary should describe the stories scenes, similar to the summary in the response template
Respond in the following format only:
<response>
{
    "scenes": [
        {
            "scene": "Scene 1: [Short Title]",
            "description": "Describe what happens in this part of the story in rich, visual detail. Make it emotionally powerful."
            "duration": 5
        },
        {
            "scene": "Scene 2: [Short Title]",
            "description": "Next emotional or dramatic beat. Keep the momentum strong."
            "duration": 5
        },
        ...
    ],
    "scene_count": 10,
    "total_duration": 40,
    "summary": "In a world soaked with rain and loneliness, a scrappy stray dog trembles beside an empty bowl—forgotten, hungry, and alone. But fate arrives on velvet paws. A bold black cat, agile and mischievous, topples a dumpster and spills hope in the form of food. What starts as a snarling showdown in the shadows soon melts into an unexpected alliance. From sharing sausage scraps under flickering alley lights to frolicking in golden parks, their bond deepens—a cat on a dog’s back, two misfits writing their own legend. Just as joy blooms, danger strikes. A net falls, a leash snaps, and they’re ripped apart. The dog tears through the city, nose down, heart pounding. Posters flutter. Doors slam. Time runs thin. In a van, the cat cries out, clawing at fate. Then—a blur, a leap, a miracle. The dog soars through the air, smashing into destiny itself. They crash together in a whirl of leaves, tongues and tails tangled in joy. The van vanishes into insignificance. What matters is the sunset—and the forever forged between two strays who found each other."
}
</response>

Make the pacing fast, the emotions raw, and the transitions clear. End with impact."""
                },
                {
                    "role": "user",
                    "content": f"""
                Prompt: {prompt_text}

                Generate a short story with 10 to 15 distinct scenes, formatted as requested. The story should be suitable for a 45-second video and have wild emotional shifts — think tragic falls, euphoric wins, betrayal, triumph, or mystery.
                """
                },
            ],
            temperature=1.4,
            max_tokens=1800,
            stream=False,
        )

        raw_result = response.choices[0].message.content
        print(raw_result)

        try:
            # Find JSON content between <response> tags
            match = re.search(r'<response>\s*(.*?)\s*</response>', raw_result, re.DOTALL)
            if not match:
                raise ValueError("Response format not as expected: missing <response> tags")
            
            json_str = match.group(1)
            # Parse the JSON string into a Python dictionary
            story_data = json.loads(json_str)
            
            # Validate that required fields exist
            required_fields = ["scenes", "scene_count", "total_duration", "summary"]
            for field in required_fields:
                if field not in story_data:
                    raise ValueError(f"Response missing required field: {field}")
            
            return story_data
        except json.JSONDecodeError as e:
            print(f"Error parsing JSON: {e}")
            print(f"Problematic JSON string: {json_str}")
            # Return a simple error object that's still valid JSON
            return {
                "error": "Failed to parse the story response",
                "raw_response": raw_result
            }
        except Exception as e:
            print(f"Error processing response: {e}")
            return {
                "error": str(e),
                "raw_response": raw_result
            }