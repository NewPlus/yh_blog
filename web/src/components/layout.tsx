import { cn } from "@/lib/utils"
import Link from "next/link"

export default function Layout({ children }: { children: React.ReactNode }) {
  return (
    <div className="min-h-screen bg-background">
      <header className="border-b">
        <div className="container flex h-16 items-center px-4">
          <Link href="/" className="flex items-center space-x-2">
            <span className="text-xl font-bold">Yonghwan Lee</span>
          </Link>
          <nav className="ml-auto flex gap-6">
            <Link 
              href="/blog"
              className={cn(
                "text-sm font-medium transition-colors hover:text-primary"
              )}
            >
              Blog
            </Link>
            <Link
              href="/portfolio"
              className={cn(
                "text-sm font-medium transition-colors hover:text-primary"
              )}
            >
              Portfolio
            </Link>
          </nav>
        </div>
      </header>
      <main className="container mx-auto px-4 py-8">
        {children}
      </main>
    </div>
  )
}

