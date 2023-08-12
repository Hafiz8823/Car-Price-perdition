
import pandas as pd 
import datetime 
import xgboost as xgb
import streamlit as st

def main():
    html_temp="""
      <div style  = "background-color:Lightblue;padding:16px">
      <h2 style = "color:black;text-align:center;"> Car Price Prediction Using MachineLearning</h2>
      </div>
    """
    model = xgb.XGBRegressor()
    model.load_model("xgb_model.json")

    st.markdown(html_temp,unsafe_allow_html=True)
    st.write('')
    st.write('')
    st.markdown("##### Are you Planning to sell your Car!?\n##### So Let's try evaluating the Price.")

    p1=st.number_input("What is the Current Ex-showroom price of car (In lakhs)",2.5,20.0,step=1.0)    ##step shown the difference like 2.5,3.5
    p2=st.number_input("What is distance comleted by the Car in kilometers?",100,500000,step=100)
    s1=st.selectbox("What is the Fual type?",('Petrol','Diesel','CNG'))
    if s1=="Petrol":
        p3=0
    elif s1=="Diesel":
        p3=1
    elif s1=="CNG":
        p3=2        
    
    s2=st.selectbox("Are you Dealer or Individual?",('Dealer','Individual'))
    if s2=="Dealer":
        p4=0
    elif s2=="Individual":
        p4=1
    
    s3=st.selectbox("What is The Transmission Type?",('Manual','Automatic'))
    if s3=="Manual":
        p5=0
    elif s3=="Automatic":
        p5=1
    p6=st.slider("Number of Owners the Car previously had?",0,3)

    Date_time=datetime.datetime.now()
    years=st.number_input("In which year car was purchases?",1990,Date_time.year)
    p7=Date_time.year-years

    data_new = pd.DataFrame({
    'Present_Price':p1,
    'Kms_Driven':p2,
    'Fuel_Type':p3,
    'Seller_Type':p4,
    'Transmission':p5,
    'Owner':p6,
    'Age':p7
},index=[0])
    try:
       if st.button('predict'):
          pred = model.predict(data_new)
          if pred>0:
            st.balloons()
            st.success("You can sell your car for {:.2f} Lakhs".format(pred[0]))
          else:
              st.warning("You can't able to sell this car")
    except:
        st.warning("Something Went Wrong please try again")

    
    
    
    
if __name__== '__main__':
    main()