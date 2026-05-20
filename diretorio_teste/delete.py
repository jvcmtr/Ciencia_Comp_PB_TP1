from pathlib import Path

TOTAL_FILES = 10000
deleted = 0

for i in range(1, TOTAL_FILES + 1):
    filename = Path(f"Arquivo_{i}.txt")

    if filename.exists():
        filename.unlink()
        deleted += 1

print(f"{deleted} Arquivos deletados")