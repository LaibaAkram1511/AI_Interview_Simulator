# import streamlit as st
# from streamlit_mic_recorder import mic_recorder
# from src.speech_to_text import convert_audio_to_text
# # from src.interview_engine import generate_question, generate_feedback, generate_final_report
# # from src.scoring import calculate_average_scores
# from src.report_generator import create_downloadable_report


# st.set_page_config(
#     page_title="AI Interview Simulator",
#     page_icon="🎤",
#     layout="wide"
# )


# if "auth_page" not in st.session_state:
#     st.session_state.auth_page = "Login"

# if "logged_in" not in st.session_state:
#     st.session_state.logged_in = False

# if "user" not in st.session_state:
#     st.session_state.user = None

# if "profile_completed" not in st.session_state:
#     st.session_state.profile_completed = False

# if "profile" not in st.session_state:
#     st.session_state.profile = {}

# if "started" not in st.session_state:
#     st.session_state.started = False

# if "question_number" not in st.session_state:
#     st.session_state.question_number = 1

# if "current_question" not in st.session_state:
#     st.session_state.current_question = ""

# if "interview_data" not in st.session_state:
#     st.session_state.interview_data = []

# if "feedback_list" not in st.session_state:
#     st.session_state.feedback_list = []

# if "final_report" not in st.session_state:
#     st.session_state.final_report = ""

# if "signup_success_message" not in st.session_state:
#     st.session_state.signup_success_message = ""


# st.markdown("""
# <style>
# .main-title {
#     font-size: 38px;
#     font-weight: 800;
# }
# .card {
#     background: #ffffff;
#     padding: 25px;
#     border-radius: 16px;
#     box-shadow: 0px 4px 18px rgba(0,0,0,0.08);
#     margin-bottom: 20px;
# }
# .profile-box {
#     background: linear-gradient(135deg, #1f2937, #111827);
#     color: white;
#     padding: 18px;
#     border-radius: 14px;
# }
# </style>
# """, unsafe_allow_html=True)


# def logout():
#     st.session_state.logged_in = False
#     st.session_state.user = None
#     st.session_state.profile_completed = False
#     st.session_state.profile = {}
#     st.session_state.started = False
#     st.rerun()


# # if not st.session_state.logged_in:
# #     st.markdown('<div class="main-title">🎤 AI Interview Simulator</div>', unsafe_allow_html=True)
# #     st.write("Professional AI-powered interview preparation platform.")

# #     auth_choice = st.radio(
# #         "Choose Option",
# #         ["Login", "Signup"],
# #         horizontal=True,
# #         index=0 if st.session_state.auth_page == "Login" else 1
# #     )

# #     st.session_state.auth_page = auth_choice

# #     if st.session_state.signup_success_message:
# #         st.success(st.session_state.signup_success_message)
# #         st.session_state.signup_success_message = ""

# #     if auth_choice == "Signup":
# #         st.subheader("Create Account")

# #         with st.form("signup_form", clear_on_submit=True):
# #             full_name = st.text_input("Full Name")
# #             email = st.text_input("Email")
# #             password = st.text_input("Password", type="password")

# #             signup_btn = st.form_submit_button("Signup")

# #             if signup_btn:
# #                 if not full_name or not email or not password:
# #                     st.warning("Please fill all fields.")
# #                 else:
# #                     success, message = signup_user(full_name, email, password)
# #                     if success:
# #                         st.session_state.auth_page = "Login"
# #                         st.session_state.signup_success_message = "Account created successfully. Please login now."
# #                         st.rerun()
# #                     else:
# #                         st.error(message)

# #     else:
# #         st.subheader("Login")

# #         with st.form("login_form"):
# #             email = st.text_input("Email")
# #             password = st.text_input("Password", type="password")

# #             login_btn = st.form_submit_button("Login")

# #              if login_btn:
# #             #     user, message = login_user(email, password)

# #                  if user:
# #                      st.session_state.logged_in = True
# #             #         st.session_state.user = {
# #             #             "id": user.id,
# #             #             "full_name": user.full_name,
# #             #             "email": user.email
# #             #         }
# #             #         st.rerun()
# #                  else:
# #                      st.error(message)


# # else:
# #     top_left, top_right = st.columns([3, 1])

# if not st.session_state.logged_in:
#     st.session_state.logged_in = True
#     st.session_state.user = {
#         "full_name": "Demo Candidate",
#         "email": "demo@example.com"
#     }
#     st.rerun()

#     with top_left:
#         st.markdown('<div class="main-title">🎤 AI Interview Simulator</div>', unsafe_allow_html=True)
#         st.write("Practice interviews with personalized AI feedback.")

#     with top_right:
#         st.markdown(
#             f"""
#             <div class="profile-box">
#                 👤 <b>{st.session_state.user['full_name']}</b><br>
#                 {st.session_state.user['email']}
#             </div>
#             """,
#             unsafe_allow_html=True
#         )
#         if st.button("Logout"):
#             logout()

