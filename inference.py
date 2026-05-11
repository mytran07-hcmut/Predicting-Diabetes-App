import pickle

with open('model.pkl', 'rb') as f:
    model, scaler = pickle.load(f)

fake_input = [[2, 200, 70, 20, 100, 29.3, 0.5, 35]]
fake_input = scaler.transform(fake_input)

prediction = model.predict(fake_input)
print(prediction)