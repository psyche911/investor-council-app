'use server';

import fs from 'fs/promises';
import path from 'path';

const ANALYSES_DIR = path.join(process.cwd(), '..', 'analyses');

export async function getAnalysisList(): Promise<string[]> {
    try {
        const entries = await fs.readdir(ANALYSES_DIR, { withFileTypes: true });
        return entries
            .filter((dirent) => dirent.isDirectory())
            .map((dirent) => dirent.name);
    } catch (error) {
        console.error("Error reading analyses directory:", error);
        return [];
    }
}

export async function getReport(ticker: string): Promise<string | null> {
    try {
        const reportPath = path.join(ANALYSES_DIR, ticker, 'report.md');
        const content = await fs.readFile(reportPath, 'utf-8');
        return content;
    } catch (error) {
        console.error(`Error reading report for ${ticker}:`, error);
        return null;
    }
}
