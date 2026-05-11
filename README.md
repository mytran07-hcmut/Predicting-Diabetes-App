# 🩺 Diabetes Prediction App

Ứng dụng web sử dụng **Machine Learning** để dự đoán một người có khả năng mắc bệnh tiểu đường hay không dựa trên 8 chỉ số sức khỏe do người dùng cung cấp.

Dự án được xây dựng với:

* **Scikit-learn** để huấn luyện mô hình học máy.
* **FastAPI** để triển khai mô hình dưới dạng REST API.
* **Streamlit** để xây dựng giao diện người dùng trực quan.

---

## 📌 Giới thiệu dự án

Tiểu đường (Diabetes) là một bệnh mãn tính phổ biến và có thể gây ra nhiều biến chứng nguy hiểm nếu không được phát hiện sớm.

Ứng dụng này cho phép người dùng nhập vào 8 chỉ số y tế quan trọng, sau đó mô hình Machine Learning sẽ dự đoán:

* **1** → Có khả năng mắc bệnh tiểu đường.
* **0** → Không có khả năng mắc bệnh tiểu đường.

---

## 🎯 Mục tiêu của dự án

* Xây dựng mô hình Machine Learning để phân loại bệnh tiểu đường.
* Triển khai mô hình dưới dạng API bằng FastAPI.
* Xây dựng giao diện web thân thiện với Streamlit.
* Kết nối frontend và backend để tạo thành một ứng dụng hoàn chỉnh.

---

## 🏗️ Cấu trúc thư mục dự án

```text
Diabetes Prediction App/
│── app.py                  # Giao diện người dùng Streamlit
│── server.py               # FastAPI backend
│── classification.py       # Huấn luyện mô hình Machine Learning
│── inference.py            # Kiểm thử dự đoán cục bộ
│── model.pkl               # Mô hình đã huấn luyện và scaler
│── diabetes.csv            # Bộ dữ liệu
│── diabetes_report.html    # Báo cáo phân tích dữ liệu (EDA)
│── .gitignore
└── README.md
```

---

## 🧠 Quy trình xây dựng mô hình

### 1. Thu thập dữ liệu

Dự án sử dụng bộ dữ liệu **Pima Indians Diabetes Dataset** với biến mục tiêu `Outcome`:

* `Outcome = 1`: Có bệnh tiểu đường.
* `Outcome = 0`: Không mắc bệnh.

### 2. Tiền xử lý dữ liệu

* Kiểm tra và xử lý dữ liệu thiếu.
* Chuẩn hóa dữ liệu bằng `StandardScaler`.
* Chia dữ liệu thành tập train/test.

### 3. Huấn luyện mô hình

Mô hình phân loại được huấn luyện bằng Scikit-learn.

### 4. Lưu mô hình

Mô hình và scaler được lưu trong file:

```python
model.pkl
```

### 5. Triển khai API

FastAPI sẽ tải mô hình từ `model.pkl` và cung cấp endpoint `/predict` để dự đoán.

---

## 📊 Các đặc trưng đầu vào

| Tên biến                 | Mô tả                            |
| ------------------------ | -------------------------------- |
| Pregnancies              | Số lần mang thai                 |
| Glucose                  | Nồng độ glucose trong máu        |
| BloodPressure            | Huyết áp tâm trương (mm Hg)      |
| SkinThickness            | Độ dày lớp da (mm)               |
| Insulin                  | Nồng độ insulin (mu U/ml)        |
| BMI                      | Chỉ số khối cơ thể               |
| DiabetesPedigreeFunction | Chỉ số di truyền bệnh tiểu đường |
| Age                      | Tuổi                             |

---

## 🔄 Luồng hoạt động của hệ thống

1. Người dùng nhập 8 chỉ số sức khỏe trên giao diện Streamlit.
2. Streamlit gửi dữ liệu đến API FastAPI.
3. FastAPI tải mô hình đã huấn luyện.
4. Mô hình đưa ra kết quả dự đoán.
5. Kết quả được hiển thị trên giao diện.

