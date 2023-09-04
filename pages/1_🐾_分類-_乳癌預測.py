import streamlit as st
import joblib

# 載入模型與標準化轉換模型
clf = joblib.load('class_model.joblib')
scaler = joblib.load('class_scaler.joblib')

st.title('是否罹患乳癌預測')
mean_radius                = st.slider('mean_radius',min_value=0.0, max_value=30.0, value =14.0)
mean_texture               = st.slider('mean_texture',min_value=0.0, max_value=40.0, value =19.0)
mean_perimeter             = st.slider('mean_perimeter',min_value=0.0, max_value=200.0, value =91.0)
mean_area                  = st.slider('mean_area',min_value=0.0, max_value=3000.0, value =654.0)
mean_smoothness            = st.slider('mean_smoothness',min_value=0.0, max_value=1.0, value =0.09)
mean_compactness           = st.slider('mean_compactness',min_value=0.0, max_value=1.0, value = 0.1)
mean_concavity             = st.slider('mean_concavity',min_value=0.0, max_value=1.0, value = 0.08)
mean_concave_points        = st.slider('mean_concave_points',min_value=0.0, max_value=1.0, value = 0.04)
mean_symmetry              = st.slider('mean_symmetry',min_value=0.0, max_value=1.0, value = 0.18)
mean_fractal_dimension     = st.slider('mean_fractal_dimension',min_value=0.0, max_value=1.0, value = 0.06)
radius_error               = st.slider('radius_error',min_value=0.0, max_value=10.0, value = 0.4)
texture_error              = st.slider('texture_error',min_value=0.0, max_value=10.0, value = 1.2)
perimeter_error            = st.slider('perimeter_error',min_value=0.0, max_value=100.0, value = 2.8)
area_error                 = st.slider('area_error',min_value=0.0, max_value=1000.0, value = 40.0)
smoothness_error           = st.slider('smoothness_error',min_value=0.0, max_value=0.5, value = 0.007)
compactness_error          = st.slider('compactness_error',min_value=0.0, max_value=0.5, value = 0.025)
concavity_error            = st.slider('concavity_error',min_value=0.0, max_value=0.5, value = 0.031)
concave_points_error       = st.slider('concave_points_error',min_value=0.0, max_value=0.5, value = 0.011)
symmetry_error             = st.slider('symmetry_error',min_value=0.0, max_value=0.5, value = 0.02)
fractal_dimension_error    = st.slider('fractal_dimension_error',min_value=0.0, max_value=0.5, value = 0.003)
worst_radius               = st.slider('worst_radius',min_value=0.0, max_value=100.0, value = 16.0)
worst_texture              = st.slider('worst_texture',min_value=0.0, max_value=100.0, value = 25.0)
worst_perimeter            = st.slider('worst_perimeter',min_value=0.0, max_value=500.0, value = 107.0)
worst_area                 = st.slider('worst_area',min_value=0.0, max_value=5000.0, value = 880.0)
worst_smoothness           = st.slider('worst_smoothness',min_value=0.0, max_value=1.0, value = 0.1)
worst_compactness          = st.slider('worst_compactness',min_value=0.0, max_value=10.0, value = 0.25)
worst_concavity            = st.slider('worst_concavity',min_value=0.0, max_value=10.0, value = 0.27)
worst_concave_points       = st.slider('worst_concave',min_value=0.0, max_value=1.0, value = 0.11)
worst_symmetry             = st.slider('worst_symmetry',min_value=0.0, max_value=1.0, value = 0.29)
worst_fractal_dimension    = st.slider('worst_fractal_dimension',min_value=0.0, max_value=1.0, value = 0.08)

labels = ['malignant', 'benign']
if st.button('預測'):
    X_new = [[mean_radius,mean_texture,mean_perimeter,mean_area,mean_smoothness,mean_compactness,mean_concavity
              ,mean_concave_points,mean_symmetry,mean_fractal_dimension,radius_error,texture_error,perimeter_error
              ,area_error,smoothness_error,compactness_error,concavity_error,concave_points_error,symmetry_error
              ,fractal_dimension_error,worst_radius,worst_texture,worst_perimeter,worst_area,worst_smoothness
              ,worst_compactness,worst_concavity,worst_concave_points,worst_symmetry,worst_fractal_dimension]]
    X_new = scaler.transform(X_new)
    st.write('### 預測結果是：', labels[clf.predict(X_new)[0]])
