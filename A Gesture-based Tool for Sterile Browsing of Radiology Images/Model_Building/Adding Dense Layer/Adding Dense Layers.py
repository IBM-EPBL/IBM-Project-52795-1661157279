model.add(Dense (units=128, activation='relu'))
model.add(Dense (units=6, activation='softmax'))
model.summary()