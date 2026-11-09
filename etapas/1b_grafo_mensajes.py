from typing import Annotated

from typing_extensions import TypedDict
from langchain_core.messages import AIMessage, AnyMessage, HumanMessage
from langgraph.graph import END, START, StateGraph
from langgraph.graph.message import add_messages


class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]
    tool_count: int
    errores: list[str]

def responder(state: State) -> dict:
    return {"messages": [AIMessage(content="Hola, soy el asistente de soporte. ¿En qué puedo ayudarte?")]}

builder = StateGraph(State)
builder.add_node("responder", responder)
builder.add_edge(START, "responder")
builder.add_edge("responder", END)

graph = builder.compile()

resultado = graph.invoke(
    {"messages": [HumanMessage(content="Hola")], "tool_count": 0, "errores": []}
)

for mensaje in resultado["messages"]:
    print(f"{mensaje.type}: {mensaje.content}")
    