Agentic AI Course-Planner
Overview

A multi-agent system that automates semester course selection for IIT Bombay undergraduates. From a student's CPI, academic standing and interests, it produces a registration plan that is clash-free, credit-compliant and personalised. It was built with LangChain, LangGraph, RAG and Google Gemini.

The Problem

From their second year, IITB students can take courses beyond the core curriculum: HASMED electives, institute electives, department electives and minors. Finalising a choice on the ASC portal usually means:

Spending hours browsing courses across all departments
Discovering slot clashes only after shortlisting
Hitting credit limits that depend on academic category
Finding that a course counts as an elective rather than a minor, or that prerequisites are missing
System Architecture

The planner is a sequential LangGraph pipeline in which five agents share a common StudentState object:

Student Input → Rulebook Validator → Eligibility → Candidate Generator → Ranking → Planner → Final Plan
Data layer
database.py holds every Semester 3 compulsory course plus all HASMED, institute, department and minor electives. Each entry stores code, title, credits, department, category, time slot, full or half-semester offering, and interest tags for semantic matching. It covers every department, including Policy Studies and Climate Studies.
timetable.py encodes the actual IITB 2025-26 slot timetable, so clash detection (can_add_course) and credit calculation use real data.
rag.py indexes the UG Rulebook and retrieves only the sections relevant to registration. Because rules are retrieved rather than hardcoded, a new rulebook can replace the old one without touching any code.
Agents

1. Rulebook Validator Agent (RAG + Gemini)
Takes the student's CPI and academic history (outstanding FR/DX/DR/W grades in core courses, FR/DX credits, credits earned in the previous two semesters, non-core FR/DX count). It retrieves the relevant rulebook sections and has Gemini determine the academic category (I-VI), maximum and minimum credits, and important registration remarks. The prompt restricts Gemini to the retrieved text and states that Category VI supersedes all others. If the output can't be parsed, safe defaults are used and the problem is flagged.

2. Eligibility Agent
Validates the requested credit load against the rulebook output. If the request exceeds the category maximum, it is automatically capped and the student is told why. Loads below the minimum are flagged as needing Faculty Advisor approval. Loads below the compulsory credit total are marked ineligible.

3. Candidate Generator Agent
Builds the pool of recommendable electives from the course database. It excludes courses that are already compulsory for the semester and sorts the rest by credits and course code.

4. Ranking Agent (Gemini)
Instead of keyword matching, Gemini reads each candidate's title and tags and judges semantic relevance (for example, AI maps to Machine Learning, Computer Vision and NLP, and Finance maps to Financial Engineering and Economics). It returns up to 15 courses, each with a 0-100 relevance score and a one-line justification.

Safeguards include:

A prompt that requires a strong, direct academic link and gives explicit negative examples to prevent speculative matches
Hallucination filtering: every returned course code is checked against the local database, and unknown codes are discarded
Three retries with JSON cleanup if the LLM call or parse fails
Graceful degradation: if Gemini fails, finds nothing relevant or returns only invalid codes, the system tells the student and continues with the compulsory courses only
A fallback "broadly useful electives" mode when the student gives no interests

5. Planner Agent
Starts from the compulsory courses and adds ranked electives one at a time. Before accepting each course it checks:

Credit limit: the addition must not exceed the planning target
Slot clash: it must not clash with already-selected courses
Duplicates: it must not already be in the plan

Rejected courses are recorded with reasons, and when a course is rejected for a clash, the planner suggests the next-best non-clashing alternative. Every decision is written to a decision log, so the final output explains why each course was selected or rejected. The final summary includes registered and remaining credits, clashes, alternatives and remarks.

Special case: Category VI. The UG rules don't say which compulsory courses should be deferred for students in the Academic Rehabilitation Programme, so the planner deliberately does not auto-plan. It states the credit cap and directs the student to their Faculty Advisor and the Department UG Committee.

Key Design Decisions
RAG over hardcoding: rules live in the rulebook document, so updates need no code changes.
LLM for judgment, code for constraints: Gemini handles semantic ranking and rule interpretation, while slot clashes, credit arithmetic and duplicate checks are deterministic Python. The LLM can't produce an invalid timetable.
Validate everything the LLM returns: course codes are verified against the database before use.
Transparency: scores, reasons, rejection causes and the decision log make the output auditable.
Fail safe: every failure mode falls back to a valid compulsory-only plan with an explanation.
Tech Stack

Python · LangChain · LangGraph · Google Gemini · RAG (vector retrieval over the UG Rulebook) · .env-based API key configuration · CLI via app.py

Usage

Add your Gemini API key to .env, run app.py, enter your CPI, academic standing details, target credits and interests, and receive a complete semester plan.
