print('CÁLCULO DE MASSA DE AGENTE CO2 CONFORME VdS 2093, CEA 4007, APSAD R13\n\nv1.0 04/22 - Manesco\n\nInstruções:\n- Separe os valores por espaço;\n- Utilize "." para casas decimais.\n')
outro_trecho = True

vol_total = 0.00
sup_total = 0.00
mas_total = 0.00

kb = 1.50

while outro_trecho:
    l, a, c = input('Insira Dimensões do Trecho: (L A C): ').split()

    l = float(l)
    a = float(a)
    c = float(c)

    vol = a * l * c                                                         ## CALCULO VOLUME DO TRECHO
    sup = 2.00 * ((c * l) + (c * a) + (l * a))                              ## CALCULO SUPERFICIE DO TRECHO
    mas = kb * ((0.75 * vol) + (0.20 * sup))                                ## CALCULO MASSA CO2

    vol_total = vol_total + vol
    sup_total = sup_total + sup
    mas_total = mas_total + mas

    opcao = input('Existem Mais Trechos? (s/n): ')

    if opcao != 's':
        outro_trecho = False

print('\nVolume Total = %.3f' % vol_total, 'm³')
print('Superfície Total = %.3f' % sup_total, 'm²')
print('Massa Total = %.3f' % mas_total, 'kg')
print('Considerando fator Kb = 1.50\n')

if mas_total <= 10:
    print('Utilizar Cilindro de CO² de 10kg\n')
else:
    if mas_total >= 10 and mas_total <=20:
        print('Utilizar Cilindro de CO² de 20kg\n')
    else:
        print('Utilizar Cilindro de CO² de 30kg\n')

input('Pressione "ENTER" para sair...')