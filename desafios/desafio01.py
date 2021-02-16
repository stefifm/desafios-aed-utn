print("Cantidad inicial de segundos a sus correspondientes horas")

#datos
iseg=36058
#proceso
seg_hora=60*60
ch=iseg//seg_hora
ts=iseg%seg_hora
cm=ts//60
cs=ts%60
#resultados
print("Cantidad de Horas", ch)
print("Minutos restantes", cm)
print("Segundos que quedan", cs)
