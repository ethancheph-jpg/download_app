import streamlit as st

st.title('dowload the green and red app')

st.write('press the button and dowlaod from your phone')

app_url = f'https://drive.google.com/uc?export=download&id=1MhX1xwzqeXPgjPmkrapBV7NfNTYOLZzS'

st.link_button(
    label='download from me',
    url=app_url
    )
