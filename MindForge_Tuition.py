import streamlit as st
from streamlit_option_menu import option_menu
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
  options=[ "Student Info", "Fees", "Attendence"],
  icons =["file-person", "cash-coin", "toggles"],
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
  
  with st.form("Form 1",clear_on_submit=True):
    col1,col2 = st.columns(2)
    f_name = col1.text_input("First Name") 
    l_name = col2.text_input("Last Name") 

    col3, col4 = st.columns(2)
    cls = col3.text_input("Class")
    cno = col4.text_input("Contact No", max_chars=10)
    s_btn = st.form_submit_button("Submit")

    if s_btn:
      if not all([f_name, l_name, cno, s_btn]):
        st.warning("Please fill all the above fields")
      else:
        st.success("Submitted Successfully")  

elif choice == "Fees":
  st.markdown("<h3 style= 'text-align: center;'> Students Fees</h3>",unsafe_allow_html=True)
  with st.form("Form 2", clear_on_submit=True):

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
        st.success("Paid Successfully")  

else:
    st.markdown("<h3 style= 'text-align: center;'> Student Attendence </h3>", unsafe_allow_html=True)
    with st.form("Form 3", clear_on_submit=True):
           fl_name = st.text_input("Full Name")
           col1,col2, col3 = st.columns(3)
           atnce = col1.text_input("Attendence as Yes/No")
           sbtn = st.form_submit_button("Submit")

           if sbtn:
              if not all([fl_name, sbtn]):
                  st.warning("Please fill all the above fields")
              else:
                  st.success("Submitted Successfully")  