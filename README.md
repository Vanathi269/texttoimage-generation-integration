# Text-to-Image Generation Integration

This project is a simple web application that allows users to upload an image (in JPG format) and generate a caption for it using the Hugging Face `Salesforce/blip-image-captioning-large` model. The application is built with Streamlit.

## Features

- **Image Upload**: Users can upload a JPG image file through the web interface.
- **Caption Generation**: The uploaded image is sent to the Hugging Face API, which returns a caption describing the image.
- **Real-time Results**: The generated caption is displayed on the web page instantly.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- **Python 3.7 or higher** installed on your local machine.
- **pip** package installer.
- A **Hugging Face API token** for accessing the `Salesforce/blip-image-captioning-large` model.

## Installation

1. Clone this repository to your local machine:

    ```bash
    git clone https://github.com/yourusername/texttoimage-generation-integration.git
    cd texttoimage-generation-integration
    ```

2. Create a virtual environment (optional but recommended):

    ```bash
    python -m venv .venv
    source .venv/bin/activate  # On Windows use `.venv\Scripts\activate`
    ```

3. Install the required packages:

    ```bash
    pip install streamlit requests
    ```

4. Create a `.env` file (or simply edit the code) and add your Hugging Face API token:

    ```plaintext
    HUGGING_FACE_API_KEY=your_hugging_face_api_key_here
    ```

5. Replace the API key in the code with the one you received from Hugging Face.

## Usage

1. Run the Streamlit application:

    ```bash
    streamlit run caption.py
    ```

2. Open your web browser and navigate to `http://localhost:8501`.

3. Upload an image in JPG format using the "Upload an image" button.

4. Wait for the caption to be generated and displayed on the page.

## Code Explanation

- **`API_URL`**: The endpoint of the Hugging Face model API.
- **`headers`**: Authorization header with the Hugging Face API token.
- **`query(file)`**: Function that sends the image file to the API and returns the JSON response.
- **`st.file_uploader`**: Streamlit component for uploading image files.
- **`st.write(output)`**: Displays the API response (caption) on the webpage.

## Example

When you upload an image like `example.jpg`, the app will return a caption such as:

> "A dog running through a field."


