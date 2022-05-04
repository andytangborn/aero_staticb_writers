import argparse
import netCDF4
import numpy as np
import os
import hashlib

# Reads in BUMP staticB correlation files and writes out at different resolution.


parser = argparse.ArgumentParser(
    description=('Read in BUMP correlation file and write out at a different resolution')
)
parser.add_argument(
    '-i', '--input',
    help="name of NetCDF input file",
    type=str, required=True)
parser.add_argument(
    '-o', '--output',
    help="name of NetCDF output file",
    type=str, required=True)
parser.add_argument(
    '-x', '--xdim',
    help="x-dimension",
    type=str, required=True)
parser.add_argument(
    '-y', '--ydim',
    help="x-dimension",
    type=str, required=True)
parser.add_argument(
    '-z', '--zdim',
    help="z-dimension",
    type=str, required=True)



args = parser.parse_args()



ncfile_in = netCDF4.Dataset(args.input, mode='r', format='NETCDF4')
ncfile_out = netCDF4.Dataset(args.output, mode='w', format='NETCDF4')

xdim = int(args.xdim)
ydim = int(args.ydim)
zdim = int(args.zdim)

my_attrs = dict(filename=args.output)
for name, value in my_attrs.items():
    setattr(ncfile_out, name, value)


sulfa = ncfile_in.variables['sulf']
bc1a = ncfile_in.variables['bc1']
bc2a = ncfile_in.variables['bc2']
oc1a = ncfile_in.variables['oc1']
oc2a = ncfile_in.variables['oc2']
dust1a = ncfile_in.variables['dust1']
dust2a = ncfile_in.variables['dust2']
dust3a = ncfile_in.variables['dust3']
dust4a = ncfile_in.variables['dust4']
dust5a = ncfile_in.variables['dust5']
seas1a = ncfile_in.variables['seas1']
seas2a = ncfile_in.variables['seas2']
seas3a = ncfile_in.variables['seas3']
seas4a = ncfile_in.variables['seas4'] 



