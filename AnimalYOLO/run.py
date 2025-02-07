from ultralytics import YOLO
 
model = YOLO("./yolov8-all.yaml")
 
data = "./animals.yaml"
 
model.train(data=data, epochs=100, batch=8)