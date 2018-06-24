$sum=0
for($i=1;$i -le 120;$i++)
{
	cmd /c all.bat
	Start-Sleep -s 180
    $sum+=$i
}
$sum


