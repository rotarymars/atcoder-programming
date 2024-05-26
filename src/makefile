SRC = ./main.cpp
BIN = ./a.exe
DEBUG_BIN = ./debug.exe
SAMPLE = ./test
all: $(BIN)
	./test-sample.sh $(BIN) $(SRC)
$(BIN): $(SRC)
	g++ -std=gnu++23 -o $(BIN) $(SRC)
$(DEBUG_BIN): $(SRC)
	g++ -std=gnu++23 -o $(DEBUG_BIN) $(SRC)
for_python:
	./test-sample.sh "python main.py" main.py