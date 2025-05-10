"use client"

import { z } from "zod"
import { useForm } from "react-hook-form"
import { Button } from "@/components/ui/button"
import {
  Form,
  FormControl,
  FormDescription,
  FormField,
  FormItem,
  FormLabel,
  FormMessage,
} from "@/components/ui/form"
import { Input } from "@/components/ui/input"
import { zodResolver } from "@hookform/resolvers/zod"
import { useState } from "react"

const formSchema = z.object({
  prompt: z.string().min(10, {
    message: "Prompt must be at least 10 characters long"
  })
})

export function SubmissionForm() {
  const [storyPreview, setStoryPreview] = useState<string | null>(null);
  const [isLoading, setIsLoading] = useState(false);

  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      prompt: "",
    },
  })

  async function onSubmit(values: z.infer<typeof formSchema>) {
    setIsLoading(true)
    console.log(values)
    const query = encodeURIComponent(values.prompt)

    try {
      const response = await fetch(`http://localhost:5000/api/createvideo?prompt=${query}`, {
        method: "GET",
      })

      if (!response.ok) {
        throw new Error("Failed to fetch from backend")
      }

      const data = await response.json()
      console.log("Response from backend:", data)
      setStoryPreview(data.summary)
      console.log("STORY PREVIEW: ",storyPreview)
    } catch (error) {
      console.error("Error during fetch:", error)
    } finally {
      setIsLoading(false)
    }
  }
  
  return (
    <div className="p-6 rounded-lg shadow-md bg-white border border-gray-100 max-w-xl mx-auto">
      <h2 className="text-2xl font-bold mb-6 text-center text-gray-800">Create Your Video</h2>
      <Form {...form}>
        <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-6">
          <FormField
            control={form.control}
            name="prompt"
            render={({ field }) => (
              <FormItem>
                <FormLabel className="text-md font-medium">Video Prompt To Be Created:</FormLabel>
                <FormControl>
                  <Input 
                    placeholder="Narrate to your heart's content" 
                    className="p-3 rounded-md border-gray-300 focus:border-blue-500 focus:ring-2 focus:ring-blue-200 transition-all"
                    {...field} 
                  />
                </FormControl>
                <FormDescription className="text-sm text-gray-500 italic">
                  Ex: "I want a love story between a tiger and a lioness"
                </FormDescription>
                <FormMessage className="text-red-500" />
              </FormItem>
            )}
          />
          <div className="flex justify-center mt-6">
            <Button 
              type="submit" 
              className="px-6 py-3 bg-gradient-to-r from-blue-500 to-indigo-600 hover:from-blue-600 hover:to-indigo-700 text-white font-medium rounded-md shadow-sm hover:shadow transition-all duration-200"
            >
              Create your video!
            </Button>
          </div>
        </form>
      </Form>
    </div>
  )
}