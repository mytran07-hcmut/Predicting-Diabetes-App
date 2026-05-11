import pandas as pd
#from ydata_profiling import ProfileReport

#Thư viện để save model lại (đỡ train lại)
import pickle

#Sử dụng cho việc phân chia dữ liệu
from sklearn.model_selection import train_test_split, GridSearchCV

#Sử dụng cho việc tiền xử lý
from sklearn.preprocessing import StandardScaler

#Các model (thuật toán) sử dụng
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier

#Các metrics sử dụng
#from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
from sklearn.metrics import classification_report

#Sử dụng thư viện để dự đoán xem model nào đạt hiệu quả cao nhất
from lazypredict.Supervised import LazyClassifier


dataset = pd.read_csv('diabetes.csv') #Đọc dữ liệu từ file CSV vào DataFrame của pandas

#Truc quan hoa du lieu
#stats = dataset.describe()
#profile = ProfileReport(dataset, title="Diabetes Report")
#profile.to_file('diabetes_report.html') #Chuyển đổi báo cáo thành file HTML để dễ dàng xem trên trình duyệt

#Phan chia du lieu
target = 'Outcome' 
x = dataset.drop(target, axis=1) #
y = dataset[target]
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=1009) #Chia dữ liệu thành train set và test set với tỷ lệ 80:20

#Tien xu ly du lieu (chuan hoa du lieu)
# => Quan trọng cho hầu hết các thuật toán trong ML (các thuât toán dựa trên cây: decision tree, random forest,... không cần bước này)
scaler = StandardScaler()
x_train = scaler.fit_transform(x_train)
x_test = scaler.transform(x_test)

# #So sánh các model và dự đoán model hiệu quả nhất sử dụng LazyClassifier
# cls = LazyClassifier()
# models,predictions = cls.fit(x_train, x_test, y_train, y_test)

#Cai thien mo hinh
params = {
    "n_estimators": [50, 100, 200],
    "criterion": ["gini", "entropy", "log_loss"],
}
model = GridSearchCV(
    RandomForestClassifier(random_state=100), #Thuật toán sử dụng cho model
    param_grid=params, #Dict chứa các tham số để thử chạy thuật toán
    cv=6, #Số K fold được chia ra
    scoring="f1", #Metrics được chọn để đánh giá model
    verbose=1, #In thông tin của việc grid search
    n_jobs=6 #Số luồng xử lý mà CPU chia cho việc searching (càng nhiều thì càng tăng thời gian xử lý)
)


#Chon mo hinh & chon thuat toan
#model = LogisticRegression() #Chọn thuật toán LogisticRegression
#model = SVC() #Chọn thuật toán Support Vector Machine
#model = RandomForestClassifier() #Chọn thuật toán RandomForest

model.fit(x_train, y_train)

print(model.best_params_)
print(model.best_score_)

#Save model
with open('model.pkl', 'wb') as f:
    pickle.dump([model,scaler], f)

#Test mo hinh
y_predict = model.predict(x_test)

#Danh gia mo hinh bang metric
#print("Accuracy: {}".format(accuracy_score(y_test, y_predict))) #Sử dụng metric accuracy (tỉ lệ dự đoán đúng trên tổng dự đoán được mô hình đưa ra)
#print("Precision: {}".format(precision_score(y_test, y_predict)))
#print("Recall: {}".format(recall_score(y_test, y_predict)))
#print("F1 score: {}".format(f1_score(y_test, y_predict)))

print(classification_report(y_test, y_predict)) #Report kết quả của 4 metrics (precision, recall, f1, support)
