from algoritimos import bublesort, insertionsort, selectionsort
from time import time, perf_counter_ns
import tracemalloc
from collections import deque

nome_arquivo = "lista_arquivos.txt"

def test_memory(name, func):
    print(f"Executando em {name}")

    tracemalloc.start()

    inicio = perf_counter_ns() # Tive que usar ns aqui ou se não ia retornar sempre 0
    result = func()
    t = perf_counter_ns() - inicio

    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"  -> Concluído em: {t} nanosegundos.")
    print(f"     Uso de memoria: {peak} bytes")
    return result, t, peak

def test(name, func):
	print(f"Executando {name}")
	inicio = time()
	result = func()
	fim = time()
	t = fim - inicio
	print(f"  -> Concluído em: {t:.4f} segundos.")
	return t

if __name__ == "__main__":
	arquivos = []
	with open(nome_arquivo, "r", encoding="utf-8") as f:
		temp = [linha.strip() for linha in f if linha.strip()]
		for ln in temp:
			for segment in ln.split(" "):
				if ".txt" in segment:
					arquivos.append(segment)

	if not arquivos:
		raise Exception("Falha ao carregar o arquivo")

	n = len(arquivos)

	print("_____________________")
	print("TESTES DO PROGRAMA 1")
	print(f"+ Testando ordenação de {n} itens:")
	tempo_bubble = test(f"Buble Sort", lambda: bublesort(arquivos))
	tempo_selection = test(f"Selection Sort", lambda: selectionsort(arquivos))
	tempo_insertion = test(f"Insertion Sort", lambda: insertionsort(arquivos))


	print("_____________________")
	print("TESTES DO PROGRAMA 2")
	print("___")
	print(f"+ Uso de memoria e tempo de inserção de {n} itens")
	hashtable, h_time, h_mem = test_memory(f"Hashtable", lambda: {i: item for i, item in enumerate(arquivos)})
	stack, s_time, s_mem = test_memory(f"Stack", lambda: list(arquivos))
	queue, q_time, q_mem = test_memory(f"Queue", lambda: deque(arquivos))

	print("___")
	print(f"+ Uso de memoria e tempo de leitura dos itens:")
	targets = [1, 100, 1000, 5000]

	results = {}
	for t in targets:
		print("___")
		print(f"+ Realizando busca pelo item {t}")
		results[ f"H{t}" ] = test_memory(f"Hashtable ({t})", lambda: hashtable.get(t) )
		results[ f"S{t}" ] = test_memory(f"Stack ({t})", lambda: stack[t])
		results[ f"Q{t}" ] = test_memory(f"Queue ({t})", lambda: queue[t]) 


	with open("relatorio.txt", "w", encoding="utf-8") as relatorio:
		relatorio.write(f"PROGRAMA 1: Tempo de execução dos algoritimos\n")
		relatorio.write(f"Quantidade de arquivos ordenados: {len(arquivos)}\n\n")
		relatorio.write(f"Bubble Sort:    {tempo_bubble:.4f} segundos\n")
		relatorio.write(f"Selection Sort: {tempo_selection:.4f} segundos\n")
		relatorio.write(f"Insertion Sort: {tempo_insertion:.4f} segundos\n")

		relatorio.write(f"\n---\n\n")
		relatorio.write(f"PROGRAMA 2: Tempo de execução e uso de memoria em estruturas de dados\n")
		relatorio.write(f"\n")
		relatorio.write(f"Inserção de {len(arquivos)} itens:\n")
		relatorio.write(f"Estrutura   | Tempo de execução \t  \t  \t| Pico no no consumo de memoria\n")
		relatorio.write(f"HashTable:  | {h_time} nanosegundos \t  \t  \t| {h_mem} bytes \n")
		relatorio.write(f"Stack:      |  {s_time} nanosegundos \t  \t  \t| {h_mem} bytes \n")
		relatorio.write(f"Queue:      |  {q_time} nanosegundos \t  \t  \t| {h_mem} bytes \n")

		for t in targets:
			relatorio.write(f"\nLeitura do item no indice {t}\n")
			relatorio.write(f"Estrutura   | Tempo de execução \t  \t  \t| Pico no no consumo de memoria\n")
			relatorio.write(f"HashTable:  | {results[f'H{t}'][1]} nanosegundos  \t  \t  \t| {results[f'H{t}'][2]} bytes \n")
			relatorio.write(f"Stack:      | {results[f'S{t}'][1]} nanosegundos  \t  \t  \t| {results[f'S{t}'][2]} bytes \n")
			relatorio.write(f"Queue:      | {results[f'Q{t}'][1]} nanosegundos  \t  \t  \t| {results[f'Q{t}'][2]} bytes \n")

	print("Relatório gerado com sucesso!")
