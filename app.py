from flask import Flask, request, jsonify, render_template
import os
import pdfplumber
import pytesseract
from PIL import Image
import google.generativeai as genai
from werkzeug.utils import secure_filename

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

ALLOWED_EXTENSIONS = {"pdf", "png", "jpg", "jpeg"}

genai.configure(api_key="YOUR_GEMINI_API_KEY")

model = genai.GenerativeModel("gemini-1.5-flash")


def allowed(filename):
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


def extract_pdf(path):
    text = ""

    with pdfplumber.open(path) as pdf:
        for page in pdf.pages:
            t = page.extract_text()
            if t:
                text += t + "\n"

    return text


def extract_image(path):
    img = Image.open(path)
    text = pytesseract.image_to_string(img)
    return text


def analyze(text):
    prompt = f"""
You are an expert Social Media Marketing Assistant.

Analyze the following social media content.

Return

1. Engagement Score (/10)

2. Tone

3. Readability

4. Weaknesses

5. Suggested Hashtags

6. Better CTA

7. Improved Version

Content:

{text}
"""

    response = model.generate_content(prompt)
    return response.text


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload():

    if "file" not in request.files:
        return jsonify({"error": "No File Uploaded"}), 400

    file = request.files["file"]

    if file.filename == "":
        return jsonify({"error": "Empty filename"}), 400

    if not allowed(file.filename):
        return jsonify({"error": "Unsupported file"}), 400

    filename = secure_filename(file.filename)
    path = os.path.join(app.config["UPLOAD_FOLDER"], filename)
    file.save(path)

    ext = filename.split(".")[-1].lower()

    try:
        if ext == "pdf":
            extracted = extract_pdf(path)
        else:
            extracted = extract_image(path)

        if extracted.strip() == "":
            return jsonify({"error": "No text detected"}), 400

        analysis = analyze(extracted)

        return jsonify({
            "text": extracted,
            "analysis": analysis
        })

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True)
