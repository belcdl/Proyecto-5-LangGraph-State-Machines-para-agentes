"""
ETAPA 1 · Un grafo sin modelo.

Estado, nodo y aristas SIN depender de un LLM: el nodo devuelve un texto fijo.

Ejecutar:  uv run python etapas/1_grafo.py
"""

from typing_extensions import TypedDict

from langgraph.graph import END, START, StateGraph
   # print("Hola!")#

class State(TypedDict):
    text: str

def mayusculas (state: State) -> dict:
        return {"text": state["text"].upper()}

# 2. DEFINIR el grafo
builder = StateGraph(State)
builder.add_node("mayusculas", mayusculas)
builder.add_edge(START, "mayusculas")
builder.add_edge("mayusculas", END)

# 3. COMPILAR
graph = builder.compile()

# 4. EJECUTAR
resultado = graph.invoke({"text": "Hola grafo!"})
print(resultado)