xaxis_1 = ncfile_out.createDimension("xaxis_1", xdim)
xaxis_1 = ncfile_out.createVariable("xaxis_1", float, ('xaxis_1')) 
xaxis_1.long_name = 'xaxis_1'
xaxis_1.units = 'none'
print(hashlib.md5("xaxis_1".encode('utf-8')).hexdigest()[:16])
xaxis_1.cartesian_axis = 'X'
yaxis_1 = ncfile_out.createDimension("yaxis_1", ydim)
yaxis_1 = ncfile_out.createVariable("yaxis_1", float, ('yaxis_1'))
yaxis_1.long_name = 'yaxis_1'
yaxis_1.units = 'none'
yaxis_1.cartesian_axis = 'Y'
zaxis_1 = ncfile_out.createDimension("zaxis_1", zdim) 
zaxis_1 = ncfile_out.createVariable("zaxis_1", float, ('zaxis_1'))
zaxis_1.long_name = 'zaxis_1'
zaxis_1.units = 'none'
zaxis_1.cartesian_axis = 'Z'
Time = ncfile_out.createDimension("Time",None )
Time = ncfile_out.createVariable("Time", float, ('Time'))
Time.long_name = 'Time'
Time.units = 'time level'
Time.cartesian_axis = 'T'
#cor_dim = ncfile_out.createDimension('cor_values', (1,64,12,12))
sulf=ncfile_out.createVariable('sulf', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
sulf.long_name = 'mass_fraction_of_sulfate_in_air' 
sulf.units = 'ugkg-1' 
sulf.checksum = hashlib.md5("sulf".encode('utf-8')).hexdigest()[:16]
bc1=ncfile_out.createVariable('bc1', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
bc1.long_name = 'mass_fraction_of_hydrophobic_black_carbon_in_air'
bc1.units = 'ugkg-1'
bc1.checksum = hashlib.md5("bc1".encode('utf-8')).hexdigest()[:16]
bc2=ncfile_out.createVariable('bc2', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
bc2.long_name = 'mass_fraction_of_hydrophilic_black_carbon_in_air'
bc2.units = 'ugkg-1'
bc2.checksum = hashlib.md5("bc2".encode('utf-8')).hexdigest()[:16]
oc1=ncfile_out.createVariable('oc1', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
oc1.long_name = 'mass_fraction_of_hydrophobic_organic_carbon_in_air'
oc1.units = 'ugkg-1'
oc1.checksum = hashlib.md5("oc1".encode('utf-8')).hexdigest()[:16]
oc2=ncfile_out.createVariable('oc2', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
oc2.long_name = 'mass_fraction_of_hydrophilic_organic_carbon_in_air'
oc2.units = 'ugkg-1'
oc2.checksum = hashlib.md5("oc2".encode('utf-8')).hexdigest()[:16]
dust1=ncfile_out.createVariable('dust1', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
dust1.long_name = 'mass_fraction_of_dust001_in_air'
dust1.units = 'ugkg-1'
dust1.checksum = hashlib.md5("dust1".encode('utf-8')).hexdigest()[:16]
dust2=ncfile_out.createVariable('dust2', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
dust2.long_name = 'mass_fraction_of_dust002_in_air'
dust2.units = 'ugkg-1'
dust2.checksum = hashlib.md5("dust2".encode('utf-8')).hexdigest()[:16]
dust3=ncfile_out.createVariable('dust3', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
dust3.long_name = 'mass_fraction_of_dust003_in_air'
dust3.units = 'ugkg-1'
dust3.checksum = hashlib.md5("dust3".encode('utf-8')).hexdigest()[:16]
dust4=ncfile_out.createVariable('dust4', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
dust4.long_name = 'mass_fraction_of_dust004_in_air'
dust4.units = 'ugkg-1'
dust4.checksum = hashlib.md5("dust4".encode('utf-8')).hexdigest()[:16]
dust5=ncfile_out.createVariable('dust5', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
dust5.long_name = 'mass_fraction_of_dust005_in_air'
dust5.units = 'ugkg-1'
dust5.checksum = hashlib.md5("dust5".encode('utf-8')).hexdigest()[:16]
seas1=ncfile_out.createVariable('seas1', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
seas1.long_name = 'mass_fraction_of_sea_salt001_in_air'
seas1.units = 'ugkg-1'
seas1.checksum = hashlib.md5("seas1".encode('utf-8')).hexdigest()[:16]
seas2=ncfile_out.createVariable('seas2', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
seas2.long_name = 'mass_fraction_of_sea_salt002_in_air'
seas2.units = 'ugkg-1'
seas2.checksum = hashlib.md5("seas2".encode('utf-8')).hexdigest()[:16]
seas3=ncfile_out.createVariable('seas3', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
seas3.long_name = 'mass_fraction_of_sea_salt003_in_air'
seas3.units = 'ugkg-1'
seas3.checksum = hashlib.md5("seas3".encode('utf-8')).hexdigest()[:16]
seas4=ncfile_out.createVariable('seas4', float, ('Time', 'zaxis_1','yaxis_1','xaxis_1'))
seas4.long_name = 'mass_fraction_of_sea_salt004_in_air'
seas4.units = 'ugkg-1'
seas4.checksum = hashlib.md5("seas4".encode('utf-8')).hexdigest()[:16]

xaxis_1a = [] 
yaxis_1a = []
zaxis_1a = [] 
for k in range(1,xdim+1):
    xaxis_1a += [k] 
    yaxis_1a += [k]
for k in range(1,zdim+1):
    zaxis_1a += [k]
xaxis_1[:] = xaxis_1a[:]
yaxis_1[:] = yaxis_1a[:] 
zaxis_1[:] = zaxis_1a[:]

Time_a = []
Time_a = [1]
Time[:] = Time_a[:]


#print(yaxis_1)

#yaxis_1[:] = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
sulf[:] = sulfa[:]
bc1[:] = bc1a[:]
bc2[:] = bc2a[:]
oc1[:] = oc1a[:]
oc2[:] = oc2a[:]
seas1[:] = seas1a[:]
seas2[:] = seas2a[:]
seas3[:] = seas3a[:]
seas4[:] = seas4a[:]
dust1[:] = dust1a[:]
dust2[:] = dust2a[:]
dust3[:] = dust3a[:]
dust4[:] = dust4a[:]
dust5[:] = dust5a[:]


ncfile_out.close
