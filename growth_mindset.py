import streamlit as st

# Page Configuration
st.set_page_config(page_title="Growth Mindset Challenges", page_icon="🌱", layout="wide")

# Header Section
st.title("🌱 Growth Mindset Challenges")
st.subheader("Overcome challenges and develop a growth mindset!")

st.write("A growth mindset helps you embrace challenges, learn from failures, and keep improving. Below are some challenges to help you develop resilience and a positive attitude.")

# Challenge Sections
challenges = {
    "💡 Learn Something New": "Pick a new skill (e.g., coding, painting) and practice it for 7 days.",
    "📖 Read a Book on Mindset": "Read 'Mindset' by Carol Dweck or any self-improvement book.",
    "📝 Daily Reflection": "Write 3 things you learned each day for a week.",
    "💪 Face a Fear": "Do something that scares you (public speaking, meeting new people, etc.).",
    "❌ Embrace Failure": "Try something difficult, fail, and learn from it without feeling bad."
}

# Display Challenges
for challenge, description in challenges.items():
    with st.expander(challenge):
        st.write(description)

# User Interaction
st.write("👉 **Which challenge will you take on?**")
challenge_choice = st.selectbox("Choose a challenge:", list(challenges.keys()))

if st.button("Accept Challenge"):
    st.success(f"Awesome! You have accepted the challenge: {challenge_choice} 🎯")

# Footer
st.write("---")
st.write("💬 *Share your progress and keep growing!*")

