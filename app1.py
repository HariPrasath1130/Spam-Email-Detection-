import streamlit as st
import joblib

model = joblib.load('model.pkl')
vectorizer = joblib.load('vectorizer.pkl')

st.title("📧 Text & Email Spam Detector")
st.write("Type or paste any message below to check if it's **Spam** or **Safe (Ham)**.")

user_message = st.text_area("Message Content", placeholder="Paste message text here (e.g. Please send me your notes)...")

if st.button("Check Message"):
    if user_message.strip() != "":
        message_tfidf = vectorizer.transform([user_message])
        prediction = model.predict(message_tfidf)[0]
        
        if prediction == "spam":
            st.error("🚨 **Prediction: SPAM** — This message looks suspicious!")
        else:
            st.success("✅ **Prediction: HAM (Safe)** — This looks like a legitimate message.")
    else:
        st.warning("Please type a message first!")