#     # db = SessionLocal()
#     # existing_profile = db.query(CandidateProfile).filter(
#     #     CandidateProfile.user_id == st.session_state.user["id"]
#     # ).first()
#     # db.close()

#     # if existing_profile and not st.session_state.profile_completed:
#     #     st.session_state.profile_completed = True
#     #     st.session_state.profile = {
#     #         "full_name": st.session_state.user["full_name"],
#     #         "field": existing_profile.field,
#     #         "qualification": existing_profile.qualification,
#     #         "experience_level": existing_profile.experience_level,
#     #         "skills": existing_profile.skills,
#     #         "target_role": existing_profile.target_role,
#     #         "linkedin": existing_profile.linkedin,
#     #         "portfolio": existing_profile.portfolio
#     #     }

#     # if not st.session_state.profile_completed:
#     #     st.subheader("Complete Candidate Profile")

#     #     st.write("Please add your details before starting the interview.")

#     #     field = st.text_input("Your Field", placeholder="Example: Software Engineering, AI, Data Science")
#     #     qualification = st.text_input("Qualification", placeholder="Example: BS Software Engineering")
#     #     experience_level = st.selectbox(
#     #         "Experience Level",
#     #         ["Student", "Fresher", "0-1 Year", "1-3 Years", "3-5 Years"]
#     #     )
#     #     skills = st.text_area("Skills", placeholder="Example: Python, Machine Learning, SQL, React")
#     #     target_role = st.text_input("Target Role", placeholder="Example: AI Intern")
#     #     linkedin = st.text_input("LinkedIn Profile URL")
#     #     portfolio = st.text_input("GitHub / Portfolio URL")

#     #     if st.button("Save Profile"):
#     #         if not field or not qualification or not skills or not target_role:
#     #             st.warning("Please fill required fields.")
#     #         else:
#     #             db = SessionLocal()

#                 # profile = CandidateProfile(
#                 #     user_id=st.session_state.user["id"],
#                 #     field=field,
#                 #     qualification=qualification,
#                 #     experience_level=experience_level,
#                 #     skills=skills,
#                 #     target_role=target_role,
#                 #     linkedin=linkedin,
#                 #     portfolio=portfolio
#                 # )

#                 # db.add(profile)
#                 # db.commit()
#                 # db.close()

#         st.session_state.profile_completed = True
#         st.session_state.profile = {
#                     "full_name": st.session_state.user["full_name"],
#                     "field": field,
#                     "qualification": qualification,
#                     "experience_level": experience_level,
#                     "skills": skills,
#                     "target_role": target_role,
#                     "linkedin": linkedin,
#                     "portfolio": portfolio
#                 }

#         st.success("Profile saved successfully.")
#         st.rerun()

#     # else:
#     #     profile = st.session_state.profile

#     #     with st.sidebar:
#     #         st.header("Interview Setup")

#     #         st.markdown(f"""
#     #         **Candidate:** {profile['full_name']}  
#     #         **Field:** {profile['field']}  
#     #         **Qualification:** {profile['qualification']}  
#     #         **Experience:** {profile['experience_level']}
#     #         """)

#     #         role = st.selectbox(
#     #             "Target Role",
#     #             [
#     #                 profile["target_role"],
#     #                 "AI Intern",
#     #                 "Python Developer",
#     #                 "Data Analyst",
#     #                 "Machine Learning Engineer",
#     #                 "Software Engineer",
#     #                 "Frontend Developer",
#     #                 "Backend Developer"
#     #             ]
#     #         )

#     #         experience = st.selectbox(
#     #             "Interview Experience Level",
#     #             ["Student", "Fresher", "0-1 Year", "1-3 Years", "3-5 Years"],
#     #             index=["Student", "Fresher", "0-1 Year", "1-3 Years", "3-5 Years"].index(profile["experience_level"])
#     #         )

#     #         interview_type = st.selectbox(
#     #             "Interview Type",
#     #             [
#     #                 "HR Interview",
#     #                 "Technical Interview",
#     #                 "Project-Based Interview",
#     #                 "Mixed Interview"
#     #             ]
#     #         )

#     #         total_questions = st.slider(
#     #             "Number of Questions",
#     #             min_value=3,
#     #             max_value=10,
#     #             value=5
#     #         )

#     #         if st.button("Start Interview"):
#     #             st.session_state.started = True
#     #             st.session_state.question_number = 1
#     #             st.session_state.interview_data = []
#     #             st.session_state.feedback_list = []
#     #             st.session_state.final_report = ""

#     #             with st.spinner("Generating first question..."):
#     #                 st.session_state.current_question = generate_question(
#     #                     profile,
#     #                     role,
#     #                     experience,
#     #                     interview_type,
#     #                     st.session_state.question_number
#     #                 )

# #         if not st.session_state.started:
# #             st.subheader("Candidate Dashboard")

# #             c1, c2, c3 = st.columns(3)

# #             c1.metric("Target Role", profile["target_role"])
# #             c2.metric("Experience", profile["experience_level"])
# #             c3.metric("Interview Status", "Not Started")

# #             st.markdown("### Profile Summary")
# #             st.info(f"""
# # Name: {profile['full_name']}

