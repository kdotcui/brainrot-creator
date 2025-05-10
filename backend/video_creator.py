from story_generator import StoryGenerator
from video_generator import VideoGenerator
from typing import Dict, Any
import asyncio, os, json, requests

class VideoCreator:
	def __init__(self):
		"""Initialize the VideoCreator with a StoryGenerator instance."""
		self.story_generator = StoryGenerator()
		# self.video_generator = VideoGenerator()
		
	async def generate_story(self, prompt_text: str) -> str:
		"""Generate a story using the StoryGenerator."""
		return await self.story_generator.generate_story(prompt_text)



