from ultralytics import YOLO

model = YOLO(r'./best.pt')

result = model.val(data=r'./LorisHead.yaml', epochs=100, imgsz=640)