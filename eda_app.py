import numpy as np
import pandas as pd
import streamlit as st
from pandas_profiling import ProfileReport
from streamlit_pandas_profiling import st_profile_report

def main():
    html_temp1 = """<div style="background-color:#913D8D;padding:10px">
                            		<h4 style="color:white;text-align:center;">Exploratory data Analysis Application</h4>
                            		</div>
                            		<div>
                            		</br>"""
    st.markdown(html_temp1, unsafe_allow_html=True)

    menu = ["Home", "EDA", "About"]
    choice = st.sidebar.selectbox("Menu", menu, 2)
    # for hide menu
    hide_streamlit_style = """
                    <style>
                    #MainMenu {visibility: hidden;}
                    footer {visibility: hidden;}
                    </style>
                    """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)


    if choice == "Home":
        # color codes  ff1a75  6D7B8D
        html_temp2 = """<div style="background-color:#728FCE;padding:10px">
                                        		<h4 style="color:white;text-align:center;">This is the EDA App created in Streamlit using the pandas-profiling library.</h4>
                                        		</div>
                                        		<div>
                                        		</br>"""
        st.markdown(html_temp2, unsafe_allow_html=True)

    elif choice == "EDA":
        html_temp3 = """
                        		<div style="background-color:#8C001A;padding:10px">
                        		<h4 style="color:white;text-align:center;">Upload Your file in csv formate and perform Exploratory Data Analysis</h4>
                        		
                        		</div>
                        		<br></br>"""

        st.markdown(html_temp3, unsafe_allow_html=True)
        st.subheader("Perform Exploratory data Analysis with Pandas Profiling Library")
        data_file= st.file_uploader("Upload your input CSV file", type=["csv"])
        if st.button("perform EDA"):
            if data_file is not None:

                @st.cache
                def load_csv():
                    csv = pd.read_csv(data_file)
                    return csv

                df = load_csv()
                pr = df.profile_report()
                st.header('*Input DataFrame*')
                st.title("Pandas Profiling in Streamlit")
                st.write(df)
                st_profile_report(pr)
            else:
                st.success("Upload file")
        else:
            pass
 
    elif choice == "About":
        html_temp4 = """
                       		<div style="background-color:#7D0552;padding:10px">
                       		<h4 style="color:white;text-align:center;">LET'S EXPLORE DATA </h4>
                       		
                       		</div>
                       		<br></br>
                       		<br></br>"""

        st.markdown(html_temp4, unsafe_allow_html=True)
    else:
        pass


if __name__ == "__main__":
    main()