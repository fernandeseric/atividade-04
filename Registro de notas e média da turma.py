quantidade = int(input("Quantos alunos existem na turma: "))
soma = 0

for i in range(quantidade):
    nota = float(input(f"Digite a nota do aluno {i+1}: "))
    soma = soma + nota

media = soma / quantidade

print("Total de alunos:", quantidade)
print("Média da turma:", round(media, 2))




