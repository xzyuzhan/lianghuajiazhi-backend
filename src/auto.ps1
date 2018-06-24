$sum=0
for($i=1;$i -le 12;$i++)
{
	cmd /c all.bat
	Start-Sleep -s 1800
    $sum+=$i
}
$sum


