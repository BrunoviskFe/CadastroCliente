#Importando o módulo notes
import notes
import datetime

#Cadastro do Cliente
nome = str(input('Nome Completo: '))
rgCliente = int(input('RG: '))
cpfCliente = int(input('CPF: '))
dataNascimento = int(input('Data de Nascimento: '))
ruaCliente = str(input('Rua: '))
numeroCasa = int(input('Numero: '))
bairro = str(input('Bairro: '))
telCliente = int(input('Telefone: '))
email = str(input('E-mail: '))
velocidade = int(input('Plano: '))

#Verifica se o plano precisará de modem Wi-Fi
if velocidade >= 450:
    modemWifi = str(input('Digite o Roteador em Comodato: '))

tipoInternet = str(input('Fibra ou Rádio? '))
valorPagamento = float(input('Valor a ser pago: '))
formaPagamento = str(input('Dinheiro, Debito ou Credito? '))
diaVenda = float(input('Dia da Venda: '))
prazoFinal = float(input('Prazo Final: '))



#Este comando abre um arquivo txt
arquivo = open("dados.txt", "w")

#Este bloco apresenta todos os dados no arquivo .txt
arquivo.write('Nome: {}    {}'.format(nome, dataNascimento))
arquivo.write("\n")
arquivo.write('RG: {:>}   CPF: {}'.format(rgCliente, cpfCliente))
arquivo.write("\n")
arquivo.write('Data: {}'.format(dataNascimento))
arquivo.write("\n")
arquivo.write('End: Rua {}, {} - {}'.format(ruaCliente, numeroCasa, bairro))
arquivo.write("\n")
arquivo.write('Telefone: {}'.format(telCliente))
arquivo.write("\n")
arquivo.write('E-mail: {}'.format(email))
arquivo.write("\n")
arquivo.write('Plano: {}MB - {}'.format(velocidade, tipoInternet ))
arquivo.write("\n")
arquivo.write('FP: R${:.2f} - {}'.format(valorPagamento, formaPagamento))
arquivo.write("\n")
arquivo.write('Venda: {:.0f}PF: {:.0f}'.format(diaVenda, prazoFinal))

#Ele realiza o fechamento do arquivo .txt
arquivo.close()
