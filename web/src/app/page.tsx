import Layout from "@/components/layout"
import { BlogCard } from "@/components/blog-card"

export default function Home() {
  return (
    <Layout>
      <div className="space-y-8">
        <section className="text-center space-y-4">
          <h1 className="text-4xl font-bold tracking-tighter sm:text-5xl md:text-6xl">
            Welcome to my digital space
          </h1>
          <p className="mx-auto max-w-[700px] text-muted-foreground">
            I write about design, development, and the intersection of technology and creativity.
          </p>
        </section>
        
        <section className="grid gap-6 sm:grid-cols-2 lg:grid-cols-3">
          <BlogCard
            title="2025년 AI 기술 & 디자인 융합 트렌드 예측과 전망"
            description="2025년도의 it기술 트렌드 핵심 아젠다 top 10과 함께 AI 기술 & 디자인 융합 트렌드가 촉발할 UX디자인의 변화를 예측해봅니다."
            tags={["위디엑스", "인사이트"]}
            href="/blog/ai-design-trends-2025"
          />
          {/* Add more BlogCard components as needed */}
        </section>
      </div>
    </Layout>
  )
}

