import streamlit as st
from collections import Counter
import re

st.set_page_config(
    page_title="Text Analysis",
    page_icon="📝",
    layout="centered"
)

st.title("📝 Text Analysis")

st.write(
    "Analyze text and calculate words, characters, "
    "vowels, and repeated words."
)

text = st.text_area(
    "Enter your text:",
    height=200,
    placeholder="Type or paste your text here..."
)

if st.button("Analyze Text"):

    if not text.strip():
        st.warning("Please enter some text.")

    else:
        # Convert text to lowercase
        clean_text = text.lower()

        # Extract words
        words = re.findall(r"\b[a-zA-Z]+\b", clean_text)

        # Word count
        word_count = len(words)

        # Character count
        character_count = len(text)

        # Character count excluding spaces
        characters_without_spaces = len(
            text.replace(" ", "").replace("\n", "")
        )

        # Vowels
        vowels = "aeiou"

        vowel_count = sum(
            1 for char in clean_text
            if char in vowels
        )

        # Individual vowel frequency
        vowel_frequency = {
            vowel: clean_text.count(vowel)
            for vowel in vowels
        }

        # Word frequency
        word_frequency = Counter(words)

        # Repeated words
        repeated_words = {
            word: count
            for word, count in word_frequency.items()
            if count > 1
        }

        # Display results
        st.subheader("📊 Analysis Results")

        col1, col2 = st.columns(2)

        with col1:
            st.metric("Total Words", word_count)
            st.metric("Total Vowels", vowel_count)

        with col2:
            st.metric("Total Characters", character_count)
            st.metric(
                "Characters Without Spaces",
                characters_without_spaces
            )

        st.subheader("🔤 Vowel Frequency")

        st.write(vowel_frequency)

        st.subheader("🔁 Repeated Words")

        if repeated_words:
            st.write(repeated_words)
        else:
            st.info("No repeated words found.")