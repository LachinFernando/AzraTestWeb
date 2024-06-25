import streamlit as st

# set a title
st.title("My Test Web Page")

# set some tabs
text_tab, upload_tab, cam_tab = st.tabs(["Text Input", "Upload Image", "Cam Input"])

# first code the text input
with text_tab:
    st.title("Text Input")

    # text input
    text_input = st.text_input("Please Enter a Text Here")

    if text_input:
        st.subheader("Entered Text:")
        st.markdown("**{}**".format(text_input))

# second: code the upload tab
with upload_tab:
    file_uploader = st.file_uploader("Upload An Image", ["jpg", "jpeg", "png", "bmp"], help = "Upload an Image")

    if file_uploader:
        st.subheader("Uploaded Image")
        st.image(file_uploader)

# third: code the camera input
with cam_tab:
    cam_uploader = st.camera_input("Take a Picture")

    if cam_uploader:
        st.subheader("Camera Uploader")
        st.image(cam_uploader)