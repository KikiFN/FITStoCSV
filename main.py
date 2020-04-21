from astropy.io import fits
import numpy
import string 

myfits = fits.open('COSMOS_3DHST_MCSPF_input.fits')

id_list, column_names, results,arrays_list= [],[],[],[]

#LISTA
for i in myfits[1].data['id']:
    id_list.append(i)

#NOMI COLONNE
cols = myfits[1].columns
for k in cols.names:
    column_names.append(k)

#CREO ARRAY DI TUTTI I RAPPORTI
with open("data.csv", "w") as f:
    f.write('"ID"')
    for n_col,(col,nextcol) in enumerate(zip(column_names,column_names[1:])):
            if (n_col == 0 or n_col == 1):
                    continue
            if (n_col%2==0):
                    f.write(',"{0}/{1}"'.format(str(col),str(nextcol)))
    for n,idn in enumerate(id_list):
        f.write('\n"{0}"'.format(str(idn)))
        for n_col,(col,nextcol) in enumerate(zip(column_names,column_names[1:])):
            if (n_col == 0 or n_col == 1):
                    continue
            if (n_col%2==0):
                    f.write(',"{0}"'.format(str(myfits[1].data[col][n]/myfits[1].data[nextcol][n])))