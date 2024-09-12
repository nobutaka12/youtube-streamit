import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time

st.title('Streamit 超入門')

st.write('プログレスバーの表示')
'勉強の'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'やる気　{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'むきむき！！'


left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')

if button:
    right_column.write('ここは右カラム')

expander1 = st.expander('問い合わせ')
expander1.write('問い合わせ1に対する回答')

expander2 = st.expander('問い合わせ')
expander2.write('問い合わせ2に対する回答')

expander3 = st.expander('問い合わせ')
expander3.write('問い合わせ3に対する回答')

# text = st.text_input(
#     'あなた趣味を教えてください。'
# )
# 'あなたの趣味：', text, 'です。'

# condition = st.slider('あなたの今の調子は？', 0, 100, 50)
# 'コンディション：', condition
# if st.checkbox('Show Image'):
#     img = Image.open('sample.png')
#     st.image(img, caption='Udemy kyouzai', use_column_width=True)
