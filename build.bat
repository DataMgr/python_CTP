set PRJ_NAME=python_ctp

cd %PRJ_NAME%
del *.pyd  /F 
del *.cpp  /F
cd  ..


python setup.py build_ext --inplace