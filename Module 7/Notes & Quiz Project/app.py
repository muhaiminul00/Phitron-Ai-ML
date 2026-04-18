import streamlit as st
from api_calling import note_generator, audio_generator, quiz_generator
from PIL import Image
st.title("Note Summury & Quiz Generator")
st.markdown("Upload upto 3 iamges to generate note & quizzes")
st.divider()

with st.sidebar:
    st.header("Controls")
    Images = st.file_uploader(
        "Uplaod the imgaes of your notes",
        type=['jpg', 'jpeg', 'png'],
        accept_multiple_files=True,
    )
    Colums = st.columns(3)
    img_warn = st.columns(1)
    
    if len(Images) < 4 and len(Images) > 0:
        for i in range(len(Images)):
            with Colums[i]:
                st.image(Images[i])
    elif len(Images) > 3:
        st.warning("Max upload is 3 images")
    
    dificulty = st.selectbox(
        "Choose difficulty level of quizzes",
        options=['Easy', 'Hard', 'Extreme'],
        index=None
    )
    diff_warn = st.columns(1)
    
    Submit = st.button(
        "Generate...",
        type="primary"
    )
    
if Submit and len(Images) < 4:
        if not Images:
            with img_warn[0]:
                st.error("Upload atleast 1 Image !! ")
        if not dificulty:
            with diff_warn[0]:
                st.error("Must choose difficulty level")
        if Images and dificulty:
            
            st.subheader("Note")
            with st.container(border=True):
                pil_images = [Image.open(x) for x in Images]
                with st.spinner("Geneerating notes..."):
                    notes = note_generator(pil_images)
                    st.markdown(notes)
                    
            st.subheader("Transcript")
            with st.container(border=True):
                with st.spinner():
                    st.audio(audio_generator(notes))
                    
            st.subheader("Quiz")
            with st.container(border=True):
                with st.spinner("Generating quizzes..."):
                    generated_quizzes = quiz_generator(pil_images, dificulty)
                    st.markdown(generated_quizzes)
            
                
                
            

        
        
        