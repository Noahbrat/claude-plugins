#!/usr/bin/env python3
"""
Semantic memory search using Gemini embeddings.
Searches through memory/*.md files and returns relevant snippets.
"""

import os
import sys
import json
import re
from pathlib import Path
from typing import Optional

try:
    import google.generativeai as genai
except ImportError:
    print("Error: google-generativeai package not installed.")
    print("Install with: pip install google-generativeai")
    sys.exit(1)


def get_api_key() -> Optional[str]:
    """Get Gemini API key from environment or common locations."""
    # Check environment variable
    if key := os.environ.get("GEMINI_API_KEY"):
        return key
    if key := os.environ.get("GOOGLE_API_KEY"):
        return key
    
    # Check clawdbot config
    config_path = Path.home() / ".clawdbot" / "clawdbot.json"
    if config_path.exists():
        try:
            config = json.loads(config_path.read_text())
            # Check models.providers.gemini.apiKey
            if key := config.get("models", {}).get("providers", {}).get("gemini", {}).get("apiKey"):
                return key
            # Check skills.entries (for backward compat)
            for entry in config.get("skills", {}).get("entries", {}).values():
                if key := entry.get("apiKey"):
                    if key.startswith("AIza"):  # Google API key format
                        return key
        except (json.JSONDecodeError, KeyError):
            pass
    
    return None


def find_search_dirs() -> list[Path]:
    """Find memory and brain directories to search."""
    dirs = []
    cwd = Path.cwd()
    
    # Check current directory and parents for memory/ and brain/
    for parent in [cwd] + list(cwd.parents)[:5]:
        for dirname in ["memory", "brain"]:
            search_dir = parent / dirname
            if search_dir.is_dir() and search_dir not in dirs:
                dirs.append(search_dir)
    
    # Check clawd workspace as fallback
    clawd_path = Path.home() / "clawd"
    for dirname in ["memory", "brain"]:
        search_dir = clawd_path / dirname
        if search_dir.is_dir() and search_dir not in dirs:
            dirs.append(search_dir)
    
    return dirs


def chunk_text(text: str, chunk_size: int = 500, overlap: int = 100) -> list[tuple[int, int, str]]:
    """Split text into overlapping chunks. Returns (start_line, end_line, chunk_text)."""
    lines = text.split('\n')
    chunks = []
    
    current_chunk = []
    current_start = 0
    current_length = 0
    
    for i, line in enumerate(lines):
        current_chunk.append(line)
        current_length += len(line) + 1
        
        if current_length >= chunk_size:
            chunk_text = '\n'.join(current_chunk)
            chunks.append((current_start + 1, i + 1, chunk_text))  # 1-indexed lines
            
            # Keep overlap
            overlap_lines = []
            overlap_length = 0
            for j in range(len(current_chunk) - 1, -1, -1):
                if overlap_length + len(current_chunk[j]) > overlap:
                    break
                overlap_lines.insert(0, current_chunk[j])
                overlap_length += len(current_chunk[j]) + 1
            
            current_chunk = overlap_lines
            current_start = i - len(overlap_lines) + 1
            current_length = overlap_length
    
    # Don't forget the last chunk
    if current_chunk:
        chunk_text = '\n'.join(current_chunk)
        chunks.append((current_start + 1, len(lines), chunk_text))
    
    return chunks


def get_embedding(text: str) -> list[float]:
    """Get embedding vector for text using Gemini."""
    result = genai.embed_content(
        model="models/gemini-embedding-001",
        content=text,
        task_type="retrieval_document"
    )
    return result['embedding']


def get_query_embedding(text: str) -> list[float]:
    """Get embedding vector for a query using Gemini."""
    result = genai.embed_content(
        model="models/gemini-embedding-001",
        content=text,
        task_type="retrieval_query"
    )
    return result['embedding']


