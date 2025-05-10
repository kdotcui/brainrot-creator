from dotenv import load_dotenv
import asyncio, os, json, requests, time


class VideoGenerator:
	def __init__(self):
		"""Initialize the VideoCreator with a StoryGenerator instance."""
		load_dotenv()
		self.MINIMAX_API_KEY = os.getenv("MINIMAX_API_KEY")
		self.model = "T2V-01" 
		self.output_file_name = f"{int(time.time())}.mp4"
		self.url = "https://api.minimaxi.chat/v1/video_generation"
		
	def invoke_video_generation(self, text_prompt: str) -> str:
		"""Generate a video using MiniMax API"""
		print("-----------------Submit video generation task-----------------")
		

		headers = {
			'authorization': 'Bearer ' + self.MINIMAX_API_KEY,
			'content-type': 'application/json',
		}
		payload = json.dumps({
			"prompt": text_prompt,
			"model": self.model
		})

		response = requests.request("POST", self.url, headers=headers, data=payload)
		print(response.text)

		task_id = response.json()['task_id']
		print("Video generation task submitted successfully, task ID.："+task_id)
		return task_id
	
	def query_video_generation(self, task_id: str):
		url = "https://api.minimaxi.chat/v1/query/video_generation?task_id="+task_id
		headers = {
			'authorization': 'Bearer ' + self.MINIMAX_API_KEY
		}
		response = requests.request("GET", url, headers=headers)
		status = response.json()['status']
		if status == 'Preparing':
			print("...Preparing...")
			return "", 'Preparing'
		elif status == 'Queueing':
			print("...In the queue...")
			return "", 'Queueing'
		elif status == 'Processing':
			print("...Generating...")
			return "", 'Processing'
		elif status == 'Success':
			return response.json()['file_id'], "Finished"
		elif status == 'Fail':
			return "", "Fail"
		else:
			return "", "Unknown"
		
	def fetch_video_result(self, file_id: str):
		print("---------------Video generated successfully, downloading now---------------")
		url = "https://api.minimaxi.chat/v1/files/retrieve?file_id="+file_id
		headers = {
			'authorization': 'Bearer ' + self.MINIMAX_API_KEY,
		}

		response = requests.request("GET", url, headers=headers)
		print(response.text)

		download_url = response.json()['file']['download_url']
		print("Video download link：" + download_url)
		with open(self.output_file_name, 'wb') as f:
			f.write(requests.get(download_url).content)
		print("THe video has been downloaded in："+os.getcwd()+'/'+self.output_file_name)


# video_generator = VideoGenerator()

# task_id = video_generator.invoke_video_generation("h")
# print("-----------------Video generation task submitted -----------------")
# while True:
#     time.sleep(10)

#     file_id, status = video_generator.query_video_generation(task_id)
#     if file_id != "":
#         video_generator.fetch_video_result(file_id)
#         print("---------------Successful---------------")
#         break
#     elif status == "Fail" or status == "Unknown":
#         print("---------------Failed---------------")
#         break

		
	



