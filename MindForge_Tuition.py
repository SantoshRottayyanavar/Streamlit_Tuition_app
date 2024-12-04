import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd
import os

st.set_page_config(page_title="MindForge_Tuition", layout="wide", page_icon="👨🏻‍💼")
st.markdown("""<style>
.st-emotion-cache-1wbqy5l.e17vllj40
{
            visibility : Hidden;
}            
.st-emotion-cache-125megu.ef3psqc5 
{
            visibility : Hidden;
}                       
</style>""", unsafe_allow_html=True)

with st.sidebar:
 choice = option_menu(
  menu_title=None,
  options=[ "Student Info", "Fees", "Attendence", "Report"],
  icons =["file-person", "cash-coin", "toggles", "table"],
  menu_icon="cast",
  default_index=0,
 )

img, titl = st.columns([1,2]) 
with img:
  st.image("D:\Streamlit\env\Tution.png", width=150)
with titl:
  st.title("MindForge Tuition")
st.write("---")



if choice == "Student Info":
  st.markdown("<h3 style= 'text-align: center;'> Student Information </h3>", unsafe_allow_html=True)
    #Create Session state
  if "student_info" not in st.session_state or "student_info" in st.session_state:
    try:
          st.session_state.student_info = pd.read_csv("Student_Information.csv")
    except:
          st.session_state.student_info = pd.DataFrame(columns =  ["First Name",
                        "Last Name",
                        "Class",
                        "Contact NO"])
    
  #add, remove
  rad= st.radio("Choose any one for Add or Remove", options=("ADD", "Remove"))
  if rad == "ADD":
    with st.form("Student Information",clear_on_submit=True):
      col1,col2 = st.columns(2)
      f_name = col1.text_input("First Name") 
      l_name = col2.text_input("Last Name") 

      col3, col4 = st.columns(2)
      cls = col3.text_input("Class")
      cno = col4.text_input("Contact No", max_chars=10)

      col1, col2, col3, col4 = st.columns(4)
      s_btn = col1.form_submit_button("Submit")
      #remove = col2.form_submit_button("Remove")

      if s_btn:
        if not all([f_name, l_name, cls, cno]):
          st.warning("Please fill all the above fields")
        else:
          new_entry = [{"First Name": f_name,
                    "Last Name": l_name,
                    "Class": cls,
                    "Contact NO" : cno }]
          st.session_state.student_info = pd.concat([st.session_state.student_info, pd.DataFrame(new_entry)], ignore_index=True)
          st.session_state.student_info.to_csv("Student_Information.csv", index = False)
          #st.dataframe(st.session_state.student_info)      
          st.success("Submitted Successfully")
          st.write(st.session_state.student_info)

 #Students Remove
  elif rad == "Remove":
    col1, col2 = st.columns(2)
    f_n = col1.text_input("First Name")
    l_n = col2.text_input("Last Name")
    s_r = st.button("Remove")
    if s_r:
     if not all([f_n, l_n]):
       st.warning("Please enter First Name and Last Name fields properly to remove a perticular person")
     else:
       if not st.session_state.student_info.empty:
          st.session_state.student_info = st.session_state.student_info.drop(
             st.session_state.student_info[
                (st.session_state.student_info['First Name'] ==  f_n ) & 
                (st.session_state.student_info['Last Name'] == l_n)].index)
          st.session_state.student_info.to_csv("Student_Information.csv", index = False)
          st.success(f"Record for {f_n} {l_n} has been removed.")
       else:
          st.warning("No data Available to remove.") 
       st.write(st.session_state.student_info)     

         
elif choice == "Fees":
  st.markdown("<h3 style= 'text-align: center;'> Students Fees</h3>",unsafe_allow_html=True)
  if "student_fees" not in st.session_state or "student_fees" in st.session_state:
    try:
       st.session_state.student_fees = pd.read_csv("Student_Fees.csv")
    except:
       st.session_state.student_fees = pd.DataFrame(columns = ["First Name", "Last Name", "Fees", "Date", "Time"])
    
    rad1 = st.radio("Select any one to add or remove fees information(remove only if any wrong information)", options=("ADD","Remove"))
    if rad1 == "ADD":
      with st.form("Students Fees", clear_on_submit=True):

        col1, col2 = st.columns(2)
        fname = col1.text_input("First Name")
        lname = col2.text_input("Last Name")
        fe = st.number_input("Enter Fees")

        col3, col4 = st.columns(2)
        dat = col3.date_input("Enter Date")
        tme = col4.time_input("Enter Time")
        p_btn = st.form_submit_button("Paid")

        if p_btn:
          if not all([fname, lname, fe, dat, p_btn]):
            st.warning("Please fill all the above fields")
          else:
            new_fee_entry = [{"First Name": fname, "Last Name": lname, "Fees": fe, "Date": dat, "Time": tme}]
            st.session_state.student_fees = pd.concat([st.session_state.student_fees, pd.DataFrame(new_fee_entry)], ignore_index=True)
            st.session_state.student_fees.to_csv("Student_Fees.csv", index=False)
            st.success("Paid Successfully") 
            st.write(st.session_state.student_fees)

    elif rad1 == "Remove":
       col1, col2 = st.columns(2)
       fn_ = st.text_input("First Name")
       ln_ = st.text_input("Last Name") 
       rb_  = st.button("Remove")       
       



elif choice == "Attendence":
    st.markdown("<h3 style= 'text-align: center;'> Student Attendence </h3>", unsafe_allow_html=True)
    with st.form("Student Attendence", clear_on_submit=True):
           fl_name = st.text_input("Full Name")
           col1,col2, col3 = st.columns(3)
           atnce = col1.text_input("Attendence as Yes/No")
           sbtn = st.form_submit_button("Submit")

           if sbtn:
              if not all([fl_name, sbtn]):
                  st.warning("Please fill all the above fields")
              else:
                  st.success("Submitted Successfully")  

else:
   st.markdown("<h3 style= 'text-align: center;'> Report </h3>", unsafe_allow_html=True)

   #Student Information
   st.markdown("<h5> Student Information </h5>",unsafe_allow_html=True)
   st.write(st.session_state.student_info) 

   #Student Fees
   st.markdown("<h5> Student Fees </h5>", unsafe_allow_html=True)