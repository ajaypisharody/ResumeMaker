import streamlit as st
from fpdf import FPDF
import time
def createfunc(fname,lname,email,address,contact,portfolio,LinkedIn,profession,field,subfield,qualification,degree,skills,age,projects,AdditionalSkills,Extracurricular,Certificates,achievement,Hobbies,tagline):
  pdf=FPDF()
  pdf.add_page()
  pdf.set_draw_color(176,224,230)
  pdf.set_font("Arial",'B',size=14)
  name=fname+" "+lname 
  info=email+" | "+contact
  pdf.cell(200,20,txt=name,ln=2,align='L')

  pdf.set_font("Arial",size=12)
  pdf.cell(200,10,txt=info,ln=2,align='L')
  pdf.cell(200,10,txt=address,ln=2,align='L')
  pdf.cell(200,10,txt=portfolio,ln=2,align='L',link=portfolio)
  pdf.cell(200,10,txt=LinkedIn,ln=2,align='L',link=LinkedIn)
  pdf.set_line_width(3)

  pdf.line(10,72,200,72)
  pdf.set_line_width(0.3)
  pdf.set_font("Arial",'B',size=14)
  pdf.cell(190,25,txt="Objective",border='B',ln=2,align='L')
 

  pdf.set_font("Arial",size=12)
  pdf.multi_cell(190,10,txt=tagline)

  pdf.set_font("Arial",'B',size=14)
  pdf.cell(190,10,txt="Education",border='B',ln=2,align='L')


  pdf.set_font("Arial",size=12)
  pdf.cell(200,10,txt=field+" - "+degree,ln=2)

  pdf.set_font("Arial",'B',size=14)
  pdf.cell(190,10,txt="Skills",border='B',ln=2,align='L')


  pdf.set_font("Arial",size=12)
  sk=len(skills)
  for i in range(sk):
    pdf.multi_cell(200,10,txt=chr(149)+" "+skills[i])

  pdf.set_font("Arial",'B',size=14)
  pdf.cell(190,10,txt="Projects",ln=2,border='B',align='L')
  pdf.set_font("Arial",size=12)
  pdf.multi_cell(200,10,txt=projects)

  pdf.set_font("Arial",'B',size=14)
  pdf.cell(190,10,txt="Additional Skills",border='B',ln=2,align='L')
  pdf.set_font("Arial",size=12)
  pdf.multi_cell(200,10,txt=Additionalskills)
    
  pdf.set_font("Arial",'B',size=14)
  pdf.cell(190,10,txt="Extracurricular and Academic Activities",border='B',ln=2,align='L')
  pdf.set_font("Arial",size=12)
  pdf.multi_cell(200,10,txt=Extracurricular)
  

  pdf.set_font("Arial",'B',size=14)
  pdf.cell(190,10,txt="Certifications",border='B',ln=2,align='L')
  pdf.set_font("Arial",size=12)
  pdf.multi_cell(200,10,txt=Certificates)
 

  pdf.set_font("Arial",'B',size=14)
  pdf.cell(190,10,txt="Hobbies",border='B',ln=2,align='L')
  pdf.set_font("Arial",size=12)
  pdf.multi_cell(200,10,txt=Hobbies)
  

  pdf.set_font("Arial",size=12)
  pdf.cell(200,20,txt="I hereby declare that all the details given are true to the best of my knowledge and belief.",ln=2,align='L')
  pdf.cell(200,25,txt=name,ln=2,align='L')
  
  pdf.output("Resume.pdf",dest='F').encode('utf-8')
  



st.header("ResumeMaker - Make a Wonderful Resume with Ease")
st.markdown("---")
fname=st.text_input("First Name:")
lname=st.text_input("Last Name:")
email=st.text_input("Email Address:")
address=st.text_input("Address:")
contact=st.text_input("Contact Number:")
portfolio=st.text_input("Portfolio Link(if available):")
LinkedIn=st.text_input("LinkedIn link:")
profession=st.radio("Are you a Student or an Employee?",["Student","Employee"])

