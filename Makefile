# Makefile for creating a standalone Windows executable using PyInstaller

# Variables
PYINSTALLER = pyinstaller
SCRIPT = bitvis/bitvis.py
ICON = bitvis/resources/bitvis.ico
OUTPUT_DIR = dist

# Default target
all: build

# Clean up build and dist directories
clean:
	rm -rf build/ $(OUTPUT_DIR)/ *.spec

# Build the executable
build:
	$(PYINSTALLER) --onefile --noconsole --icon=$(ICON) $(SCRIPT)

# Clean and rebuild
rebuild: clean build

.PHONY: all clean build rebuild
