'''
Faça um Programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. 
Calcule e mostre o total do seu salário no referido mês, sabendo-se que são descontados 
11% para o Imposto de Renda, 8% para o INSS e 5% para o sindicato, faça um programa que nos dê:
  salário bruto.
  quanto pagou ao INSS.
  quanto pagou ao sindicato.
  o salário líquido.
  calcule os descontos e o salário líquido, conforme a tabela abaixo:
    + Salário Bruto : R$
    - IR (11%) : R$
    - INSS (8%) : R$
    - Sindicato ( 5%) : R$
    = Salário Liquido : R$  
  Obs.: Salário Bruto - Descontos = Salário Líquido.
'''

# função aqui
def calcular_salario(v1, v2):
  texto = """
    + Salário Bruto : R$ {:0.2f}
    - IR (11%) : R$ {:0.2f}
    - INSS (8%) : R$ {:0.2f}
    - Sindicato (5%) : R$ {:0.2f}
    = Salário Liquido : R$ {:0.2f}
    """
  texto = texto.format(100, 11, 8, 5, 76)
  return texto





def main():
  print(calcular_salario(1,3))
  # Após o teste passar criar a interface de usuário aqui

if __name__ == '__main__':
  main()