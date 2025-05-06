# BrainRot Creator

A web application that generates cinematic tiktok/reels/shorts type videos using the greatest Chinese developments in AI technology to accelerate the brain degredation of the American Youth (joke). 

## Overview

BrainRot Creator lets you generate 45-second video narratives with emotional scenes based on your text prompts. The application uses DeepSeek's AI to create structured stories with distinct scenes. We then use MiniMax to generate an accompanying video for each scene. End result is a video that 

## Features

- Simple user interface for entering video prompts
- AI-powered story generation with multiple scenes
- Structured output with scene descriptions and durations
- Quick processing and response

## Project Structure

- `frontend/`: Next.js web application
- `backend/`: Python Quart API server

## Prerequisites

- Node.js 18+ and npm/pnpm
- Python 3.8+
- DeepSeek API key

## Setup and Installation

### Backend Setup

1. Navigate to the backend directory:
   ```
   cd backend
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the backend directory with your API key:
   ```
   DEEPSEEK_API_KEY=your_api_key_here
   ```

### Frontend Setup

1. Navigate to the frontend directory:
   ```
   cd frontend
   ```

2. Install dependencies:
   ```
   pnpm install
   ```

## Running the Application

### Start the Backend

1. From the backend directory with the virtual environment activated:
   ```
   python app.py
   ```
   The backend server will start at http://localhost:5000

### Start the Frontend

1. From the frontend directory:
   ```
   pnpm dev
   ```
   The frontend will be available at http://localhost:3000

## Usage

1. Open http://localhost:3000 in your browser
2. Enter a creative prompt in the text field
3. Click "Create your video!" to generate a story
4. View the AI-generated narrative with multiple scenes

## API Endpoints

- `GET /api/test` - Test if the backend is running
- `GET /api/createvideo?prompt=your_prompt_here` - Generate a video script based on the prompt

## Technologies Used

- **Frontend**: Next.js, React, TailwindCSS
- **Backend**: Python, Quart, OpenAI API
- **AI**: DeepSeek AI for narrative generation
