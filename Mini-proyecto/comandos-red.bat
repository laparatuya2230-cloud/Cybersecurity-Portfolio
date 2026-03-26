echo off
cls 
echo Bienvenidos a mi scrip
echo por : +++++++++

echo primer analisis : guardando reporte de comando ipconfig
ipconfig >reporte-ipconfig.txt
echo reporte geenrado con exito
echo ________________


echo segundo analisis : guardando reporte de comando ipconfig /all
ipconfig /all >reporte-ipconfig-all.txt
echo reporte geenrado con exito
echo ________________


echo tercero analisis : guardando reporte de comando ipconfig /release
ipconfig /release >reporte-ipconfig-release.txt
echo reporte geenrado con exito
echo ________________


echo cuarto analisis : guardando reporte de comando ipconfig /renew
ipconfig /renew >reporte-ipconfig-renew.txt
echo reporte geenrado con exito
echo ________________


echo quinto analisis : guardando reporte de comando ipconfig /flushdns
ipconfig /flushdns >reporte-ipconfig-flushdns.txt
echo reporte geenrado con exito
echo ________________

echo on 