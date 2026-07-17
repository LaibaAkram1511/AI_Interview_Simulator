import streamlit as st
from streamlit_mic_recorder import mic_recorder

from src.speech_to_text import convert_audio_to_text
from src.interview_engine import (
    generate_question,
    generate_feedback,
    generate_final_report
)
from src.scoring import calculate_average_scores
from src.report_generator import create_downloadable_report


st.set_page_config(
    page_title="AI Interview Simulator",
    page_icon="🎤",
    layout="wide"
)


# ---------------- SESSION ----------------

defaults = {
    "logged_in": True,
    "user": {
        "full_name": "Demo Candidate",
        "email": "demo@example.com"
    },
    "profile_completed": False,
    "profile": {},
    "started": False,
    "question_number": 1,
    "current_question": "",
    "interview_data": [],
    "feedback_list": [],
    "final_report": ""
}


for key, value in defaults.items():
    if key not in st.session_state:
        st.session_state[key] = value



# ---------------- STYLE ----------------

st.markdown("""
<style>

.main-title {
    font-size:38px;
    font-weight:800;
}

.card {
    background:white;
    padding:25px;
    border-radius:16px;
    box-shadow:0px 4px 18px rgba(0,0,0,0.08);
}

.profile-box {
    background:linear-gradient(135deg,#1f2937,#111827);
    color:white;
    padding:18px;
    border-radius:14px;
}

</style>
""", unsafe_allow_html=True)



# ---------------- LOGOUT ----------------

def logout():

    st.session_state.logged_in = False
    st.session_state.profile_completed = False
    st.session_state.profile = {}

    st.rerun()



# ---------------- HEADER ----------------

top_left, top_right = st.columns([3,1])


with top_left:

    st.markdown(
        '<div class="main-title">🎤 AI Interview Simulator</div>',
        unsafe_allow_html=True
    )

    st.write(
        "Practice interviews with personalized AI feedback."
    )


with top_right:

    st.markdown(
        f"""
        <div class="profile-box">
        👤 <b>{st.session_state.user['full_name']}</b><br>
        {st.session_state.user['email']}
        </div>
        """,
        unsafe_allow_html=True
    )


    if st.button("Logout"):
        logout()



# ---------------- PROFILE ----------------


if not st.session_state.profile_completed:


    st.subheader("Complete Candidate Profile")


    field = st.text_input(
        "Your Field",
        placeholder="Software Engineering, AI, Data Science"
    )


    qualification = st.text_input(
        "Qualification",
        placeholder="BS Software Engineering"
    )


    experience_level = st.selectbox(
        "Experience Level",
        [
            "Student",
            "Fresher",
            "0-1 Year",
            "1-3 Years",
            "3-5 Years"
        ]
    )


    skills = st.text_area(
        "Skills",
        placeholder="Python, AI, ML, SQL"
    )


    target_role = st.text_input(
        "Target Role",
        placeholder="AI Intern"
    )


    linkedin = st.text_input(
        "LinkedIn Profile URL"
    )


    portfolio = st.text_input(
        "GitHub / Portfolio URL"
    )



    if st.button("Save Profile"):


        if not field or not qualification or not skills or not target_role:

            st.warning(
                "Please fill required fields."
            )

        else:

            st.session_state.profile = {

                "full_name":
                st.session_state.user["full_name"],

                "field": field,

                "qualification":
                qualification,

                "experience_level":
                experience_level,

                "skills": skills,

                "target_role":
                target_role,

                "linkedin":
                linkedin,

                "portfolio":
                portfolio
            }


            st.session_state.profile_completed = True


            st.success(
                "Profile saved successfully."
            )


            st.rerun()

# ---------------- INTERVIEW SECTION ----------------


