'''PROGRAMA PARA CALCULAR VALOR DE FINANCIAMENTO.... 
CRIADO POR JACKSON
01.12.2023'''


valor_do_financiamento = float(input('DIGITE O VALOR DO FINANCIAMENTO: '))
parcelas = int(input('DIGITE A QUANTIDADE DE PARCELAS QUE DESEJA PAGAR: '))
taxa_juros = float(input('DIGITE A TAXA DE JUROS MENSAL: ')) / 100
vl_parcela = valor_do_financiamento * ((((1 + taxa_juros)**parcelas) *taxa_juros) / (((1 + taxa_juros)**parcelas) -1))
print('Valor da parcela: R$ {:.2f} em {}X, total financiamento {:.2f}'.format(vl_parcela,parcelas, vl_parcela*parcelas))
print('TOTAL DE JUROS {:.2f}'.format(vl_parcela*parcelas - valor_do_financiamento))

'''opcao = entrada = (input('DESEJA DA ALGUM VALOR DE ENTRADA? S/N' ))
opcao = opcao.upper()
if opcao == 's':
    print('ok')'''
    
    


