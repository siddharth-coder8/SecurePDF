import streamlit as st
import PyPDF2
from io import BytesIO

st.title('PDF Encryptor')
st.text('By Siddharth Shah')
st.text('SVECTOR')
def encrypt_pdf(input_buffer, password):
    pdf_reader = PyPDF2.PdfReader(input_buffer)
    pdf_writer = PyPDF2.PdfWriter()

    for page in pdf_reader.pages:
        pdf_writer.add_page(page)

    pdf_writer.encrypt(password)

    output_buffer = BytesIO()
    pdf_writer.write(output_buffer)
    return output_buffer

uploaded_file = st.file_uploader("Choose a PDF file", type=['pdf'])
st.text('We do not store any uploaded PDFs in our database.')
st.text('All PDFs generated with passwords are end-to-end encrypted with no loopholes.')
if uploaded_file:
    st.title('Encryption Settings')
    password = st.text_input('Enter Password', type='password')
    encrypt_button = st.button('Encrypt PDF')

    if encrypt_button and password:
        encrypted_pdf = encrypt_pdf(uploaded_file, password)

        st.success('PDF encrypted successfully!')
        st.download_button('Download Encrypted PDF', encrypted_pdf, file_name='encrypted_pdf.pdf', mime='application/pdf')
