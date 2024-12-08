# 🎨 ImaginAItion: A Text-to-Image Generation Application

ImaginAItion is a cutting-edge application that leverages AI-powered Stable Diffusion to transform textual prompts into visually captivating images. This project consists of a **FastAPI backend** for image generation and a **Streamlit frontend** for an intuitive user interface.

---

## Table of Contents

1. [Features](#features)
2. [Requirements](#requirements)
3. [Installation](#installation)
4. [Usage](#usage)
5. [API Endpoints](#api-endpoints)
6. [Streamlit Frontend Features](#streamlit-frontend-features)
7. [Directory Structure](#directory-structure)
8. [Acknowledgments](#acknowledgments)

---

## Features

- **AI-Powered Image Generation**: Generate high-quality images from text prompts using Stable Diffusion.
- **Prompt History**: Save and view past prompts and corresponding generated images.
- **Download Images**: Easily download generated images from the frontend.
- **Responsive Design**: A modern, user-friendly interface built with Streamlit.
- **History Management**: View and clear prompt history directly from the frontend.
- **Health Monitoring**: Check the status of the backend service and the availability of hardware acceleration.

---

## Requirements

- **Python**: 3.8 or higher
- **Dependencies**:
  - `FastAPI`
  - `SQLAlchemy`
  - `Streamlit`
  - `torch`
  - `diffusers`
  - `Pillow`
  - `requests`

Ensure you have a compatible GPU for faster image generation, or fallback to CPU if unavailable.

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-repo/imaginAItion.git
cd imaginAItion
```

### 2. Set Up a Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Download the Stable Diffusion Model
The application uses the `runwayml/stable-diffusion-v1-5` model. Ensure you have internet access to download the model when running the backend for the first time.

---

## Usage

### Start the Backend Server
1. Navigate to the project directory.
2. Run the FastAPI app:
   ```bash
   uvicorn app:app --reload
   ```
   By default, the app will be available at `http://127.0.0.1:8000`.

### Start the Frontend
1. Open a new terminal in the project directory.
2. Run the Streamlit app:
   ```bash
   streamlit run frontend.py
   ```

   The frontend will open in your default browser at `http://localhost:8501`.

---

## API Endpoints

### 1. **`GET /`**
- **Description**: Welcome message for the API.
- **Response**:
  ```json
  {
      "message": "Welcome to the ImaginAItion API!"
  }
  ```

### 2. **`GET /health`**
- **Description**: Check the backend's health and device status.
- **Response**:
  ```json
  {
      "status": "healthy",
      "device": "cuda"
  }
  ```

### 3. **`GET /generate`**
- **Description**: Generate an image from a text prompt.
- **Query Parameters**:
  - `prompt` (str): The textual prompt for image generation.
- **Response**:
  - On success: Returns the generated image as a file.
  - On failure: Returns an error message.

### 4. **`GET /history`**
- **Description**: Retrieve the history of generated prompts and image paths.
- **Response**:
  ```json
  [
      {
          "id": 1,
          "prompt": "A futuristic cityscape",
          "image_path": "./generated_images/1234abcd.png"
      }
  ]
  ```

### 5. **`DELETE /history`**
- **Description**: Clear all prompt history from the database.
- **Response**:
  ```json
  {
      "message": "Prompt history cleared successfully!"
  }
  ```

---

## Streamlit Frontend Features

### 1. **Title and Subtitle**
- A centered and beautifully styled title ("🎨 ImaginAItion") and subtitle ("Where words shape worlds—craft captivating visuals with the art of AI.").

### 2. **Service Status**
- A sidebar section displaying the health of the backend and the device used (e.g., CPU/GPU).

### 3. **Image Generation**
- Text input box for users to provide a prompt.
- A "✨ Generate Image" button to create images.
- Spinner animation while the image is being generated.

### 4. **Image Display and Download**
- Generated images are displayed with an option to download them.

### 5. **Prompt History**
- A grid view of previously generated images and their prompts.

### 6. **Clear History**
- A button to delete all history entries.

---

## Directory Structure

```plaintext
imaginAItion/
│
├── app.py               # Backend FastAPI application
├── frontend.py          # Streamlit frontend application
├── requirements.txt     # Python dependencies
├── generated_images/    # Directory for storing generated images
└── prompts.db           # SQLite database for prompt history
```

---

## Acknowledgments

This application uses the following:
- **[Hugging Face Diffusers](https://huggingface.co/docs/diffusers/)** for Stable Diffusion.
- **[FastAPI](https://fastapi.tiangolo.com/)** for building the backend API.
- **[Streamlit](https://streamlit.io/)** for the user-friendly frontend interface.
- **[PyTorch](https://pytorch.org/)** for running the Stable Diffusion model.

Enjoy creating stunning AI-generated visuals with **ImaginAItion**! 🌟

---

## Results

#### 1. Eiffel tower in fire

![Eiffel_tower_on_fire](https://github.com/user-attachments/assets/78ca5ac5-ee86-43cc-a423-f55aabb7f06f)

#### 2. A snowy mountain peak with northern light

![A_snowy_mountain_peak_under_a_starry_sky_with_the_Northern_Lights](https://github.com/user-attachments/assets/462eebe5-4594-4ae2-b4a4-15aaa817d7dd)

#### 3. Sunset in Antarctica

![sunset_in_antartica](https://github.com/user-attachments/assets/3474f504-79aa-4345-a250-7597c417850f)
