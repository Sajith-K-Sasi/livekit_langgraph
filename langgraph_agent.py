from typing import Annotated, TypedDict
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI

from langgraph.graph.message import add_messages,AnyMessage
from langgraph.graph import START, END, StateGraph

load_dotenv()

class State(TypedDict):
    messages: Annotated[list[AnyMessage], add_messages]

def chat_node(state: State) -> State:
    model = ChatOpenAI(model_name="gpt-4o-mini", temperature=0.7)
    state["messages"] = model.invoke(state["messages"])
    return state

def create_workflow():
    graph_builder = StateGraph(State)
    graph_builder.add_node("chat_node", chat_node)
    graph_builder.add_edge(START, "chat_node")
    graph_builder.add_edge("chat_node", END)
    graph = graph_builder.compile()
    return graph    

if __name__ == "__main__":
    graph = create_workflow()
    response = graph.invoke({"messages": ["Hello, how are you?"]})
    print(response["messages"][-1].content)
