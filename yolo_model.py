from ultralytics import YOLO
import os

def train_yolo():
    model = YOLO("yolov8n.pt")
    model.train(
        data="data.yaml",
        epochs=100,
        imgsz=640,
        batch=16,
        project="runs/train",
        name="cctv_hazard_model"
    )

def run_inference(model_path, image_path):
    model = YOLO(model_path)
    results = model(image_path)
    results[0].show()
    results[0].save(filename="output.jpg")

if __name__ == "__main__":
    os.environ["WANDB_DISABLED"] = "true"
    train_yolo()
