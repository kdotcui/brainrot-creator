"use client"

import { SubmissionForm } from "@/components/submission-form";
import { VideoCreation } from "@/components/video-creation";
import { useState } from "react"

export default function Home() {
  const [storyData, setStoryData] = useState<any>(null);

  const handleRawDataReceived = (data: any) => {
    setStoryData(data);
    console.log("Raw story data received in home page:", data);
  };

  return (
    <div className="min-h-screen bg-gradient-to-b from-gray-50 to-gray-100">
      <header className="py-6 bg-white shadow-sm">
        <div className="container mx-auto px-4">
          <h1 className="text-3xl font-bold text-center text-gray-800">Video Creator</h1>
          <p className="text-center text-gray-600 mt-2">Transform your ideas into amazing videos</p>
        </div>
      </header>
      
      <main className="container mx-auto px-4 py-12">
        <div className="flex flex-col md:flex-row gap-8">
          {/* Left Column - Story Creation */}
          <div className="w-full md:w-1/2">
            <SubmissionForm onRawDataReceived={handleRawDataReceived} />
          </div>
          
          {/* Right Column - Video Creation */}
          <div className="w-full md:w-1/2">
            <VideoCreation storyData={storyData} />
          </div>
        </div>
      </main>
    </div>
  );
}
