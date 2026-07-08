from langgraph.graph import StateGraph, START, END

from state import StudentState

from rulebook_validator import rulebook_validator_agent
from eligibility import eligibility_agent
from candidate_generator import candidate_generator_agent
from ranking_agent import ranking_agent
from planner import planner_agent

builder = StateGraph(StudentState)

builder.add_node(
    "RulebookValidator",
    rulebook_validator_agent
)

builder.add_node(
    "Eligibility",
    eligibility_agent
)

builder.add_node(
    "CandidateGenerator",
    candidate_generator_agent
)

builder.add_node(
    "RankingAgent",
    ranking_agent
)

builder.add_node(
    "Planner",
    planner_agent
)

builder.add_edge(
    START,
    "RulebookValidator"
)

builder.add_edge(
    "RulebookValidator",
    "Eligibility"
)

builder.add_edge(
    "Eligibility",
    "CandidateGenerator"
)

builder.add_edge(
    "CandidateGenerator",
    "RankingAgent"
)

builder.add_edge(
    "RankingAgent",
    "Planner"
)

builder.add_edge(
    "Planner",
    END)


graph = builder.compile()
