import h5py
f = h5py.File('Enregistrements/turning2.h5')
m = f['muh5']['0']['sig'][()]
enr = []
for i in f['muh5'].keys():
    enr.append(int(i))

print(enr)
enr = np.sort(enr)
print(enr)
for k in enr:
    if k != 0:
        m = np.concatenate((m, f['muh5'][str(k)]['sig'][()]), axis = 1)


print(m.shape)
