# JOEL: 
# 1. Capturar ruta de archivo input_file y label_index.  
# 2. Ejecutar el script
# 3. Guardar resultado en output_file (misma ruta y nombre que input_file+.libsvm)
#!/usr/bin/env python
"""
Convert CSV file to libsvm format. Works only with numeric variables.
Put -1 as label index (argv[3]) if there are no labels in your file.
Expecting no headers. If present, headers can be skipped with argv[4] == 1.
"""
import sys, csv, pandas as pd
from collections import defaultdict

def construct_line( label, line ):
	new_line = []
    
	if float( label ) == 0.0:
		label = "0"
        
	new_line.append( label )

	for i, item in enumerate( line ):
        
		if item == '' or float( item ) == 0.0:
            
			continue

		new_item = "%s:%s" % ( i + 1, item )
		new_line.append( new_item )
	new_line = " ".join( new_line )
	new_line += "\n"
	return new_line

# ---
#input_file  = sys.argv[1]
#output_file = sys.argv[2]
#%% 
input_file  = 'C:/Users/TUF-PC8/Google Drive/2018.12 work/datasets/csv/hepatitis/wmvalues/hepatitis.csv'
output_file = 'C:/Users/TUF-PC8/Google Drive/2018.12 work/datasets/csv/hepatitis/wmvalues/hepatitis.libsvm'
#output_file = 'C:/Users/Carlos Villaseñor/Google Drive/2018.12 work/datasets/csv/hepatitis.libsvm'

#try:
	#label_index = int( sys.argv[3] )
label_index = 19

#except IndexError:

#	label_index = 30

#try:
	#skip_headers = sys.argv[4]
   

#except IndexError:

#	skip_headers = 0


i = open( input_file, 'rt', encoding= 'utf8'  )
o = open( output_file, 'wt' )

reader = csv.reader( i )

#df = pd.DataFrame(reader)


#if skip_headers:
	#headers = reader.next()
    
count = 0
for line in reader:    
    if label_index == -1:
        label = '1'
    else:
        label = line.pop( label_index )
    count = count +1
    #print("idx ", count)
    new_line = construct_line( label, line )
    o.write( new_line )