else:

    profile = st.session_state.profile


    with st.sidebar:

        st.header("Interview Setup")


        st.markdown(f"""
        **Candidate:** {profile['full_name']}

        **Field:** {profile['field']}

        **Qualification:** {profile['qualification']}

        **Experience:** {profile['experience_level']}
        """)



        role = st.selectbox(
            "Target Role",
            [
                profile["target_role"],
                "AI Intern",
                "Python Developer",
                "Data Analyst",
                "Machine Learning Engineer",
                "Software Engineer",
                "Frontend Developer",
                "Backend Developer"
            ]
        )



        experience = st.selectbox(
            "Interview Experience Level",
            [
                "Student",
                "Fresher",
                "0-1 Year",
                "1-3 Years",
                "3-5 Years"
            ],
            index=0
        )



        interview_type = st.selectbox(
            "Interview Type",
            [
                "HR Interview",
                "Technical Interview",
                "Project-Based Interview",
                "Mixed Interview"
            ]
        )



        total_questions = st.slider(
            "Number of Questions",
            3,
            10,
            5
        )



        if st.button("Start Interview"):

            st.session_state.started = True

            st.session_state.question_number = 1

            st.session_state.interview_data = []

            st.session_state.feedback_list = []

            st.session_state.final_report = ""


            with st.spinner(
                "Generating first question..."
            ):


                st.session_state.current_question = generate_question(

                    profile,

                    role,

                    experience,

                    interview_type,

                    st.session_state.question_number
                )





    # ---------------- DASHBOARD ----------------


    if not st.session_state.started:


        st.subheader(
            "Candidate Dashboard"
        )


        c1, c2, c3 = st.columns(3)


        c1.metric(
            "Target Role",
            profile["target_role"]
        )


        c2.metric(
            "Experience",
            profile["experience_level"]
        )


        c3.metric(
            "Interview Status",
            "Not Started"
        )



        st.markdown(
            "### Profile Summary"
        )


        st.info(
f"""
Name:
{profile['full_name']}

Field:
{profile['field']}

Qualification:
{profile['qualification']}

Skills:
{profile['skills']}

LinkedIn:
{profile['linkedin']}

Portfolio:
{profile['portfolio']}
"""
        )



        st.success(
            "Start your interview from sidebar."
        )



    # ---------------- INTERVIEW ----------------


    else:


        st.subheader(
            f"Question {st.session_state.question_number} of {total_questions}"
        )


        st.markdown(
            "### Interview Question"
        )


        st.info(
            st.session_state.current_question
        )



        st.markdown(
            "### Answer Mode"
        )


        answer_mode = st.radio(

            "Choose answer method",

            [
                "Type Answer",
                "Speak Answer"
            ],

            horizontal=True
        )



        speech_text = ""



        if answer_mode == "Speak Answer":


            st.info(
                "Record your answer."
            )


            audio = mic_recorder(

                start_prompt="🎙️ Start Recording",

                stop_prompt="⏹️ Stop Recording",

                just_once=True,

                use_container_width=True,

                key=f"mic_{st.session_state.question_number}"

            )



            if audio:


                with st.spinner(
                    "Converting speech..."
                ):


                    speech_text = convert_audio_to_text(
                        audio["bytes"]
                    )


                if speech_text:

                    st.success(
                        "Speech converted successfully."
                    )


                    st.info(
                        speech_text
                    )



        user_answer = st.text_area(

            "Your Answer",

            value=speech_text,

            height=180,

            placeholder=
            "Write your answer here..."

        )



        if st.button(
            "Submit Answer"
        ):


            if not user_answer.strip():

                st.warning(
                    "Please write your answer."
                )


            else:


                with st.spinner(
                    "Evaluating answer..."
                ):


                    feedback = generate_feedback(

                        role,

                        experience,

                        interview_type,

                        st.session_state.current_question,

                        user_answer

                    )



                st.session_state.interview_data.append({

                    "question_number":
                    st.session_state.question_number,

                    "question":
                    st.session_state.current_question,

                    "answer":
                    user_answer,

                    "feedback":
                    feedback

                })



                st.session_state.feedback_list.append(
                    feedback
                )



                st.success(
                    feedback
                )





        col1, col2 = st.columns(2)



        with col1:


            if st.button(
                "Next Question"
            ):


                if st.session_state.question_number < total_questions:


                    st.session_state.question_number += 1



                    with st.spinner(
                        "Generating question..."
                    ):


                        st.session_state.current_question = generate_question(

                            profile,

                            role,

                            experience,

                            interview_type,

                            st.session_state.question_number

                        )


                    st.rerun()



                else:


                    st.warning(
                        "Interview completed. Generate report."
                    )





        with col2:


            if st.button(
                "Generate Final Report"
            ):


                if len(
                    st.session_state.interview_data
                ) == 0:


                    st.warning(
                        "Answer at least one question."
                    )



                else:


                    scores = calculate_average_scores(

                        st.session_state.feedback_list

                    )



                    interview_text = ""



                    for item in st.session_state.interview_data:


                        interview_text += f"""

Question {item['question_number']}

{item['question']}


Answer:

{item['answer']}


Feedback:

{item['feedback']}


-------------------

"""



                    with st.spinner(
                        "Generating final report..."
                    ):


                        final_report = generate_final_report(

                            profile,

                            role,

                            experience,

                            interview_type,

                            interview_text

                        )



                    st.session_state.final_report = final_report



                    st.markdown(
                        "## Final Scores"
                    )


                    c1,c2,c3,c4 = st.columns(4)


                    c1.metric(
                        "Communication",
                        f"{scores['communication']}/10"
                    )


                    c2.metric(
                        "Technical",
                        f"{scores['technical']}/10"
                    )


                    c3.metric(
                        "Confidence",
                        f"{scores['confidence']}/10"
                    )


                    c4.metric(
                        "Overall",
                        f"{scores['overall']}/10"
                    )



                    st.markdown(
                        "## Final Report"
                    )


                    st.write(
                        final_report
                    )



                    report_file = create_downloadable_report(

                        profile,

                        role,

                        experience,

                        interview_type,

                        final_report

                    )



                    st.download_button(

                        label="Download Professional Report",

                        data=report_file,

                        file_name=
                        "professional_interview_report.txt",

                        mime="text/plain"

                    )