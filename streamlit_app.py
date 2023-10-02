import streamlit as st
import app
import utilityFunctions

st.set_page_config(page_title="Career Path", page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)
page_layout = """
<style>
[data-testid="stHeader"]{
    background-color: #679289;
}

[class="main st-emotion-cache-uf99v8 ea3mdgi5"]{
    background-color: #071E22;
}

[id="let-your-experience"]{
    text-align: left;
    color: #1D7874;
    font-size: 4em;
    padding-bottom: 5px;
    padding-left: 15px;
}

[id="show-you-the-path"]{
    text-align: right;
    background-color: #1D7874;
    # width: 100%;
    font-size: 4em;
    padding-top: 5px;
    padding-left: 15px;
    padding-right: 15px;
}


[id="upload-linkedin-profile-and-career-profile"]{
    text-align: center;
    font-size: 1.5em;
    padding-left: 15px;
    padding-bottom: 3px;
}
[id="get-personalized-path-to-success"]{
    text-align: center;
    font-size: 1.5em;
    padding-left: 15px;
    padding-top: 3px;
    padding-bottom: 50px;
}

[id="career-path"]{
    color: #F4C095;
}
[id="strengths"]{
    color: #F4C095;
}
[id="profile-improvement"]{
    color: #F4C095;
}

[data-testid="stHeader"]{
    padding-top: 10px;
    padding-bottom: 10px;
}

</style>
"""

st.markdown(page_layout, unsafe_allow_html=True)
st.title("")
st.title("")
st.title("")
st.title("")
st.title("LET your Experience")
st.title("Show you the PATH!")
st.title("")
st.title("")

st.subheader("Upload LinkedIn profile and Career Profile")
st.subheader("Get Personalized path to success")

linkedin = st.text_input('Enter LinkedIn Profile', '')
career = st.text_input('Enter the career you want.... (Data Scientist, Software Developer, Consultant)', "")
placeholder = st.empty()

submitted = st.button("Submit")
st.title("")

if submitted:
    with st.spinner('Analyzing, Please wait for it...'):
        gptResp = app.showResult(linkedin, career)
        career, strength, improvement = utilityFunctions.cleanResp(gptResp)

    if gptResp==-1:
        st.text("Error while searching....!")
    else:
        st.subheader("Career Path")
        st.markdown(f"""<span style="word-wrap:break-word;">{career}</span>""", unsafe_allow_html=True)
        st.subheader("Strengths")
        st.markdown(f"""<span style="word-wrap:break-word;">{strength}</span>""", unsafe_allow_html=True)
        st.subheader("Profile Improvement")
        st.markdown(f"""<span style="word-wrap:break-word;">{improvement}</span>""", unsafe_allow_html=True)

else:
    st.text("Please fill and press submit.")






