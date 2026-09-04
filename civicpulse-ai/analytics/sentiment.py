import pandas as pd
from typing import List, Dict


class PublicSentimentAnalyzer:
    def process_feedback(self, feedback_items: List[str]) -> pd.DataFrame:
        """Clusters civic feedback and classifies priority sentiment buckets."""
        categories = ["Cost of Living", "Environmental Impact", "Healthcare Priority", "Infrastructure"]

        # Lightweight rules-based clustering pipeline
        data = []
        for idx, text in enumerate(feedback_items):
            text_lower = text.lower()
            if "cost" in text_lower or "tax" in text_lower or "price" in text_lower:
                cat = "Cost of Living"
            elif "green" in text_lower or "climate" in text_lower or "carbon" in text_lower:
                cat = "Environmental Impact"
            elif "health" in text_lower or "hospital" in text_lower:
                cat = "Healthcare Priority"
            else:
                cat = "Infrastructure"

            data.append({"Feedback_ID": f"FB-{idx + 101}", "Category": cat, "Snippet": text})

        return pd.DataFrame(data)