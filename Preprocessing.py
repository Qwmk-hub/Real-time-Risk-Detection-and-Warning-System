import os
import random
import shutil
from glob import glob

random.seed(42)

def split_dataset(image_dir, label_dir, output_dir, split_ratio=0.8):
    images = sorted(glob(os.path.join(image_dir, '*.jpg')))
    labels = sorted(glob(os.path.join(label_dir, '*.txt')))

    paired = list(zip(images, labels))
    random.shuffle(paired)

    split_idx = int(len(paired) * split_ratio)
    train_data = paired[:split_idx]
    test_data = paired[split_idx:]

    train_img_dir = os.path.join(output_dir, 'images/train')
    test_img_dir = os.path.join(output_dir, 'images/val')
    train_lbl_dir = os.path.join(output_dir, 'labels/train')
    test_lbl_dir = os.path.join(output_dir, 'labels/val')

    for d in [train_img_dir, test_img_dir, train_lbl_dir, test_lbl_dir]:
        os.makedirs(d, exist_ok=True)

    for img, lbl in train_data:
        shutil.copy(img, train_img_dir)
        shutil.copy(lbl, train_lbl_dir)

    for img, lbl in test_data:
        shutil.copy(img, test_img_dir)
        shutil.copy(lbl, test_lbl_dir)

    print(f"Train: {len(train_data)}, Val: {len(test_data)}")

if __name__ == "__main__":
    split_dataset(
        image_dir='dataset/images',
        label_dir='dataset/labels',
        output_dir='split_data',
        split_ratio=0.8
    )
