BASE_direc=$( dirname "$0" )
TOP_direc=`pwd`
p_OUTCAR="OUTCAR"
p_EIGENVAL="EIGENVAL"

nband=$( grep NBANDS $p_OUTCAR | awk '{print $15}' )
for(( i=1; i<=$nband; i++ ))
do
	awk 'NR>=9{if($1=='"$i"')print}' $p_EIGENVAL | awk '{
if(NR==1){
	min=$2;
	max=$2;
}
else{
	if($2>max){
		max=$2;
	}
	if($2<min){
		min=$2;
	}
}
}END{print "Band '"$i"' : MIN= "min" ; MAX=  "max}' >> band_extrema.dat
done

python $BASE_direc/get_gap.py

rm -f band_extrema.dat

efermi=$( awk 'NR==6{print $4}' DOSCAR )
sed -i '1i Efermi = '"$efermi"' eV' gap.dat

