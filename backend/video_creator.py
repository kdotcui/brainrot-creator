from openai import OpenAI
import os
import json
from typing import Dict, Any
from dotenv import load_dotenv
import asyncio

class VideoCreator:
	def __init__(self):
		load_dotenv()
		self.LLM_API_KEY = os.getenv("DEEPSEEK_API_KEY")
		if not self.LLM_API_KEY:
			raise ValueError("Missing DEEPSEEK_API_KEY environment variable")
		
		print(f"Initializing DeepSeek client with API key starting with: {self.LLM_API_KEY[:4]}...")
		self.client = OpenAI(
			api_key=f"{self.LLM_API_KEY}", 
			base_url="https://api.deepseek.com"
		)
	async def generate_story(self, prompt_text: str) -> str:
		response = self.client.chat.completions.create(
			model="deepseek-chat",
			messages=[
				{
					"role": "system",
					"content": """You are a master storyteller writing cinematic scripts for 45-second short videos.
	Each story must be structured as a series of emotionally charged visual scene depctions, with each scene lasting no more than 8 seconds of screen time.
	These stories must take the viewer on a dramatic rollercoaster — filled with sensational highs (e.g. victory, joy, surprise)
	and miserable lows (e.g. betrayal, defeat, sorrow), while remaining tight, vivid, and emotionally gripping.

	Respond in the following format only:
	<response>
	{
		"scenes": [
			{
				"scene": "Scene 1: [Short Title]",
				"description": "Describe what happens in this part of the story in rich, visual detail. Make it emotionally powerful."
				"duration": 3
			},
			{
				"scene": "Scene 2: [Short Title]",
				"description": "Next emotional or dramatic beat. Keep the momentum strong."
				"duration": 5
			},
			...
		],
		"scene_count": 10,
		"total_duration": 40
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

		result = response.choices[0].message.content
		print(result)
		return result


