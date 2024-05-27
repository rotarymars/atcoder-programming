SRC = ./main.cpp
BIN = ./a.exe
DEBUG_BIN = ./debug.exe
SAMPLE = ./test/sample-1.in
all: $(BIN) $(SAMPLE)
	./test-sample.sh $(BIN) $(SRC)
debugall: $(DEBUG_BIN) $(SAMPLE)
	./test-sample.sh $(DEBUG_BIN) $(SRC)
$(BIN): $(SRC)
	g++ -std=gnu++23 -o $(BIN) $(SRC)
$(DEBUG_BIN): $(SRC)
	g++ -std=gnu++23 -o $(DEBUG_BIN) $(SRC)
$(SAMPLE):
	python ../download.py