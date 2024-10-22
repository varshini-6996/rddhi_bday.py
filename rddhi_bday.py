import streamlit as st
from PIL import Image

# Predefined password and clues
password = "undongi"  # Replace this with the actual password
clues = [
    "It's something you like to smack.",  # Clue 1
    "It belongs to me.",                   # Clue 2
    "Enter its Korean name (no spaces, only small letters, one word).",  # Clue 3
]

# Streamlit app
st.title("🎉 Hello my Yojaaaaa! 🎉")

# Display clues immediately on load
st.header("Password Clues")
for clue in clues:
    st.write(clue)  # Display each clue

# Login Section
st.header("Login")
login_password = st.text_input("Enter the password", type="password")  # User input for password

# Initialize session state for login
if 'logged_in' not in st.session_state:
    st.session_state.logged_in = False  # Track login status

if st.button("Login"):  # Button to submit the password
    if login_password == password:  # Check if entered password matches the predefined password
        st.session_state.logged_in = True  # Set login status to True
        st.success("🎉 Good job! You cracked it! 🎉")
    else:
        st.error("Incorrect password.")  # Error message for incorrect password

# After successful login
if st.session_state.logged_in:
    # Display all messages and images immediately after login
    st.header("Here's Your Birthday Surprise!")

    # Option 1 content
    st.subheader("One way or the other got to give this on a 18th birthday!")
    image_url_1 = "https://pbs.twimg.com/media/FP8YCQzacAAVUob.jpg:large"  # URL for Jungkook's image
    st.image(image_url_1, caption="Jungkook", use_column_width=True)
    st.write("You're officially 18!!!! lets work fucking hard and one day, 'see this emotion in 3D'[get it?] ")  # Message for Option 1

    # Option 2 content
    st.subheader("As always a little window of words through which you can see through my heart.")
    poem = poem = """\
A part of life is growing up,

and now I guess we might be too old to say waaassss uppp!

This part of life is surely gonna be tough,

but there's no fun when things are not rough.


Let's get through this together,

with the courage and skills we gather.

You have one of the purest souls I have ever seen,

such wonderful days there have been.


Now responsibilities are part of our lives,

it's like struggle and fear are our tormenting wives.

But there's nothing to fear,

when we are surrounded by our dear."""

    
    st.write(poem)  # Display the poem

    # Option 3 content
    st.subheader("THOSE WHERE THE DAY(cringy but true, quite frankly makes me seem old telling this.)")
    together_image_url = r"C:\Users\harsh\Downloads\WhatsApp Image 2024-10-22 at 21.10.19.jpeg"
  # Replace with a direct image URL of you both
    st.image(together_image_url, caption="Us Together!", use_column_width=True)
    
    # Input space for your message
    custom_message = st.text_area( "Happy Birthday, RDDHI! You mean the world to me!")  # Default message


# If not logged in, show clue for incorrect password attempts
else:
    # Handle the case where the user is not logged in
    if 'attempts' not in st.session_state:  # Initialize attempts if not already done
        st.session_state['attempts'] = 0
    st.session_state['attempts'] += 1  # Increment the number of attempts

    if st.session_state['attempts'] <= len(clues):  # Check if there are clues left
        st.write(f"Clue: {clues[st.session_state['attempts'] - 1]}")  # Display the corresponding clue
    else:
        st.write("No more clues left! Try again.")  # Message when no clues are left





















