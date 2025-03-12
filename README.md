Japanese Furigana Annotation Tool

This is a web application built with Python + Django that adds furigana (振り仮名) annotations to Japanese text or text extracted from images, and extracts a list of verb base forms. Furigana for verbs is highlighted in red for easy learning and reading.
Features
Text Input: Enter Japanese text to automatically add hiragana annotations to kanji.

Image Processing: Upload images containing Japanese text, extract the text, and add furigana annotations (requires Tesseract OCR installation).

Verb Extraction: Identify verbs in the text and list their base forms.

Frontend Interaction: Adjust the font size of the output text, with a user interface enhanced by Bootstrap.

Tech Stack
Backend: Python, Django

Japanese Processing: Fugashi (Japanese tokenizer), Jaconv (kana conversion)

Image Processing: Pytesseract (OCR), PIL (image processing)

Frontend: HTML, Bootstrap 5, JavaScript

Installation Steps
Prerequisites
Python 3.11+ (recommended)

Git

Tesseract OCR (required for image text extraction; Windows users need to install it manually)

Installation Process
Clone the Repository
bash

git clone https://github.com/your-username/your-repository-name.git
cd your-repository-name

Create and Activate a Virtual Environment (optional but recommended)
bash

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

Install Dependencies
bash

pip install -r requirements.txt

Install Tesseract OCR (if processing images)
Windows: Download Tesseract, install it, and update the code with the path:
python

pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

Linux: sudo apt install tesseract-ocr tesseract-ocr-jpn

Mac: brew install tesseract-lang

Run the Django Project
bash

python manage.py runserver

Open your browser and visit http://127.0.0.1:8000/japan_kanji/.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------

日文假名注释工具
这是一个基于 Python + Django 的Web应用，用于为日文文本或图片中的日文内容添加假名注释（振り仮名），并提取动词的原形列表。动词的假名注释会以红色高亮显示，方便学习和阅读。
功能特点
文本输入：输入日文文本，自动为汉字添加平假名注释。

图片处理：上传包含日文的图片，提取文本并添加假名注释（需安装Tesseract OCR）。

动词提取：识别文本中的动词，并列出其原形。

前端交互：支持调整输出文本的字体大小，使用Bootstrap美化界面。

技术栈
后端：Python, Django

日文处理：Fugashi（日文分词器）, Jaconv（假名转换）

图片处理：Pytesseract（OCR）, PIL（图像处理）

前端：HTML, Bootstrap 5, JavaScript

安装步骤
前提条件
Python 3.11+（推荐）

Git

Tesseract OCR（用于图片文本提取，Windows用户需手动安装）

安装过程
克隆仓库
bash

git clone https://github.com/你的用户名/你的仓库名.git
cd 你的仓库名

创建并激活虚拟环境（可选但推荐）
bash

python -m venv venv
# Windows
venv\Scripts\activate
# Linux/Mac
source venv/bin/activate

安装依赖
bash

pip install -r requirements.txt

安装Tesseract OCR（若处理图片）
Windows：下载 Tesseract，安装后修改代码中的路径：
python

pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

Linux：sudo apt install tesseract-ocr tesseract-ocr-jpn

Mac：brew install tesseract-lang

运行Django项目
bash

python manage.py runserver

打开浏览器，访问 http://127.0.0.1:8000/japan_kanji/。

