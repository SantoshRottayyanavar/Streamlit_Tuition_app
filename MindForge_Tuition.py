import streamlit as st
from streamlit_option_menu import option_menu
import pandas as pd

st.set_page_config(page_title="MindForge_Tuition", layout="wide", page_icon="👨🏻‍💼")

page_bg_image = """
<style>
[data-testid="stMain"] {
background-image: url("https://img.freepik.com/free-photo/black-background-with-leaves-vegetation-texture_23-2149872513.jpg?t=st=1733395221~exp=1733398821~hmac=8252e2041bb510ccfc16ca40a293c1b3d610f4fa3a5e83eafda1fab8c4f4202f&w=1060");
background-size: cover;
}
[data-testid="stHeader"] {
background-color: rgba(0, 0, 0, 0);
}
[data-testid="stSidebar"] {
background-image: url("https://img.freepik.com/free-vector/elegant-watercolor-background-with-golden-foil-leaves-greeting-invitation-card-design_25819-714.jpg?t=st=1733395921~exp=1733399521~hmac=3c4834eea5da3ff157367c4aa467474243ae14548c88071384aa9fb0d13f09d7&w=740");
background-size: cover;
}
</style>"""
st.markdown(page_bg_image, unsafe_allow_html=True)


# st.markdown("""<style>
# .st-emotion-cache-1wbqy5l.e17vllj40
# {
#             visibility : Hidden;
# }            
# .st-emotion-cache-125megu.ef3psqc5 
# {
#             visibility : Hidden;
# }                       
# </style>""", unsafe_allow_html=True)

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
  st.image("Tution.png", width=150)
with titl:
  st.title("MindForge Tuition")
st.write("---")


#student info section
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
          st.success("Submitted Successfully")
          # st.write(st.session_state.student_info)

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

    #Showing Final Report of Student Information
    if "student_info" not in st.session_state or "student_info" in st.session_state:
      st.session_state.student_info = pd.read_csv("Student_Information.csv")
  st.table(st.session_state.student_info)     

#Fees section        
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
        fe = round(st.number_input("Enter Fees"))

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

    #Removing wrongly inserted data in fees section
    elif rad1 == "Remove":
       col1, col2 = st.columns(2)
       fn_ = st.text_input("First Name")
       ln_ = st.text_input("Last Name") 
       rb_  = st.button("Remove") 

       if  rb_:   
          if not all([fn_, ln_]):
             st.warning("Fill the wrong data into all the fields given above")
          else:
             if not st.session_state.student_fees.empty:
                st.session_state.student_fees = st.session_state.student_fees.drop(
                   st.session_state.student_fees[
                      (st.session_state.student_fees["First Name"] ==  fn_) &
                      (st.session_state.student_fees["Last Name"] == ln_)].index)
                st.session_state.student_fees.to_csv("Student_Fees.csv", index=False)
                st.success(f"{fn_} {ln_} has been removed successfully")
    
    #Showing Student Fees Report
    if "student_fees" not in st.session_state or "student_fees" in st.session_state:
       st.session_state.student_fees = pd.read_csv("Student_Fees.csv")
  st.table(st.session_state.student_fees)
             
#Attendence section
elif choice == "Attendence":
    st.markdown("<h3 style= 'text-align: center;'> Student Attendence </h3>", unsafe_allow_html=True)
    if "student_attendence" not in st.session_state or "student_attendence" in st.session_state:
        try:
          st.session_state.student_attendence = pd.read_csv("Student Attendence.csv")
        except:
          st.session_state.student_attendence = pd.DataFrame(columns = ["First Name" , "Last Name", "Attendence", "Date", "Time", "Leave Reason"])
        
        rad2 = st.radio("Select any one button to add and remove (remove only when you typed wrong)", options = ("ADD", "Remove"))
        if rad2 == "ADD":
          with st.form("Student Attendence", clear_on_submit=True):
                col1, col2 = st.columns(2)
                fst_name = col1.text_input("First Name")
                lst_name = col2.text_input("Last Name")

                col1,col2, col3 = st.columns(3)
                atnce = col1.text_input("Attendence as Yes/No")

                col1, col2 = st.columns(2)
                dat = col1.date_input("Date")
                tme = col2.time_input("Time")

                reason = st.text_area("Leave Reason")

                sbtn = st.form_submit_button("Submit")

                if sbtn:
                    if not all([fst_name, lst_name, atnce, dat, tme ]):
                        st.warning("Please fill all the above fields")
                    else:
                        new_atendce = [{"First Name": fst_name, "Last Name": lst_name, "Attendence": atnce, "Date": dat, "Time": tme, "Leave Reason": reason}]
                        st.session_state.student_attendence = pd.concat([ st.session_state.student_attendence, pd.DataFrame(new_atendce)], ignore_index = True)
                        st.session_state.student_attendence.to_csv("Student Attendence.csv", index=False)
                        st.success(f"{fst_name} {lst_name} is attende today")  

        elif rad2 == "Remove":
           col1, col2 = st.columns(2)
           ft_name = col1.text_input("Firs Name")
           lt_name = col2.text_input("Last Name")
           rba = st.button("Remove")

           if rba:
              if not all([ft_name, lt_name]):
                 st.warning("Please fill all the above feilds")
              else:   
                st.session_state.student_attendence = st.session_state.student_attendence.drop(
                  st.session_state.student_attendence[
                      (st.session_state.student_attendence["First Name"] == ft_name) &
                      (st.session_state.student_attendence["Last Name"] == lt_name)].index)
                st.session_state.student_attendence.to_csv("Student Attendence.csv", index = False)
                st.success(f"{ft_name} {lt_name} has been removed")
        #Showing Student Attendence Report
        if "student_attendence" not in st.session_state or "student_attendence" in st.session_state:
                st.session_state.student_attendence = pd.read_csv("Student Attendence.csv")
    st.table(st.session_state.student_attendence)

#Report Section
else:
   st.markdown("<h3 style= 'text-align: center;'> Report </h3>", unsafe_allow_html=True)

   st.markdown("<h5> Student Information </h5>", unsafe_allow_html=True)
   if "student_info" not in st.session_state or "student_info" in st.session_state:
          st.session_state.student_info = pd.read_csv("Student_Information.csv")
   st.table(st.session_state.student_info) 

   st.markdown("<h5> Student Fees </h5>", unsafe_allow_html=True)
   if "student_fees" not in st.session_state or "student_fees" in st.session_state:
       st.session_state.student_fees = pd.read_csv("Student_Fees.csv")
   st.table(st.session_state.student_fees)

   st.markdown("<h5> Student Attendence </h5>", unsafe_allow_html=True)
   if "student_attendence" not in st.session_state or "student_attendence" in st.session_state:
          st.session_state.student_attendence = pd.read_csv("Student Attendence.csv")
   st.table(st.session_state.student_attendence)