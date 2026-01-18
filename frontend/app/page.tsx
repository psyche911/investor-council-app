import Link from 'next/link';
import { getAnalysisList } from './actions';

export default async function Home() {
  const analyses = await getAnalysisList();

  return (
    <main className="min-h-screen bg-neutral-950 text-neutral-100 p-8">
      <div className="max-w-4xl mx-auto">
        <header className="mb-12">
          <h1 className="text-4xl font-bold bg-gradient-to-r from-amber-200 to-yellow-400 bg-clip-text text-transparent mb-2">
            The Investor Council
          </h1>
          <p className="text-neutral-400">
            Legendary wisdom applied to modern markets.
          </p>
        </header>

        <section>
          <h2 className="text-xl font-semibold mb-6 flex items-center gap-2">
            <span className="w-2 h-8 bg-amber-500 rounded-full"></span>
            Available Analyses
          </h2>

          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
            {analyses.length === 0 ? (
              <p className="text-neutral-500 italic">No analyses found. Run the backend to generate reports.</p>
            ) : (
              analyses.map((ticker) => (
                <Link
                  key={ticker}
                  href={`/report/${ticker}`}
                  className="group block p-6 rounded-xl bg-neutral-900 border border-neutral-800 hover:border-amber-500/50 transition-all hover:bg-neutral-800/50"
                >
                  <div className="flex justify-between items-start mb-4">
                    <span className="text-2xl font-bold text-white group-hover:text-amber-400 transition-colors">
                      {ticker}
                    </span>
                    <span className="text-xs font-medium px-2 py-1 rounded bg-neutral-800 text-neutral-400 group-hover:bg-amber-900/30 group-hover:text-amber-200 transition-colors">
                      Report Ready
                    </span>
                  </div>
                  <div className="text-sm text-neutral-500 group-hover:text-neutral-300">
                    Click to view council insights &rarr;
                  </div>
                </Link>
              ))
            )}
          </div>
        </section>
      </div>
    </main>
  );
}
