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

const formSchema = z.object({
  prompt: z.string().min(10, {
    message: "Prompt must be at least 10 characters long"
  })
})

export function SubmissionForm() {
  const form = useForm<z.infer<typeof formSchema>>({
    resolver: zodResolver(formSchema),
    defaultValues: {
      prompt: "",
    },
  })

  async function onSubmit(values: z.infer<typeof formSchema>) {
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
    } catch (error) {
      console.error("Error during fetch:", error)
    }
  }
  
  return (
    <Form {...form}>
      <form onSubmit={form.handleSubmit(onSubmit)} className="space-y-8">
        <FormField
          control={form.control}
          name="prompt"
          render={({ field }) => (
            <FormItem>
              <FormLabel>Video Prompt To Be Created:</FormLabel>
              <FormControl>
                <Input placeholder="Narrate to your heart's content" {...field} />
              </FormControl>
              <FormDescription>
                We suggest having a mix of video prompts
              </FormDescription>
              <FormMessage />
            </FormItem>
          )}
        />
        <Button type="submit">Create your video!</Button>
      </form>
    </Form>
  )

}