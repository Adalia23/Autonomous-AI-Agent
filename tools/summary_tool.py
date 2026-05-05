from langchain_core.tools import tool

@tool
def summary_tool(text: str) -> str:
    """Summarize a long piece of text into key bullet points."""
    sentences = text.split('. ')
    if len(sentences) <= 3:
        return text
    summary = "Key points:\n"
    for i, sentence in enumerate(sentences[:5]):
        if sentence.strip():
            summary += f"• {sentence.strip()}\n"
    return summary