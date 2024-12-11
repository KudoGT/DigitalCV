import streamlit as st
from pathlib import Path
from PIL import Image


curr_dir = Path(__file__).parent if '__file__' in locals() else Path.cwd()
css_file = curr_dir/'styles'/'main.css'
resume_file = curr_dir/'assets'/'DataScience_CV.pdf'
profile_pic = curr_dir/'assets'/'profile-pic.png'


#---- GENERAL SETTINGS ----

Page_title = 'Digital CV | Yash Raj'
Page_Icon = ':wave:'
Name = 'Yash Raj'
Description = ''' '''
Email = 'yashraj992002@gmail.com'
Social_Media = {'Linkedln':'https://www.linkedin.com/in/yash-raj-07a6a0209/',
                'GitHub':'https://github.com/KudoGT'
                }
Projects ={
    '🏆 Sentiment Analysis for Social Media': '',
    '🏆 Quora Duplicate Question Pair Classifier': '',
    '🏆 Face Recognition System using Siamese Network': '',
    '🏆 Multipurpose Discord chatbot': '',
    '🏆 Crop Weed Detection Using Yolov4': '',
}

st.set_page_config(page_title=Page_title, page_icon=Page_Icon)

st.title('Konnichiwa minna-san!')


#----- Load Css, Pdf & PIC -----
with open(css_file) as f:
    st.markdown('<style>{}</style>'.format(f.read()), unsafe_allow_html =True)
with open(resume_file, 'rb') as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)




# ---- HERO SECTION ------wqe
col1, col2 = st.columns(2, gap='small')
with col1:
    st.image(profile_pic, width=230)
    
    
    
    
with col2:
    st.title(Name)
    st.write(Description)
    st.download_button(
        label = '📄 Download Resume',
        data = PDFbyte,
        file_name = resume_file.name,
        mime = 'application/octet-stream',
    )
    st.write('📩', Email)
    
    
    
# ----- Social Links -----

st.write('\n')
cols = st.columns(len(Social_Media))
for index, (platform, link) in enumerate(Social_Media.items()):
    cols[index].write(f'[{platform}]({link})')



# ----- SKILLS ------
st.write('\n')
st.subheader('Hard Skills')
st.write(
    """
    - Programing : Python
    - Libraries/Framework : Supervised Machine Learning, NLP, Pytorch, Tensorflow, DeepLearning(ANN, RNN, CNN, LSTM, LLM, GRU)
    - Operating Tools: Jupyter Notebook, Git, SQL, VsCode, Pycharm
    - Operating systems: Windows
    """
)


# ----- WORK History ------
st.write('\n')
st.subheader('Experience')
st.write('---')
st.write('No Experience(Fresher)')


# ------- Projects & Accomplishments --------
st.write('\n')
st.subheader('Projects')
for projects, link in Projects.items():
    st.write(f'[{projects}]({link})')