---

## 📦 Cài đặt dự án

### 1. Clone repository

```bash
git clone <your-repository-url>
cd "Diabetes Prediction App"
```

### 2. Tạo môi trường ảo

```bash
python -m venv venv
```

### 3. Kích hoạt môi trường ảo

#### Windows

```bash
venv\Scripts\activate
```

#### macOS/Linux

```bash
source venv/bin/activate
```

### 4. Cài đặt thư viện cần thiết

```bash
pip install fastapi uvicorn streamlit requests scikit-learn pandas numpy
```

---

## ▶️ Chạy ứng dụng

### Bước 1: Khởi động FastAPI

```bash
uvicorn server:app --reload
```

Sau khi chạy, API sẽ hoạt động tại:

* `http://127.0.0.1:8000`
* Swagger Docs: `http://127.0.0.1:8000/docs`

### Bước 2: Khởi động Streamlit

Mở terminal mới và chạy:

```bash
streamlit run app.py
```

---

## 🔌 API Endpoint

### `POST /predict`

#### Request Body

```json
{
  "Pregnancies": 2,
  "Glucose": 120,
  "BloodPressure": 70,
  "SkinThickness": 20,
  "Insulin": 80,
  "BMI": 25.0,
  "DiabetesPedigreeFunction": 0.5,
  "Age": 30
}
```

#### Response

```json
{
  "prediction": 0
}
```

---

## 🖥️ Giao diện Streamlit

Giao diện người dùng bao gồm:

* 8 ô nhập dữ liệu.
* Nút **Predict**.
* Kết quả hiển thị rõ ràng:

  * ✅ Không có dấu hiệu tiểu đường.
  * ⚠️ Có khả năng mắc bệnh tiểu đường.

---

## 📈 Báo cáo phân tích dữ liệu

File:

```text
diabetes_report.html
```

Bao gồm:

* Thống kê mô tả.
* Phân phối dữ liệu.
* Ma trận tương quan.
* Phát hiện dữ liệu thiếu.

---

## 🧪 Ví dụ dự đoán

| Biến                     | Giá trị |
| ------------------------ | ------: |
| Pregnancies              |       2 |
| Glucose                  |     120 |
| BloodPressure            |      70 |
| SkinThickness            |      20 |
| Insulin                  |      80 |
| BMI                      |    25.0 |
| DiabetesPedigreeFunction |     0.5 |
| Age                      |      30 |

**Kết quả:** `0` → Không có khả năng mắc bệnh tiểu đường.

---

## 🛠️ Công nghệ sử dụng

* Python 3.11+
* Scikit-learn
* Pandas
* NumPy
* FastAPI
* Uvicorn
* Streamlit
* Requests
* Pickle

---

## 📚 Kiến thức áp dụng

Dự án này giúp thực hành:

* Xây dựng mô hình phân loại với Machine Learning.
* Tiền xử lý và chuẩn hóa dữ liệu.
* Lưu và tải mô hình bằng Pickle.
* Tạo REST API với FastAPI.
* Thiết kế giao diện với Streamlit.
* Kết nối frontend và backend.

---

## 🔮 Hướng phát triển trong tương lai

* Hiển thị xác suất dự đoán.
* Bổ sung độ chính xác, precision, recall, F1-score.
* Đóng gói bằng Docker.
* Triển khai lên cloud.
* Hỗ trợ dự đoán hàng loạt từ file CSV.

---

## ⚠️ Lưu ý

Ứng dụng này chỉ phục vụ cho mục đích **học tập và nghiên cứu**.
Kết quả dự đoán không thay thế cho chẩn đoán y khoa chuyên nghiệp.

---

## 👩‍💻 Tác giả

**Tran Jessica**

Nếu bạn thấy dự án hữu ích, hãy ⭐ repository để ủng hộ.

---

## 📄 License

Dự án được phát hành theo giấy phép **MIT License**.
