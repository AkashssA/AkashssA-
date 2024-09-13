# import streamlit as st
# from PIL import Image

# # Set the title of the app
# st.title("Enhanced Calculator")

# # Create two number input widgets
# num1 = st.number_input("Enter the first number", value=0)
# num2 = st.number_input("Enter the second number", value=0)

# # Initialize session state for recent calculations
# if 'history' not in st.session_state:
#     st.session_state.history = []

# # Function to perform calculations
# def add_numbers(x, y):
#     return x + y

# def subtract_numbers(x, y):
#     return x - y

# def multiply_numbers(x, y):
#     return x * y

# def update_history(operation, result):
#     st.session_state.history.append(f"{operation}: {result}")

# # Buttons for operations
# col1, col2, col3 = st.columns(3)

# with col1:
#     if st.button("Add"):
#         result = add_numbers(num1, num2)
#         st.write(f"The sum is: {result}")
#         update_history(f"{num1} + {num2}", result)

# with col2:
#     if st.button("Subtract"):
#         result = subtract_numbers(num1, num2)
#         st.write(f"The difference is: {result}")
#         update_history(f"{num1} - {num2}", result)

# with col3:
#     if st.button("Multiply"):
#         result = multiply_numbers(num1, num2)
#         st.write(f"The product is: {result}")
#         update_history(f"{num1} * {num2}", result)

# # Display recent calculations
# st.subheader("Recent Calculations")
# if st.session_state.history:
#     for entry in st.session_state.history:
#         st.write(entry)
# else:
#     st.write("No recent calculations.")

# # Add an image
# st.subheader("Here's an Image")
# # image = Image.open("path_to_your_image.jpg")  # Replace with your image path
# # st.image(image, caption="Sample Image", use_column_width=True)

# st.file_uploader("Upload file")

import streamlit as st
import os
from PIL import Image

# Create a directory to store uploaded images
if not os.path.exists("uploaded_images"):
    os.makedirs("uploaded_images")

st.title("Photo Upload App")

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display the uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)
    
    # Save the uploaded image
    save_path = os.path.join("uploaded_images", uploaded_file.name)
    with open(save_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
    st.success(f"Image saved at: {save_path}")

# Display all uploaded images
st.header("Uploaded Images")
for image_file in os.listdir("uploaded_images"):
    image_path = os.path.join("uploaded_images", image_file)
    st.image(Image.open(image_path), caption=image_file, use_column_width=True)