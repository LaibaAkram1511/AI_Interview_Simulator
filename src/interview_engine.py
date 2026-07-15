import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.prompts import PromptTemplate

from src.prompts import QUESTION_PROMPT, FEEDBACK_PROMPT, FINAL_REPORT_PROMPT

load_dotenv()


def get_llm():
    return ChatGroq(
        groq_api_key=os.getenv("GROQ_API_KEY"),
        model_name="llama-3.1-8b-instant",
        temperature=0.3
    )


def generate_question(profile, role, experience, interview_type, question_number):
    llm = get_llm()

    prompt = PromptTemplate(
        input_variables=[
            "candidate_name", "field", "qualification", "skills",
            "role", "experience", "interview_type", "question_number"
        ],
        template=QUESTION_PROMPT
    )

    chain = prompt | llm

    response = chain.invoke({
        "candidate_name": profile["full_name"],
        "field": profile["field"],
        "qualification": profile["qualification"],
        "skills": profile["skills"],
        "role": role,
        "experience": experience,
        "interview_type": interview_type,
        "question_number": question_number
    })

    return response.content


def generate_feedback(role, experience, interview_type, question, answer):
    llm = get_llm()

    prompt = PromptTemplate(
        input_variables=["role", "experience", "interview_type", "question", "answer"],
        template=FEEDBACK_PROMPT
    )

    chain = prompt | llm

    response = chain.invoke({
        "role": role,
        "experience": experience,
        "interview_type": interview_type,
        "question": question,
        "answer": answer
    })

    return response.content


def generate_final_report(profile, role, experience, interview_type, interview_data):
    llm = get_llm()

    prompt = PromptTemplate(
        input_variables=[
            "candidate_name", "field", "qualification", "skills",
            "role", "experience", "interview_type", "interview_data"
        ],
        template=FINAL_REPORT_PROMPT
    )

    chain = prompt | llm

    response = chain.invoke({
        "candidate_name": profile["full_name"],
        "field": profile["field"],
        "qualification": profile["qualification"],
        "skills": profile["skills"],
        "role": role,
        "experience": experience,
        "interview_type": interview_type,
        "interview_data": interview_data
    })

    return response.content