if profession=="Student":
  field=st.selectbox("Your Field:",["Engineering","IT","Commerce","Arts","Medicine"])
  if field=="Engineering":
    subfield=st.selectbox("Subfield:",["Mechanical Engineering","Automobile Engineering","Civil Engineering","Electrical Engineering"])
    qualification=st.selectbox("Qualification:",["Diploma","Associate","Bachelor","Master","Doctorate"])
    if qualification=="Diploma":
      degree=st.selectbox("Degree:",["Diploma in Engineering","Diploma in Engineering(Sandwich)"])
    elif qualification=="Associate":
      degree=st.selectbox("Degree:",["ITI"])
    elif qualification=="Bachelor":
      degree=st.selectbox("Degree:",["Bachelor of Engineering","Bachelor of Technology"])
    elif qualification=="Master":
      degree=st.selectbox("Degree:",["Master of Engineering","Master of Technology","M.Phil","PGD"])
    else:
      degree=st.selectbox("Degree:",["PhD","Masters(Honours)"])
    profession=st.radio("Do you want to add another field?",["Yes","No"])
    skills=st.multiselect("What are your skills?",["AutoCAD","Tekla","Catia","Drawing","Fabrication","CNC coding","CNC operation"])
  elif field=="IT":
    subfield=st.selectbox("Subfield:",["Computer Engineering","Information Technology"])
    qualification=st.selectbox("Qualification:",["Self-Learned","Diploma","Bachelor","Master","Doctorate"])
    if qualification=="Self-Learned":
      degree=st.selectbox("Degree:",["Bootcamp","Online Certifications","Professional Courses"])
    elif qualification=="Diploma":
      degree=st.selectbox("Degree:",["Diploma in Engineering","Diploma in IT"])
    elif qualification=="Bachelor":
      degree=st.selectbox("Degree:",["BSC in IT","BCA","BCS","Bachelor of Engineering","Bachelor of Technology"])
    elif qualification=="Master":
      degree=st.selectbox("Degree:",["MSC in IT","MCA","MCS","MBA in IT","Master of Engineering","Master of Technology","M.Phil","PGD"])
    else:
      degree=st.selectbox("Degree:",["PhD","Masters(Honours)"])
    skills=st.multiselect("What are your skills?",["C","C++","JAVA","HTML","CSS","Javascript","Databases","Python","Analysis Tools","AI","ML","Android Development","iOS development","Full Stack Development"])
  elif field=="Commerce":
    qualification=st.selectbox("Qualification:",["Bachelor","Master","Doctorate"])
  elif field=="Arts":
    qualification=st.selectbox("Qualification:",["Diploma","Bachelor","Master","Doctorate"])
  else:
    qualification=st.selectbox("Qualification:",["Diploma","Bachelor","Master","Doctorate"])
  age=st.date_input("Birth Date:")
  projects=st.text_area("Projects:")
  Additionalskills=st.text_area("Additional Skills:")
  Extracurricular=st.text_area("Extracurricular Activities:")
  Certificates=st.text_area("Certifications(Provide a line about the achievement):")
  achievement=st.text_area("Professional Achievements/Experience:")
  Hobbies=st.text_area("Hobbies:")
  tagline=st.text_area("Objective:")

  
  if st.button("Create Resume!"):
    with st.spinner("Creating Resume..."):
      createfunc(fname,lname,email,address,contact,portfolio,LinkedIn,profession,field,subfield,qualification,degree,skills,age,projects,Additionalskills,Extracurricular,Certificates,achievement,Hobbies,tagline)
      time.sleep(3)
    st.success("Resume Created!")
    
    


else:
  field=st.selectbox("Field of Profession:",["Engineering","IT","Commerce","Arts","Medicine"])
  if field=="Engineering":
    subfield=st.selectbox("Subfield:",["Mechanical Engineer","Automobile Engineer","Civil Engineer","Electrical Engineer"])
    qualification=st.selectbox("Qualification:",["Diploma","Associate","Bachelor","Master","Doctorate"])
    if qualification=="Diploma":
      degree=st.selectbox("Degree:",["Diploma in Engineering","Diploma in Engineering(Sandwich)"])
    elif qualification=="Associate":
      degree=st.selectbox("Degree:",["ITI"])
    elif qualification=="Bachelor":
      degree=st.selectbox("Degree:",["Bachelor of Engineering","Bachelor of Technology"])
    elif qualification=="Master":
      degree=st.selectbox("Degree:",["Master of Engineering","Master of Technology","M.Phil","PGD"])
    else:
      degree=st.selectbox("Degree:",["PhD","Masters(Honours)"])
    experience=st.slider("Experience:",0,15)
  elif field=="IT":
    qualification=st.selectbox("Qualification:",["Self-Learned","Diploma","Bachelor","Master","Doctorate"])
    if qualification=="Self-Learned":
      degree=st.selectbox("Degree:",["Bootcamp","Online Certifications","Professional Courses"])
    elif qualification=="Diploma":
      degree=st.selectbox("Degree:",["Diploma in Engineering","Diploma in IT"])
    elif qualification=="Bachelor":
      degree=st.selectbox("Degree:",["BSC in IT","BCA","BCS","Bachelor of Engineering","Bachelor of Technology"])
    elif qualification=="Master":
      degree=st.selectbox("Degree:",["MSC in IT","MCA","MCS","MBA in IT","Master of Engineering","Master of Technology","M.Phil","PGD"])
    else:
      degree=st.selectbox("Degree:",["PhD","Masters(Honours)"])
    experience=st.slider("Experience:",0,15)
  elif field=="Commerce":
    qualification=st.selectbox("Qualification:",["Bachelor","Master","Doctorate"])
    experience=st.slider("Experience:",0,15)
  elif field=="Arts":
    qualification=st.selectbox("Qualification:",["Diploma","Bachelor","Master","Doctorate"])
    experience=st.slider("Experience:",0,15)
  else:
    qualification=st.selectbox("Qualification:",["Diploma","Bachelor","Master","Doctorate"])
    experience=st.slider("Experience:",0,15)
  age=st.date_input("Birth Date:")
  Additionalskills=st.text_area("Additional Skills:")
  Extracurricular=st.text_area("Extracurricular Activities:")
  Hobbies=st.text_area("Hobbies:")
  st.button("Create Resume!")
