# https://docs.streamlit.io/library/cheatsheet
# streamlit run app.py
import streamlit as st
import numpy as np 
import joblib
import base64

def get_image_html(page_name, file_name):
    with open(file_name, "rb") as f:
        contents = f.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    return f'<a href="{page_name}"><img src="data:image/png;base64,{data_url}" style="width:300px"></a>'

def get_image_htmlWeb(page_name, file_name,httpHref):
    with open(file_name, "rb") as f:
        contents = f.read()
    data_url = base64.b64encode(contents).decode("utf-8")
    return f'<a href="{httpHref}"><img src="data:image/png;base64,{data_url}" style="width:300px"></a>'
    
data_url = get_image_html("分類-_乳癌預測", "./breast_cancer.jpg")
data_url_2 = get_image_html("迴歸-_計程車小費預測(課堂自帶-未做)", "./taxi.png")
data_url_3 = get_image_htmlWeb("梯度下降法(Colab)", "./Colab.png","https://drive.google.com/file/d/1Pf43IjEkj5KQ-tHOlMPM0u2kvWPb_XiY/view")
data_url_4 = get_image_html("解聯立方程式(作業答案-未做)", "./xy.png")
data_url_5 = get_image_htmlWeb("EDA資料探索與分析(Colab)", "./Colab.png","https://colab.research.google.com/drive/1SpmNMA3Nc2WgK3FU_OZRSmeU3g66suiw")
data_url_6 = get_image_html("分類-_手寫英文字母辨識(nonCNN版)", "./English.png")

st.set_page_config(
    page_title="Python Level-2 學習歷程",
    page_icon="✨",
)

st.title('Python Level-2 學習歷程')   

col1, col2 = st.columns(2)
with col1:
    # url must be external url instead of local file
    # st.markdown(f"### [![分類]({url})](分類)")
    st.markdown('### [(分類)乳癌預測](分類-_乳癌預測)')
    st.markdown('''
    ##### 特徵(X)
        - radius (mean)          
        - texture (mean)                    
        - perimeter (mean)                    
        - area (mean)                    
        - smoothness (mean)                 
        - compactness (mean)                 
        - concavity (mean)                 
        - concave points (mean)                
        - symmetry (mean)                  
        - fractal dimension (mean)  
        - radius (standard error)            
        - texture (standard error)        
        - perimeter (standard error)           
        - area (standard error)            
        - smoothness (standard error)    
        - compactness (standard error)      
        - concavity (standard error)       
        - concave points (standard error) 
        - symmetry (standard error)        
        - fractal dimension (standard error) 
        - radius (worst)                      
        - texture (worst)                    
        - perimeter (worst)                 
        - area (worst)                     
        - smoothness (worst)                
        - compactness (worst)               
        - concavity (worst)                
        - concave points (worst)          
        - symmetry (worst)                
        - fractal dimension (worst)       
    ##### 預測類別(Class)
        - Malignant
        - Benign
        ''')
    # st.image('breast_cancer.jpg')
    st.markdown(data_url, unsafe_allow_html=True)
    
    st.markdown('### [(分類)手寫英文字母辨識](分類-_手寫英文字母辨識(nonCNN版))')
    st.markdown('''
    ##### 手寫英文字母辨識 , 此版本沒有套用CNN , 準確度不高
        ''')
    # st.image('Colab.png')
    st.markdown(data_url_6, unsafe_allow_html=True) 
    
with col2:
    st.markdown('### [(迴歸)計程車小費預測](迴歸-_計程車小費預測(課堂自帶-未做))')
    st.markdown('''
    ##### 特徵(X):
        - 車費
        - 性別
        - 吸菸
        - 星期
        - 時間
        - 同行人數
    ##### 目標：預測小費金額
        ''')
    # st.image('taxi.png')
    st.markdown(data_url_2, unsafe_allow_html=True)
    
    st.markdown('### [(聯立)解聯立方程式](解聯立方程式(作業答案-未做))')
    st.markdown('''
    ##### 帶入消去法
        ''')
    # st.image('Colab.png')
    st.markdown(data_url_4, unsafe_allow_html=True) 
    
    st.markdown('### [(Colab)梯度下降法](https://drive.google.com/file/d/1Pf43IjEkj5KQ-tHOlMPM0u2kvWPb_XiY/view)')
    st.markdown('''
    ##### 用Colab 完成梯度下降作業
        ''')
    # st.image('Colab.png')
    st.markdown(data_url_3, unsafe_allow_html=True) 
    
    st.markdown('### [(Colab)EDA資料探索與分析](https://colab.research.google.com/drive/1SpmNMA3Nc2WgK3FU_OZRSmeU3g66suiw)')
    st.markdown('''
    ##### 用Colab EDA資料探索與分析
        ''')
    # st.image('Colab.png')
    st.markdown(data_url_5, unsafe_allow_html=True)