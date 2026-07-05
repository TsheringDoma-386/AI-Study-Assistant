from ai.llm import get_llm

llm = get_llm()

response = llm.invoke("Explain Artificial Intelligence in one sentence.")

print(response.content)