def build_prompt(requirements, kpis, contexts):
    context_text = "\n".join(
        f"- {c['description']} | KPIs: {c['kpis']} | Stack: {c['tech_stack']}"
        for c in contexts
    )

    return f"""
        You are a senior architect.
        Given the business requirements and KPIs, recommend a tech stack.

        Requirements: {requirements}
        KPIs: {kpis}

        Past successful solutions:
        {context_text}

        Respond with:
        1. Recommended Architecture
        2. Justification
        3. Trade-offs
        """