def cosine_similarity(a: list[float], b: list[float]) -> float:
    """Calculate cosine similarity between two vectors."""
    dot_product = sum(x * y for x, y in zip(a, b))
    norm_a = sum(x * x for x in a) ** 0.5
    norm_b = sum(x * x for x in b) ** 0.5
    if norm_a == 0 or norm_b == 0:
        return 0.0
    return dot_product / (norm_a * norm_b)


def search_memory(query: str, memory_dir: Path, top_k: int = 5, min_score: float = 0.3) -> list[dict]:
    """Search memory files for relevant content."""
    results = []
    
    # Get query embedding
    query_embedding = get_query_embedding(query)
    
    # Process each markdown file
    for md_file in memory_dir.glob("*.md"):
        content = md_file.read_text()
        chunks = chunk_text(content)
        
        for start_line, end_line, text in chunks:
            # Get chunk embedding
            chunk_embedding = get_embedding(text)
            
            # Calculate similarity
            score = cosine_similarity(query_embedding, chunk_embedding)
            
            if score >= min_score:
                results.append({
                    "path": str(md_file.relative_to(memory_dir.parent)),
                    "start_line": start_line,
                    "end_line": end_line,
                    "score": score,
                    "snippet": text[:500] + ("..." if len(text) > 500 else "")
                })
    
    # Sort by score and return top results
    results.sort(key=lambda x: x["score"], reverse=True)
    return results[:top_k]


def main():
    if len(sys.argv) < 2:
        print("Usage: recall.py <query>")
        print("Example: recall.py 'how to deploy to production'")
        sys.exit(1)
    
    query = " ".join(sys.argv[1:])
    
    # Get API key
    api_key = get_api_key()
    if not api_key:
        print("Error: No Gemini API key found.")
        print("Set GEMINI_API_KEY environment variable or configure in ~/.clawdbot/clawdbot.json")
        sys.exit(1)
    
    genai.configure(api_key=api_key)
    
    # Find directories to search (memory/ and brain/)
    search_dirs = find_search_dirs()
    if not search_dirs:
        print("Error: Could not find memory/ or brain/ directory.")
        print("Make sure you're in a workspace with a memory/ or brain/ folder.")
        print("Run /brain:setup to configure iCloud sync.")
        sys.exit(1)
    
    print(f"🔍 Searching for: {query}")
    print(f"📁 Searching in: {', '.join(str(d) for d in search_dirs)}")
    print()
    
    results = []
    checked_memory_md = set()
    
    # Search each directory
    for search_dir in search_dirs:
        dir_results = search_memory(query, search_dir)
        results.extend(dir_results)
        
        # Also check for MEMORY.md in parent (but only once per parent)
        memory_md = search_dir.parent / "MEMORY.md"
        if memory_md.exists() and str(memory_md) not in checked_memory_md:
            checked_memory_md.add(str(memory_md))
            content = memory_md.read_text()
            chunks = chunk_text(content)
            query_embedding = get_query_embedding(query)
            
            for start_line, end_line, text in chunks:
                chunk_embedding = get_embedding(text)
                score = cosine_similarity(query_embedding, chunk_embedding)
                
                if score >= 0.3:
                    results.append({
                        "path": "MEMORY.md",
                        "start_line": start_line,
                        "end_line": end_line,
                        "score": score,
                        "snippet": text[:500] + ("..." if len(text) > 500 else "")
                    })
    
    # Sort all results and take top 5
    results.sort(key=lambda x: x["score"], reverse=True)
    results = results[:5]
    
    if not results:
        print("No relevant results found.")
        return
    
    print(f"Found {len(results)} relevant result(s):\n")
    
    for i, result in enumerate(results, 1):
        print(f"### Result {i} — {result['path']} (lines {result['start_line']}-{result['end_line']}) — Score: {result['score']:.2f}")
        print()
        print(result['snippet'])
        print()
        print("---")
        print()


if __name__ == "__main__":
    main()
