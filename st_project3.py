import streamlit as st
import pickle

st.title('Are You Asking or Answering a Question?')


page = st.sidebar.selectbox('Select a page', ('About', 'Make a Prediction'))

if page == 'About':
    st.write('My name is Kathy Simon and I am a data scientist')
    st.write('I created a model to determine whether a written statement is asking for information or providing information. Check it out on the next page.')

if page == 'Make a Prediction':
    st.write('r/askscienc and r/todayilearned are both subreddits. Which subreddit does YOUR comment come from?')
    user_text = st.text_input('Please input some text:', value = 'Write your comment here')

    with open('models/subreddits_pipe.pkl', mode ='rb') as pickle_in:
        pipe = pickle.load(pickle_in)
    
    predicted_subreddit = pipe.predict([user_text])[0]

    st.write(f'Your comment came from r/{predicted_subreddit}')
    st.balloons()