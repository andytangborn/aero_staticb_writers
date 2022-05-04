#!/usr/bin/env python
# run_viirs2ioda.py
# process VIIRS files and produce JEDI/IODA compatible obs files
import os
import subprocess as sp
import datetime as dt
import glob
import sys 
#import xarray as xr

#grid='96'
grid='96'
zdim='64'
xdim=grid
ydim=grid


#InRoot='/scratch1/NCEPDEV/da/Andrew.Tangborn/JEDI/fv3-bundle_march31_2022/bump_file_writer/'
#OutRoot='/scratch1/NCEPDEV/da/Andrew.Tangborn/JEDI/fv3-bundle_march31_2022/bump_file_writer/'
InRoot='/scratch1/NCEPDEV/da/Andrew.Tangborn/JEDI/nov22_staticb/work_aero_c96/Data/staticb_aero/'
OutRoot='/scratch1/NCEPDEV/da/Andrew.Tangborn/JEDI/nov22_staticb/work_aero_c96/Data/staticb_aero/'

#FV3Grid='/scratch1/BMC/gsd-fv3-dev/MAPP_2018/pagowski/fix_fv3/C'+grid

year=2016
month=6
day=30
hour=0
yyyymmdd = 20160630 

executable_cor='python bump_cor.py'
executable_stddev='python bump_stddev.py'

my_env = os.environ.copy()
my_env['OMP_NUM_THREADS'] = '4' # for openmp to speed up fortran call
#./viirs2ioda.x $validtime $fv3dir $infile $outfile

itile = 1
ntiles = 6

while itile <= ntiles:

  str_cor_rh_input = str(yyyymmdd)+'.'+str(hour).zfill(2)+'0000.cor_rh.fv_tracer.res.tile'+str(itile)+'.nc' 
  str_cor_rv_input = str(yyyymmdd)+'.'+str(hour).zfill(2)+'0000.cor_rv.fv_tracer.res.tile'+str(itile)+'.nc'
  str_stddev_input = str(yyyymmdd)+'.'+str(hour).zfill(2)+'0000.stddev.fv_tracer.res.tile'+str(itile)+'.nc'


  str_cor_rh_output = str(yyyymmdd)+'.'+str(hour).zfill(2)+'0000.cor_rh.fv_tracer_new.res.tile'+str(itile)+'.nc'
  str_cor_rv_output = str(yyyymmdd)+'.'+str(hour).zfill(2)+'0000.cor_rv.fv_tracer_new.res.tile'+str(itile)+'.nc'
  str_stddev_output = str(yyyymmdd)+'.'+str(hour).zfill(2)+'0000.stddev.fv_tracer_new.res.tile'+str(itile)+'.nc'

  input_flag='-i'
  output_flag='-o'
  xdim_flag='-x'
  ydim_flag='-y'
  zdim_flag='-z'
  InDir = InRoot
  OutDir = OutRoot
  input_file_cor_rh = InDir+str_cor_rh_input
  input_file_cor_rv = InDir+str_cor_rv_input
  output_file_cor_rh = OutDir+str_cor_rh_output
  output_file_cor_rv = OutDir+str_cor_rv_output 
  input_file_stddev = InDir+str_stddev_input
  output_file_stddev = OutDir+str_stddev_output
  args_cor_rh = ' '+input_flag+' '+input_file_cor_rh+' '+xdim_flag+' '+xdim+' '+ydim_flag+' '+ydim+' '+zdim_flag+' '+zdim+' '+output_flag+' '+output_file_cor_rh 
  args_cor_rv = ' '+input_flag+' '+input_file_cor_rv+' '+xdim_flag+' '+xdim+' '+ydim_flag+' '+ydim+' '+zdim_flag+' '+zdim+' '+output_flag+' '+output_file_cor_rv
  args_stddev = ' '+input_flag+' '+input_file_stddev+' '+output_flag+' '+output_file_stddev
  cmd_cor_rh = executable_cor+args_cor_rh
  cmd_cor_rv = executable_cor+args_cor_rv 
  cmd_stddev = executable_stddev+args_stddev
  proc_cor_rh = sp.Popen(cmd_cor_rh,env=my_env,shell=True)
  proc_cor_rv = sp.Popen(cmd_cor_rv,env=my_env,shell=True)
  proc_stddev = sp.Popen(cmd_stddev,env=my_env,shell=True)

  itile = itile + 1 
