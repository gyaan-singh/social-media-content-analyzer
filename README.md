# Social Media Content Analyzer

## Overview

Social Media Content Analyzer is a Flask-based web application that extracts text from PDF and image files and analyzes the content using Google's Gemini AI. It helps users improve their social media posts by providing engagement suggestions, readability analysis, hashtag recommendations, and an improved version of the content.

---

## Features

- Upload PDF documents
- Upload image files (JPG, JPEG, PNG)
- Drag-and-drop file upload
- PDF text extraction using pdfplumber
- OCR text extraction using Tesseract OCR
- AI-powered content analysis using Gemini
- Engagement score
- Tone analysis
- Readability analysis
- Suggested hashtags
- Better Call-to-Action (CTA)
- Improved social media post
- Error handling
- Loading indicator

---

## Technologies Used

### Frontend
- HTML5
- CSS3
- JavaScript

### Backend
- Python
- Flask

### Libraries
- pdfplumber
- pytesseract
- Pillow
- Google Generative AI
- Werkzeug



## Project Structure


social-media-content-analyzer/
│
├── app.py
├── requirements.txt
├── README.md
│
├── templates/
│   └── index.html
│
├── static/
│   ├── style.css
│   └── script.js
│
└── uploads/






### Configure Gemini API Key

Create an environment variable:


GEMINI_API_KEY=YOUR_API_KEY


or configure it in your deployment platform (e.g., Render).


## Supported File Types

- PDF
- PNG
- JPG
- JPEG



## How It Works

1. Upload a PDF or image.
2. The application extracts text from the uploaded file.
3. PDFs are processed using pdfplumber.
4. Images are processed using Tesseract OCR.
5. The extracted text is sent to the Gemini AI model.
6. Gemini analyzes the content and returns:
   - Engagement score
   - Tone
   - Readability
   - Weaknesses
   - Suggested hashtags
   - Better CTA
   - Improved version
7. Results are displayed on the webpage.



## Future Improvements

- Support DOCX files
- Export analysis as PDF
- User authentication
- Analysis history
- Multiple language support
- Dark mode
- Improved OCR preprocessing

## License

This project is developed for educational and technical assessment purposes.
