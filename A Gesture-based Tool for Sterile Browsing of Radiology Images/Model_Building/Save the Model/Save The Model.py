model.save('gesture.h5')
model_json = model.to_json()
with open("model-bw.json", "w") as json_file:json_file.write(model_json)