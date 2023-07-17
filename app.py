import streamlit as st
from PIL import Image
#####################
# Header 
st.write('''
# Prasidhi Murarka
##### *Resume* 
''')


st.image('dp.png',width=150)


st.markdown('## Summary')
st.info('''
- To enhance my professional skills, capabilities and knowledge in an organization which recognizes the value of hard work and trusts me with responsibilities and challenges.
''')


#####################
# Custom function for printing text
def txt(a, b):
  col1, col2 = st.columns([4,1])
  with col1:
    st.markdown(a)
  with col2:
    st.markdown(b)


#####################
st.markdown('''
## Contact Details
''')
st.markdown('''
- prasidhimurarka@gmail.com
- 8092452516
- ranchi,Jharkhand
''')
st.markdown('''
## Education
''')

txt('**Bachelor of Technology, *Sarala Birla University *, Ranchi',
'2020-2024')
st.markdown('''
- CGPA: `8.8`

''')

txt('**Intermediate, *D.A.V Public School*, Bariatu',
'2019-2020')
st.markdown('''
- Percentage: `79%`
''')

#####################
st.markdown('''
## Internships
''')

txt('**Data Analystics Intern**, TECH MAHINDRA',
'4th JULY-30th August 2022')
st.markdown('''
- Strong Programming and Database experienced with  SQL skills
- Hands-on experience on BI solutions (Power BI)
- Strong communication and cross functional collaboration skills.
- Strong numerical and analytical skills with the ability to collect, organize, analyze, and disseminate significant amounts of information with attention to detail and accuracy

''')

txt('**Tecg Recruiter Intern**, Workfall',
'29th AUGUST-31st OCTOBER 2022')

st.markdown('''
- Design and implement an overall recruitment strategy for the Philippines.
-Source and recruit candidates by using databases, social-media platforms, hiring platforms, etc.
-Prepare recruitment materials, publish job profiles and distribute them on social media channels and other relevant digital platforms.
-Coordinate the full-cycle recruitment process for multiple roles to move candidates through the interview process as smoothly and quickly as possible.
-Managed all communication with candidates from the moment they apply until they become a part of the Workfall team.

''')
#####################
st.markdown('''
## Certificates
''')

st.markdown('''
-Problem solving through programming in C NPTEL-Elite.
-Python course(Udemy)
-Participated  Microsoft AI  classroom series
-CYBER OFFENSIVE DEFENSE ENGINEERING USING PYTHON BEGINNER-Cybervidyapeeeth
''')



#####################
st.markdown('''
## Skills
''')
st.markdown('''
- python
- DSA
- C
- SQL
- MS-EXCEL+
- MS WORD
''')