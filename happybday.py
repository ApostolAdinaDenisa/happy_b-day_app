import streamlit as st
import matplotlib.pyplot as plt

# Fundal și stil simplu
st.markdown(
    """
    <style>
    .stApp {
        background-color: #ffccff;
        color: #800080;
        text-align: center;
        font-family: 'Comic Sans MS', cursive, sans-serif;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Titlu
st.title("🎉 Happy Birthday, Garlisma!! 🎂")

# Mesaj special
st.markdown("## Wishing you an amazing day filled with love and joy! 💖")

# Grafic cu "How much I love you" la maxim
st.subheader("How much I love you 💕")

fig, ax = plt.subplots(figsize=(6, 4))
values = [100]
labels = ['Love Level']
bars = ax.bar(labels, values, color='#ff66cc')
ax.set_ylim(0, 120)

# Adaugă valoarea pe bară
for bar in bars:
    height = bar.get_height()
    ax.text(bar.get_x() + bar.get_width()/2, height + 3, f'{height}%', ha='center', va='bottom', fontsize=14, color='#800080')

# Fără linii inutile
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.spines['left'].set_visible(False)
ax.yaxis.set_visible(False)

st.pyplot(fig)

# Mesaj final
st.markdown("---")
if st.button("Press me!"):
    st.balloons()
    st.success("Happy Birthday again, Garlisma! You are loved to the moon and back! 🌙💜")
