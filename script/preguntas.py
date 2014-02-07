from datos.models import Pregunta

VARIABLES_FILE = '/home/mikel/open_data/deusto_barometro_social/variables.csv'

vf = open(VARIABLES_FILE)

for line in vf:
    sline = line.split(';')
    #print sline[4]
    if sline[0].startswith('P'):
        print sline[0], sline[4]
        pregunta = Pregunta(enunciado=sline[4], clave=sline[0])
        pregunta.save()

print 'fin'    
vf.close()
