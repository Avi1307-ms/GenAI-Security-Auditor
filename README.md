# GenAI Security Auditor

An agentic AI + RAG + DevSecOps GitHub Action that reviews Pull Requests for security issues and suggests fixes with human-in-the-loop approval.

## Status
Phase 1: repository setup (in progress)

## Planned Architecture
- GitHub Actions pipeline (SonarQube + Trivy scans)
- Multi-agent analysis (Detective, Engineer, Analyst)
- RAG over OWASP guidelines
- Human-in-the-loop fixes via ChatOps