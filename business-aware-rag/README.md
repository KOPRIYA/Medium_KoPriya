# Business-Aware Tech Stack RAG Based Recommender (using Python and Java)

## Overview

This project is a production-oriented Retrieval-Augmented Generation (RAG) system designed to recommend **technology stacks and system architectures** based on **business requirements and KPIs**, rather than novelty or trends.

The system treats AI as **decision support**, not decision replacement. It retrieves relevant historical solutions, grounds recommendations in past success, and produces transparent, trade-off-aware outputs.

---

## Problem Statement

Engineering teams often select technologies based on trends, familiarity, or ad-hoc preferences. This leads to:

- Misalignment with business goals
- Over-engineered systems
- Higher long-term maintenance cost

This project answers a different question:
Given business requirements and KPIs, what technology stack has historically worked—and why?
Input: Product requirements + KPIs
Output: Recommended tech stack & architecture

---

## High-level Architecture

User Input
↓
Embedding + Retrieval (Vector DB)
↓
Context Assembly (Top-K past solutions)
↓
LLM Reasoning (Business-aware prompt)
↓
Validated Recommendation (Tech + Architecture)
