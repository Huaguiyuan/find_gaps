# find_gaps
Finding the energy gaps from VASP output files.

* Execute "./main.sh" directly.
* The shellscript and python script files should stay in the same director.
* Be sure the current work directory is the desired VASP calculation directory.
* OUTCAR DOSCAR EIGENVAL files are required.
* The gap data are saved into "gap.dat".
* The data include the top and bottom energy values of each gap, and the corresponding band number for those energy values.
