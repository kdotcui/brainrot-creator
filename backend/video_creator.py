from story_generator import StoryGenerator
from typing import Dict, Any
import asyncio

class VideoCreator:
	def __init__(self):
		"""Initialize the VideoCreator with a StoryGenerator instance."""
		self.story_generator = StoryGenerator()
		
	async def generate_story(self, prompt_text: str) -> str:
		"""Generate a story using the StoryGenerator."""
		return await self.story_generator.generate_story(prompt_text)


