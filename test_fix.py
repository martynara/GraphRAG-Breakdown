#!/usr/bin/env python3
"""
Test script for the GraphRAG Unicode encoding fix.

This script demonstrates how to use the corrected query_graphrag function
that handles UTF-8 encoding properly on Windows systems.
"""

from graphrag_utils import query_graphrag

def test_polish_query():
    """Test GraphRAG with a Polish language query."""
    
    # Polish query that was causing Unicode issues
    polish_query = "Jakie różnice pokoleniowe występują w zakresie korzystania z funkcjonalności bankowości mobilnej i jakie czynniki technologiczne oraz społeczne je warunkują?"
    
    print("Testing GraphRAG with Polish query...")
    print(f"Query: {polish_query}")
    print("-" * 80)
    
    try:
        # Test local search
        print("Running local search...")
        result = query_graphrag(
            query=polish_query,
            method="local",
            root_path="ragtest",
            community_level=2
        )
        print("✅ Local search successful!")
        print("Result preview:", result[:200] + "..." if len(result) > 200 else result)
        print("-" * 80)
        
        # Test global search
        print("Running global search...")
        result = query_graphrag(
            query=polish_query,
            method="global",
            root_path="ragtest",
            community_level=2
        )
        print("✅ Global search successful!")
        print("Result preview:", result[:200] + "..." if len(result) > 200 else result)
        
    except Exception as e:
        print(f"❌ Error occurred: {e}")
        print("\nIf you're still getting errors, make sure:")
        print("1. GraphRAG is properly installed (pip install graphrag)")
        print("2. Your ragtest directory is properly set up")
        print("3. You have run 'graphrag index' to build the knowledge graph")

if __name__ == "__main__":
    test_polish_query() 