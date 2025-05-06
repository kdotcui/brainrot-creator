import { SubmissionForm } from "@/components/submission-form";

export default function Home() {
  return (
    <div className="flex h-screen">
      <div className="w-1/2">
        <SubmissionForm />
      </div>
      <div className="w-1/2"></div>
    </div>
  );
}
