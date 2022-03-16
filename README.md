# simple ocr

## setup python environment

start your py virtualenv

```console
virtualenv -p python3 venv
source venv/bin/activate
pip install -r requirements.txt
```

## setup apache-tika

### tika option 1 (installing locally)

install tika + system req

```console
wget https://archive.apache.org/dist/tika/2.3.0/tika-server-standard-2.3.0.jar
sudo apt-get update
sudo apt-get install tesseract-ocr
sudo apt-get install tesseract-ocr-por
```

run tika server in another terminal (or in detached mode [&])

```console
java -jar tika-server-standard-2.3.0.jar -h 0.0.0.0
```

### tika option 2 (docker)

```console
docker pull apache/tika:2.3.0-full
docker pull apache/tika:2.3.0
```

```console
docker run -it \
    --name tika-server-ocr \
    -d \
    -p 9998:9998 \
    apache/tika:2.3.0-full
docker run -it \
    --name tika-server \
    -d \
    -p 9997:9998 \
    apache/tika:2.3.0

docker exec -it tika-server-ocr /bin/bash
apt-get update
apt-get install tesseract-ocr-por
```

## executing script

```console
python parse_cnh.py
```

------------------------------------------

references:

https://tika.apache.org/

https://cwiki.apache.org/confluence/display/tika/TikaOCR

https://medium.com/@masreis/text-extraction-and-ocr-with-apache-tika-302464895e5f
