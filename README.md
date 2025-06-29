# Real-time-Risk-Detection-and-Warning-System
# 🛡️ YOLO 기반 실시간 위험 감지 및 경고 시스템

본 프로젝트는 YOLO 객체 탐지 알고리즘을 활용하여 CCTV 기반의 실시간 위험 요소를 탐지하고, 경고 시스템을 구축하는 것을 목표로 합니다. 다양한 물체 인식을 통해 **경계 침입, 이상행동 감지**와 같은 보안 상황에 빠르게 대응할 수 있습니다.

---

## 📌 프로젝트 개요

- **주제**: YOLO 객체 탐지 알고리즘을 활용한 보안 감시 시스템 구축
- **목표**: 실시간 CCTV 영상에서 위험 요소를 탐지하고 경고 신호 제공
- **활용 알고리즘**: YOLOv5
- **기술 스택**: Python, OpenCV, YOLOv5, LabelImg, PyTorch
- **응용 분야**: 산업 시설, 공공기관, 학교, 공항 등 경계 보안 강화

---

## 📂 데이터 수집 및 전처리

- 📸 CCTV에서 캡처된 이미지 기반으로 구성
- 📍 위험 객체: 사람, 가방, 박스, 전선 등
- 🏷️ 데이터 라벨링 도구: `LabelImg` 사용  
  → YOLO 형식 `.txt`로 저장 (`class x_center y_center width height`)

---

## 📦 YOLO 모델 학습 과정

### ⚙️ 학습 환경 설정
- PyTorch 환경 기반
- GPU 가속 지원
- 커스텀 데이터셋에 맞춰 `yaml` 설정

```bash
python train.py --img 640 --batch 16 --epochs 100 --data custom.yaml --weights yolov5s.pt
```

### 💡 학습 전략
- 기본 `yolov5s` 모델 사용
- Pre-trained weights 기반 transfer learning 적용
- Train/Validation split: 80:20
- Epoch 진행에 따라 loss 감소 및 정확도 향상 관찰

---

## 📈 탐지 결과 예시

YOLO 모델은 CCTV 영상 속 사람 및 위험 요소를 다음과 같이 탐지합니다:

- `image_05`: 1 warning, 2 safe 감지
- 노란 박스: 위험 예측
- 파란 박스: 정상 상태로 예측
- bbox는 confidence score 기반 시각화

---

## 🔍 EDA (탐지 결과 통계)

| image ID   | warning | safe |
|------------|---------|------|
| image_01   |   1     |  0   |
| image_05   |   1     |  2   |
| image_10   |   1     |  2   |
| ...        |   ...   | ...  |

- 각 이미지에서 탐지된 객체 수 요약
- 이상 행동(경고) 빈도 확인 가능

---

## 🧪 성능 평가 및 한계점

### ❗️ 탐지 오류 사례

- ✅ 정상 탐지: `person`, `laptop`, `handbag`
- ❌ 오탐지:
  - `person` → `horse`
  - `person` → `bird`
  - `skis`, `horse` 등 실제 존재하지 않는 객체 감지
- ❌ 미탐지: 확실한 객체가 탐지되지 않음 (`person` 누락)

---

## 💡 개선 제안

- 데이터셋의 **다양성 및 양** 부족 → 성능 저하
- ✅ 더 많은 이미지를 확보하여 Train/Test 재구성 시 **정확도 향상 가능**
- ✅ 탐지 실패를 줄이기 위해 **멀리서 촬영한 이미지**도 포함
- ✅ 파란선(정상 탐지)과 노란선(위험 탐지) 구분 명확화 필요

---

## 📁 코드 예시 (데이터 분할)

```python
# 데이터 분할 코드
copy_files(train_data, train_image_dir, train_label_dir)
copy_files(test_data, test_image_dir, test_label_dir)

print(f"Train: {len(train_data)} images and labels")
print(f"Test: {len(test_data)} images and labels")
```

출력:
```
Train: 54 images and labels  
Test: 14 images and labels  
Data split and saved to /Users/parksung-cheol/Desktop/CCTV/split_data
```

---

## ✅ 결론

### YOLO 알고리즘은 CCTV 보안 유지에 **상당히 효율적**임

- 경계 침입 및 이상 상황을 실시간으로 탐지 가능
- 공공장소, 공항, 공장 등에서 보안 효율성 향상 기대
- 다양한 객체 탐지를 통한 보안 적용 확장성 확보

> 💬 **"You Only Live Once"**  
YOLO의 이름처럼, 실시간 감시에서의 단 한 번의 판단이 중요한 만큼 신뢰할 수 있는 탐지 성능 확보가 필수입니다.