# # Field: {profile['field']}

# # Qualification: {profile['qualification']}

# # Skills: {profile['skills']}

# # LinkedIn: {profile['linkedin']}

# # Portfolio: {profile['portfolio']}
# # """)

# #             st.success("Start your interview from the sidebar.")

# #         else:
# #             st.subheader(f"Question {st.session_state.question_number} of {total_questions}")

# #             st.markdown("### Interview Question")
# #             st.info(st.session_state.current_question)

# #             answer_key = f"user_answer_{st.session_state.question_number}"

# #             st.markdown("### Answer Mode")

# #             answer_mode = st.radio(
# #                 "Choose answer method",
# #                 ["Type Answer", "Speak Answer"],
# #                 horizontal=True
# #             )

# #             speech_text = ""
            
# #             if answer_mode == "Speak Answer":
# #                 st.info("Click Start Recording, speak your answer, then stop recording.")

# #                 audio = mic_recorder(
# #                     start_prompt="🎙️ Start Recording",
# #                     stop_prompt="⏹️ Stop Recording",
# #                     just_once=True,
# #                     use_container_width=True,
# #                     key=f"mic_{st.session_state.question_number}"
# #                 )

# #                 if audio:
# #                     with st.spinner("Converting speech to text..."):
# #                         speech_text = convert_audio_to_text(audio["bytes"])

# #                     if speech_text:
# #                         st.success("Speech converted successfully.")
# #                         st.write("Transcribed Answer:")
# #                         st.info(speech_text)
# #                     else:
# #                         st.warning("Could not understand audio. Please try again or type your answer.")

# #             user_answer = st.text_area(
# #                 "Your Answer",
# #                 value=speech_text,
# #                 height=180,
# #                 placeholder="Write in English, Roman Urdu, Urdu, or mixed language...",
# #                 key=answer_key
# #             )

# #             if st.button("Submit Answer"):
# #                 if user_answer.strip() == "":
# #                     st.warning("Please write your answer first.")
# #                 else:
# #                     with st.spinner("Evaluating your answer..."):
# #                         feedback = generate_feedback(
# #                             role,
# #                             experience,
# #                             interview_type,
# #                             st.session_state.current_question,
# #                             user_answer
# #                         )

# #                     st.session_state.interview_data.append({
# #                         "question_number": st.session_state.question_number,
# #                         "question": st.session_state.current_question,
# #                         "answer": user_answer,
# #                         "feedback": feedback
# #                     })

# #                     st.session_state.feedback_list.append(feedback)

# #                     st.markdown("### AI Feedback")
# #                     st.success(feedback)

# #             col1, col2 = st.columns(2)

# #             with col1:
# #                 if st.button("Next Question"):
# #                     if st.session_state.question_number < total_questions:
# #                         st.session_state.question_number += 1

# #                         with st.spinner("Generating next question..."):
# #                             st.session_state.current_question = generate_question(
# #                                 profile,
# #                                 role,
# #                                 experience,
# #                                 interview_type,
# #                                 st.session_state.question_number
# #                             )

# #                         st.rerun()
# #                     else:
# #                         st.warning("Interview completed. Generate final report now.")

# #             with col2:
# #                 if st.button("Generate Final Report"):
# #                     if len(st.session_state.interview_data) == 0:
# #                         st.warning("Please answer at least one question first.")
# #                     else:
# #                         scores = calculate_average_scores(st.session_state.feedback_list)

# #                         interview_text = ""
# #                         for item in st.session_state.interview_data:
# #                             interview_text += f"""
# # Question {item['question_number']}:
# # {item['question']}

# # Answer:
# # {item['answer']}

# # Feedback:
# # {item['feedback']}

# # -------------------------
# # """

# #                         with st.spinner("Generating final report..."):
# #                             final_report = generate_final_report(
# #                                 profile,
# #                                 role,
# #                                 experience,
# #                                 interview_type,
# #                                 interview_text
# #                             )

# #                         st.session_state.final_report = final_report

# #                         db = SessionLocal()
# #                         saved_report = InterviewReport(
# #                             user_id=st.session_state.user["id"],
# #                             role=role,
# #                             interview_type=interview_type,
# #                             experience_level=experience,
# #                             report=final_report
# #                         )
# #                         db.add(saved_report)
# #                         db.commit()
# #                         db.close()

#         st.markdown("## Final Scores")
#         c1, c2, c3, c4 = st.columns(4)

#         c1.metric("Communication", f"{scores['communication']}/10")
#         c2.metric("Technical", f"{scores['technical']}/10")
#         c3.metric("Confidence", f"{scores['confidence']}/10")
#         c4.metric("Overall", f"{scores['overall']}/10")

#         st.markdown("## Final Report")
#         st.write(final_report)

#         report_file = create_downloadable_report(
#                             profile,
#                             role,
#                             experience,
#                             interview_type,
#                             final_report
#                         )

#         st.download_button(
#                             label="Download Professional Report",
#                             data=report_file,
#                             file_name="professional_interview_report.txt",
#                             mime="text/plain"
#                         )