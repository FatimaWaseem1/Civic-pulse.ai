import json
from typing import Dict, Any, List
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import HumanMessage, SystemMessage


class PolicySimulationEngine:
    # Changed default model to gemini-1.5-flash (or gemini-2.0-flash)
    def __init__(self, model_name: str = "gemini-1.5-flash"):
        self.llm = ChatGoogleGenerativeAI(model=model_name, temperature=0.2)

    def run_simulation(self, bill_text: str) -> Dict[str, Any]:
        """Runs multi-agent stress test on proposed policy text."""
        personas = {
            "SME_Representative": "You are a small business advocate analyzing tax, compliance, and operational burdens.",
            "Economist": "You are a macroeconomist evaluating inflation, job creation, and GDP impact.",
            "Local_Council_Leader": "You are a regional council leader focused on housing, infrastructure, and local services."
        }

        results = {}
        logs = []

        for agent_name, system_prompt in personas.items():
            messages = [
                SystemMessage(content=system_prompt),
                HumanMessage(
                    content=f"Evaluate this policy snippet and respond ONLY with valid JSON containing 'score' (0-100) and 'rationale' (1 sentence):\n{bill_text}")
            ]
            response = self.llm.invoke(messages)

            clean_content = response.content.replace("```json", "").replace("```", "").strip()

            try:
                parsed = json.loads(clean_content)
                results[agent_name] = float(parsed.get("score", 50.0))
                logs.append({"agent": agent_name, "rationale": parsed.get("rationale", "")})
            except Exception:
                results[agent_name] = 50.0
                logs.append({"agent": agent_name, "rationale": clean_content[:100]})

        avg_score = sum(results.values()) / len(results) if results else 0.0
        return {
            "aggregate_impact_score": round(avg_score, 1),
            "breakdown": results,
            "logs": logs
        }