
#atenção!,use ponto para separar os minutos das horas

horas = float(input('que horas são? atenção!,use ponto para separar os minutos das horas  '))

if horas >=0 and horas <6:
    print("boa madrugada,tenha uma ótima madrugada!")

elif horas >=6 and horas <12:
    print("bom dia, tenha uma ótima manhã!")
elif horas >=12 and horas <18:
    print("boa tarde,tenha uma ótima tarde!")

elif horas >= 18  and horas <24:
    print("boa noite,tenha uma ótima noite!")

else:
    print("por favor,verifique a formatação digitada e tente novamente ")