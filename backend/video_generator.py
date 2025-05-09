from dotenv import load_dotenv
import asyncio, os, json, requests

class VideoCreator:
	def __init__(self):
		"""Initialize the VideoCreator with a StoryGenerator instance."""
		load_dotenv()
		self.MINIMAX_API_KEY = os.getenv("MINIMAX_API_KEY")
		
	async def generate_story(self, prompt_text: str) -> str:
		"""Generate a story using the StoryGenerator."""
		return await self.story_generator.generate_story(prompt_text)
	

video_creator = VideoCreator


