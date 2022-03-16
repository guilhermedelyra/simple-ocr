start your py virtualenv

```console
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

install system req

```console
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-por
```

run tika server in another terminal (or in detached mode [&])

```console
java -jar tika-server-standard-2.3.0.jar -h 0.0.0.0
```

execute script

```console
python parse_cnh.py
```


------------------------------------------

references:

https://tika.apache.org/
https://cwiki.apache.org/confluence/display/tika/TikaOCR
