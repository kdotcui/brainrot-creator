"use client"

import { SubmissionForm } from "@/components/submission-form";
import { useState } from "react"

export default function Home() {
  const [storySummary, setStorySummary] = useState<string | null>(null);

  const handleStoryGenerated = (summary: string) => {
    setStorySummary(summary);
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
          <div className="w-full md:w-1/2">
            <SubmissionForm onStoryGenerated={handleStoryGenerated} />
          </div>
          <div className="w-full md:w-1/2 flex flex-col p-6 rounded-lg shadow-md bg-white border border-gray-100 max-w-xl mx-auto">
            <h2 className="text-2xl font-bold mb-6 text-center text-gray-800">Story Summary</h2>
            {storySummary ? (
              <p className="text-gray-700 leading-relaxed">{storySummary}</p>
            ) : (
              <p className="text-gray-500 italic text-center">Your story summary will appear here...</p>
            )}
          </div>
        </div>
      </main>
    </div>
  );
}
