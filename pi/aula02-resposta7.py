t = int(input(""))
t_hora = t//3600
t_minuto = (t%3600)//60
t_segundo = (t%3600)%60

print(f"{t} segundos correspondem a {t_hora}:{t_minuto:02d}:{t_segundo:02d}.")