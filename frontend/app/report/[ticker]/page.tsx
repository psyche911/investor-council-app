import { getReport } from '../../actions';
import ReactMarkdown from 'react-markdown';
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';
import Link from 'next/link';

interface PageProps {
    params: Promise<{
        ticker: string;
    }>;
}

export default async function ReportPage({ params }: PageProps) {
    const { ticker } = await params;
    const report = await getReport(ticker);

    if (!report) {
        return (
            <div className="min-h-screen flex items-center justify-center bg-neutral-950 text-neutral-400">
                <div className="text-center">
                    <h1 className="text-2xl font-bold mb-4">Report Not Found</h1>
                    <p className="mb-8">Could not load analysis for {ticker}.</p>
                    <Link href="/" className="px-4 py-2 bg-neutral-800 rounded hover:bg-neutral-700 transition-colors">
                        Back to Dashboard
                    </Link>
                </div>
            </div>
        );
    }

    return (
        <main className="min-h-screen bg-neutral-950 text-neutral-100 p-8">
            <div className="max-w-4xl mx-auto">
                <nav className="mb-8">
                    <Link href="/" className="text-amber-400 hover:text-amber-300 transition-colors flex items-center gap-2">
                        &larr; Back to Dashboard
                    </Link>
                </nav>

                <article className="prose prose-invert prose-amber max-w-none">
                    <ReactMarkdown
                        remarkPlugins={[remarkMath]}
                        rehypePlugins={[rehypeKatex]}
                        components={{
                            h1: ({ node, ...props }) => <h1 className="text-4xl font-bold bg-gradient-to-r from-amber-200 to-yellow-400 bg-clip-text text-transparent mb-8" {...props} />,
                            h2: ({ node, ...props }) => <h2 className="text-2xl font-semibold border-b border-neutral-800 pb-2 mt-12 mb-6 text-amber-100" {...props} />,
                            h3: ({ node, ...props }) => <h3 className="text-xl font-medium text-amber-200 mt-8 mb-4" {...props} />,
                            strong: ({ node, ...props }) => <strong className="text-amber-400 font-semibold" {...props} />,
                            blockquote: ({ node, ...props }) => <blockquote className="border-l-4 border-amber-500/50 pl-4 italic text-neutral-400 my-6" {...props} />,
                            li: ({ node, ...props }) => <li className="my-1" {...props} />,
                        }}
                    >
                        {report}
                    </ReactMarkdown>
                </article>
            </div>
        </main>
    );
}
