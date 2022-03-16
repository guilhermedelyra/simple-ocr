from tika import parser, unpack
import pdfbox

filename = "cnh.pdf"
headers = {
    "X-Tika-OCRLanguage": "por",
}

def extract_images():
    p = pdfbox.PDFBox()
    p.extract_images(filename)

def filter_content_and_write(raw, outfile):
    dirty_content = raw['content'].split('\n')
    content = "\n".join(list(filter(None, dirty_content)))
    with open(outfile, "w") as f:
        f.write(content)

def extract_text_from_pdf():
    raw = parser.from_file(filename, headers=headers)
    filter_content_and_write(raw, "cnh.txt")

def extract_text_from_images(image_path):
    text_path = image_path.split(".")[0] + ".txt"
    raw = parser.from_file(image_path, headers=headers)
    filter_content_and_write(raw, text_path)

extract_text_from_pdf()
extract_images()
for i in [2, 4]:
    extract_text_from_images(f"cnh-{i}.jpg")
