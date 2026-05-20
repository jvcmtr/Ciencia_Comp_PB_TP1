from algoritimos import bublesort, insertionsort, selectionsort
from time import time

nome_arquivo = "lista_arquivos.txt"


def test(name, func):
	print(f"Executando {name}")
	inicio = time()
	result = func()
	fim = time()
	t = fim - inicio
	print(f"-> {name} concluído em: {t:.4f} segundos.\n")
	return t

if __name__ == "__main__":
	with open(nome_arquivo, "r", encoding="utf-8") as f:
	   txt = [linha.strip() for linha in f if linha.strip()]

	if not txt:
		raise Exception("Falha ao carregar o arquivo")

	tempo_bubble = test("Buble Sort", lambda: bublesort(txt))
	tempo_selection = test("Selection Sort", lambda: selectionsort(txt))
	tempo_insertion = test("Insertion Sort", lambda: insertionsort(txt))

	with open("relatorio.txt", "w", encoding="utf-8") as relatorio:
		relatorio.write(f"Quantidade de arquivos ordenados: {len(txt)}\n\n")
		relatorio.write(f"Bubble Sort:    {tempo_bubble:.4f} segundos\n")
		relatorio.write(f"Selection Sort: {tempo_selection:.4f} segundos\n")
		relatorio.write(f"Insertion Sort: {tempo_insertion:.4f} segundos\n")

	print("Relatório gerado com sucesso!")
