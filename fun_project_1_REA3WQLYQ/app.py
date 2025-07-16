import streamlit as st
import random
import time

st.set_page_config(page_title="Which Pastry Are You?", page_icon="🍰")

# --- Session state to track quiz state ---
if "show_result" not in st.session_state:
    st.session_state.show_result = False

if "name" not in st.session_state:
    st.session_state.name = ""

# --- Initial page title and name input ---
if not st.session_state.show_result and st.session_state.name == "":
    st.title("🍰 Which Pastry Are You?")
    st.write("Find your sweet career match!")

    name = st.text_input("What's your name?")
    if name:
        st.session_state.name = name
        st.rerun()

# --- Quiz UI ---
if not st.session_state.show_result and st.session_state.name:
    st.write(f"Hi **{st.session_state.name}**! Answer these fun questions to discover which dessert matches your personality — and what career path might suit you best!")

    st.subheader("1. Your work style is:")
    q1 = st.radio("", ["Calm & steady", "Fast & efficient",
                  "Creative & expressive", "Kind & social"], key="q1")

    st.subheader("2. When you're stressed:")
    q2 = st.radio("", ["Think step by step", "Take action fast",
                  "Make or draw something", "Talk to someone"], key="q2")

    st.subheader("3. Pick a flavor:")
    q3 = st.radio("", ["Coffee ☕", "Dark chocolate 🍫",
                  "Strawberry 🍓", "Vanilla 🍦"], key="q3")

    if st.button("Reveal My Pastry!"):
        with st.spinner("Whipping your result... 🍰"):
            time.sleep(2)
        st.session_state.answers = [q1, q2, q3]
        st.session_state.show_result = True
        st.rerun()

# --- Result display ---
if st.session_state.show_result:
    answers = st.session_state.answers

    quotes = {
        "A": [
            "Like a good tiramisu, you're calm, cool, and full of depth.",
            "Life is better with layers — just like you!"
        ],
        "B": [
            "Fast like éclair, sharp like a pro.",
            "You're the lightning in every bakery!"
        ],
        "C": [
            "Macarons don’t follow the rules — and neither do you.",
            "You're the icing on life’s cake."
        ],
        "D": [
            "Sweetness is your strength.",
            "You're everyone's comfort dessert."
        ]
    }

    scores = {"A": 0, "B": 0, "C": 0, "D": 0}

    score_map = {
        "Calm & steady": "A",
        "Think step by step": "A",
        "Coffee ☕": "A",
        "Fast & efficient": "B",
        "Take action fast": "B",
        "Dark chocolate 🍫": "B",
        "Creative & expressive": "C",
        "Make or draw something": "C",
        "Strawberry 🍓": "C",
        "Kind & social": "D",
        "Talk to someone": "D",
        "Vanilla 🍦": "D"
    }

    for answer in answers:
        result_letter = score_map.get(answer)
        if result_letter:
            scores[result_letter] += 1

    result = max(scores, key=scores.get)

    if result == "A":
        st.header("**You're a Tiramisu!**")
        st.image(
            "https://cdn.pixabay.com/photo/2019/03/14/19/02/tiramisu-4055650_1280.jpg")
        st.write("Calm, thoughtful, layered.")
        st.write("**Career match:** Researcher, Data Analyst, Developer, Writer")
    elif result == "B":
        st.header("**You're an Éclair!**")
        st.image(
            "https://cdn.pixabay.com/photo/2020/06/29/08/21/eclair-5351840_1280.jpg")
        st.write("Efficient, bold, fast-paced.")
        st.write("**Career match:** Entrepreneur, Project Manager, Event Coordinator")
    elif result == "C":
        st.heeader("**You're a Macaron!**")
        st.image(
            "https://cdn.pixabay.com/photo/2015/04/17/09/29/macarons-726983_1280.jpg")
        st.write("Creative, unique, and stylish.")
        st.write("**Career match:** Designer, Content Creator, Marketing Specialist")
    else:
        st.header("**You're a Short Cake!**")
        st.image(
            "https://cdn.pixabay.com/photo/2023/04/26/06/27/cake-7951680_1280.jpg")
        st.write("Warm, friendly, and people-loving.")
        st.write("**Career match:** Teacher, Counselor, HR, Community Support")

    st.success(random.choice(quotes[result]))

    if st.button("Try again"):
        st.session_state.clear()
        st.rerun()
