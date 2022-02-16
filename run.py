from pyzbar import pyzbar
import cv2
import argparse
import pymongo

def detect_qr(img):
    # Detect qr code bbox and text using pyzbar
    codes = pyzbar.decode(img)
    box = [code.rect for code in codes]
    text = ["{} ({})".format(code.data.decode("utf-8"), code.type) for code in codes]
    return codes, box, text
    
## Main program starts here 
if __name__ == "__main__":

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--image", required=True, help="path to input image")
    args = vars(ap.parse_args())
    
    img = cv2.imread(args["image"])
    
    data = {}
    
    # Build dict response
    data["img"] = args["image"]
    data["Title"] = "Qr code OCR"
    codes, box, text = detect_qr(img)
    
    # Check if pyzbar detects any qr code or not
    if codes != []:
        data["Box_detected"] = "Yes"
        data["Box_coords"] = box
        data["OCR_text"] = text
        data["Text detected"] = "Yes"
        
        for barcode in codes:
            # Extract the bbox coords
            (x, y, w, h) = barcode.rect
            cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 2)
            # Extract the text detected by pyzbar
            barcodeData = barcode.data.decode("utf-8")
            barcodeType = barcode.type
            # draw the barcode data and barcode type on the image
            text = "{} ({})".format(barcodeData, barcodeType)
            cv2.putText(img, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX,
            0.5, (0, 0, 255), 2)
    else:
        data["Box_detected"] = "No"
        data["OCR_text"] = []
        data["Text detected"] = "No"

        cv2.putText(img, "No QR detected", (100, 100 - 10), cv2.FONT_HERSHEY_SIMPLEX,
        0.5, (0, 0, 255), 2)
    print(data)

    # cv2.imwrite("out.png", img)
    cv2.imshow("Image", img)
    cv2.waitKey(0)
    

    ## Push the data to Mongo using Pymongo

    myclient = pymongo.MongoClient("mongodb://localhost:27017/")

    #use database named "ocr"
    mydb = myclient["ocr"]

    #use collection named "qr_response"
    mycol = mydb["qr_response"]

    #insert a document to the collection
    x = mycol.insert_one(data)

    #id returned by insert_one
    print("Document inserted with id: ", x.inserted_id)

    print("\nDocuments in qr_response collection\n----------------------------------")
    #print all the documents in the collection
    for x in mycol.find():
        print(x)