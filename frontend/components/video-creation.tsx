"use client"

import { useState } from "react"

interface VideoCreationProps {
  storyData: any;
}

export function VideoCreation({ storyData }: VideoCreationProps) {
  const [isGenerating, setIsGenerating] = useState(false);

  const handleGenerateVideo = () => {
    setIsGenerating(true);
    // Mock video generation process
    setTimeout(() => {
      setIsGenerating(false);
      alert("Video generation coming soon!");
    }, 1500);
  };

  return (
    <div className="flex flex-col p-6 rounded-lg shadow-md bg-white border border-gray-100 h-fit">
      <h2 className="text-2xl font-bold mb-6 text-center text-gray-800">Video Creation</h2>
      
      {storyData ? (
        <div className="space-y-4">
          <p className="text-gray-700">Your story has been created! Ready to generate a video?</p>
          
          <button 
            className={`w-full py-3 bg-gradient-to-r ${
              isGenerating 
                ? "from-yellow-500 to-yellow-600" 
                : "from-green-500 to-emerald-600 hover:from-green-600 hover:to-emerald-700"
            } text-white font-medium rounded-md shadow-sm hover:shadow transition-all duration-200`}
            onClick={handleGenerateVideo}
            disabled={isGenerating}
          >
            {isGenerating ? "Generating..." : "Generate Video"}
          </button>
          
          {/* Future video preview area */}
          {/* <div className="mt-6 border rounded-md p-4 bg-slate-50">
            <p className="text-center text-gray-500">Video preview will appear here</p>
          </div> */}
        </div>
      ) : (
        <p className="text-gray-500 italic text-center">Create a story first to generate a video...</p>
      )}
    </div>
  );
} 