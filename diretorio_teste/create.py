from pathlib import Path

TOTAL_FILES = 10000

for i in range(1, TOTAL_FILES + 1):
    filename = Path(f"Arquivo_{i}.txt")
    filename.write_text(f"Este é o arquivo de exemplo numero {i}\n")

print(f"{TOTAL_FILES} arquivos criados")