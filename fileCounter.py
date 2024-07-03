import os

def count_files_and_directories(directory):
    total_files = 0
    total_dirs = 0

    for root, dirs, files in os.walk(directory):
        total_files += len(files)
        total_dirs += len(dirs)

    return total_files, total_dirs

# Podaj ścieżkę do zaznaczonego folderu
folder_path = r'C:\Users\xxxxx\Desktop\xxxxx'

# Policz pliki i foldery
file_count, dir_count = count_files_and_directories(folder_path)

print(f"Liczba plików we wszystkich folderach: {file_count}")
print(f"Liczba folderów: {dir_count}")
