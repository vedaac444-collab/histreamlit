import streamlit as st
if "step" not in st.session_state:
    st.session_state.step = 1

st.title("Asking Out Batataya!")
st.write("Answer each question one by one using the button below.")

if st.button("Restart"):
    st.session_state.step = 1
    for key in ["answer1", "answer2", "answer3", "answer4", "answer5"]:
        if key in st.session_state:
            del st.session_state[key]

step = st.session_state.step

if step == 1:
    st.radio("1. wanna go out?", ["yes", "no"], key="answer1")
    if st.button("Next", key="next1"):
        if st.session_state.answer1 == "yes":
            st.session_state.step = 2
        else:
            st.session_state.step = 99
        

elif step == 2:
    st.radio("2. soon?", ["yes", "no"], key="answer2")
    if st.button("Next", key="next2"):
        if st.session_state.answer2 == "yes":
            st.session_state.step = 100
        else:
            st.session_state.step = 3
        

elif step == 3:
    st.radio("3. want me to come all the way to Dahisar?", ["yes", "no"], key="answer3")
    if st.button("Next", key="next3"):
        if st.session_state.answer3 == "yes":
            st.session_state.step = 4
        else:
            st.session_state.step = 98
        

elif step == 4:
    st.radio("4. princess treatment chahiye?", ["yes", "no"], key="answer4")
    if st.button("Next", key="next4"):
        if st.session_state.answer4 == "yes":
            st.session_state.step = 97
        else:
            st.session_state.step = 5
        

elif step == 5:
    st.radio("5. nahi hai tu princess?", ["yes", "no"], key="answer5")
    if st.button("Next", key="next5"):
        if st.session_state.answer5 == "yes":
            st.session_state.step = 96
        else:
            st.session_state.step = 95
        

elif step == 99:
    st.error("bhaad mein ja")
    st.write("You can restart if you want to answer again.")

elif step == 100:
    st.success("nerul aa")
    st.write("You can restart if you want to answer again.")

elif step == 98:
    st.warning("wait kar phir")
    st.write("You can restart if you want to answer again.")

elif step == 97:
    st.success("thik hai phir")
    st.write("You can restart if you want to answer again.")

elif step == 96:
    st.success("phir nerul aa")
    st.write("You can restart if you want to answer again.")

elif step == 95:
    st.warning("my 4am mind doesn't know what to say")
    st.write("You can restart if you want to answer again.")
