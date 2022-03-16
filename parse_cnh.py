from tika import parser, unpack
import pdfbox

filename = "cnh.pdf"

def extract_images():
    p = pdfbox.PDFBox()
    p.extract_images(filename)

def extract_text(image_path):
    text_path = image_path.split(".")[0] + ".txt"
    headers = {
        "X-Tika-OCRLanguage": "eng+por",
        "X-Tika-PDFextractInlineImages": "true"
    }
    raw = parser.from_file(image_path, headers=headers)

    dirty_content = raw['content'].split('\n')
    content = "\n".join(list(filter(None, dirty_content)))
    with open(text_path, "w") as f:
        f.write(content)

extract_images()
for i in [2, 4]:
    extract_text(f"cnh-{i}.jpg")