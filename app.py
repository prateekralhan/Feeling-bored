import streamlit as st
import hydralit_components as hc
import requests
from PIL import Image
import time

st.set_page_config(
    page_title="Feeling Bored?",
    page_icon="✨",
    layout="centered",
    initial_sidebar_state="expanded",
)

top_image = Image.open('static/banner_top.png')
bottom_image = Image.open('static/banner_bottom.png')
main_image = Image.open('static/main_banner.png')
low_image = Image.open('static/low_banner.png')

st.image(main_image,use_column_width='auto')
st.title('🤔 Feeling Bored? 🥱')
st.markdown("Don't worry. I can help you find something to do. 😉✅")

st.sidebar.image(top_image,use_column_width='auto')
st.sidebar.header('🔴 Input 🔴')
selected_type = st.sidebar.selectbox('Please select an activity type 🚀', ["Education", "Recreational", "Social", "DIY", "Charity", "Cooking", "Relaxation", "Music", "Busywork"])
st.sidebar.image(bottom_image,use_column_width='auto')

suggested_activity_url = f'http://www.boredapi.com/api/activity?type={selected_type.lower()}'
json_data = requests.get(suggested_activity_url)
suggested_activity = json_data.json()

st.header('Suggested activity')

with hc.HyLoader('',hc.Loaders.standard_loaders,index=1):
  time.sleep(2)
  st.success(suggested_activity['activity']+" ✅😉")

st.image(low_image,use_column_width='auto')

st.markdown("<br><hr><center>Made with ❤️ by <a href='mailto:ralhanprateek@gmail.com?subject=Feeling bored WebApp!&body=Please specify the issue you are facing with the app.'><strong>Prateek Ralhan</strong></a></center><hr>", unsafe_allow_html=True)
