import streamlit as st

st.title("60_Day_Coding_Challenge")


def day2():

  with st.container():
    st.header("Day_2 Dec-12")
    
    with st.container():
      st.write("1. Solving leet code questions")
      st.write("2. Done mock interview with friend, suggestion to improvise on edge cases")
      st.write("3. Finished SQL queries on CRUD operations")

def day1():

  with st.container():
    st.header("Day_1 Dec-11")

    with st.container():
      st.text("1. Hosting this website using github and streamlit cloud")
      st.text("2. completion of sql queries joins and aggregates")
      st.text("3. leet code question island question")
    

def main ():
  day2()
  day1()


if __name__ == "__main__":
  main()
