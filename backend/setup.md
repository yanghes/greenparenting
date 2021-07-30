## Setup Ubuntu 20.04

apt update
apt -y upgrade
python3 -V
apt install -y python3-pip
apt install -y build-essential libssl-dev libffi-dev python3-dev
apt-get install ffmpeg libsm6 libxext6  -y
apt-get install tesseract-ocr
tesseract -v
pip3 install pillow
pip3 install pytesseract
pip3 install opencv-python
pip3 install CherryPy
pip3 install pandas
