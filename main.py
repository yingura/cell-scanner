from collections import defaultdict
from typing import Dict
from ultralytics import YOLO
from PIL import Image
import tifffile
import torch
from WhiteBloodCellDetector import WhiteBloodCellDetector

# SETUP GPU
device = "0" if torch.cuda.is_available() else "cpu"
if device == "0":
    torch.cuda.set_device(0)
###

# def process__ndpi(ndpi):
#     wbc = {"N": 0, "L": 0, "M": 0, "E": 0, "B": 0}
#     rbc = 0
#     for h in ndpi_height:
#         for w in ndpi_width:
#             image = ndpi.crop(height, width, height + 512, width + 512)
#             wbc = wbc | count_wbcs(image)  # merge 2 dictionaries
#             rbc += count_rbc(image)

#     generate_summary(wbcs, rbc)


if __name__ == '__main__':
    wbcDetector = WhiteBloodCellDetector("models/wbc-model-Feb24.pt", "models/wbc-classification-box-Sep23.pt")
    image = Image.open("samples/sample4.jpg")
    wbcs = wbcDetector.detect(image)
    print(wbcs)
    # for ndpi in folder:
    #     process__ndpi(ndpi)




            
