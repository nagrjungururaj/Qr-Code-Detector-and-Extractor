# Qr Code Detection and Extraction

This utility is for dealing with extracting the position and text of Qr code from an invoice

## Supported on
Preferably on Linux, upto Python 3.7. Works on Windows as well but have not tried running on it

## Installation
MongoDB Install Windows : [MongoDB Windows](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-windows/)

MongoDB install Linux : [MongoDB Linux](https://docs.mongodb.com/manual/tutorial/install-mongodb-on-ubuntu/)

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install requirements.txt

To install the Pyzbar package use 

```bash
sudo apt-get install libzbar0
```
and then execute the below.
```bash
pip install -r requirements.txt
```

## Usage
Start the mongo service

```bash
sudo systemctl start mongod
```
Run the Python script
```python
Ex:
python run.py -i sample_images/1.png
```
Stop the mongo service
```bash
sudo systemctl stop mongod
```

## Windows Error Message
If you see an ugly ImportError when importing pyzbar on Windows you will most likely need the Visual C++ Redistributable Packages for Visual Studio 2013. Install vcredist_x64.exe if using 64-bit Python, vcredist_x86.exe if using 32-bit Python.

## Contact
Email : nagarjun.gururaj@gmail.com
