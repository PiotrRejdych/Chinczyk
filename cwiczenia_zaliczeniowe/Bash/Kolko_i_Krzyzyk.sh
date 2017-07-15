#!/bin/bash


tab_z_adr=(0 1 2 3 4 5 6 7 8)
tablica=("_" "_" "_" "_" "_" "_" "_" "_" "_")

przerwanie=0

while [ "$przerwanie" -eq 0 ]
do
	clear
	echo "Aktualna plansza:"

	for x in {0..2}
	do
		echo "${tablica[x]} ${tablica[x+3]} ${tablica[x+6]}"
	done

	echo " "

	logik=true
	for i in {0..8}
	do
		if [ "${tablica[$i]}" == "_" ];
		then
			logik=false
		fi
	done

	if [ "$logik" == true ];
	then
		przerwanie=1
		echo "Remis"
		echo "Enter: Wyjście"
		read
		continue
	fi

	xwygral=false;
	if [ "${tablica[0]}" == "X" -a "${tablica[1]}" == "X" -a "${tablica[2]}" == "X" ]
	then
		xwygral=true;
	fi

	if [ "${tablica[3]}" == "X" -a "${tablica[4]}" == "X" -a "${tablica[5]}" == "X" ]
	then
		xwygral=true;
	fi

	if [ "${tablica[6]}" == "X" -a "${tablica[7]}" == "X" -a "${tablica[8]}" == "X" ]
	then
		xwygral=true;
	fi

	if [ "${tablica[0]}" == "X" -a "${tablica[3]}" == "X" -a "${tablica[6]}" == "X" ]
	then
		xwygral=true;
	fi

	if [ "${tablica[1]}" == "X" -a "${tablica[4]}" == "X" -a "${tablica[7]}" == "X" ]
	then
		xwygral=true;
	fi

	if [ "${tablica[2]}" == "X" -a "${tablica[5]}" == "X" -a "${tablica[8]}" == "X" ]
	then
		xwygral=true;
	fi

	if [ "${tablica[0]}" == "X" -a "${tablica[4]}" == "X" -a "${tablica[8]}" == "X" ]
	then
		xwygral=true;
	fi

	if [ "${tablica[2]}" == "X" -a "${tablica[4]}" == "X" -a "${tablica[6]}" == "X" ]
	then
		xwygral=true;
	fi

	if [ "$xwygral" == true ]
	then
		echo "Wygrał X"
		przerwanie=1
		read
		continue
	fi

	owygral=false;
	if [ "${tablica[0]}" == "O" -a "${tablica[1]}" == "O" -a "${tablica[2]}" == "O" ]
	then
		owygral=true;
	fi

	if [ "${tablica[3]}" == "O" -a "${tablica[4]}" == "O" -a "${tablica[5]}" == "O" ]
	then
		owygral=true;
	fi

	if [ "${tablica[6]}" == "O" -a "${tablica[7]}" == "O" -a "${tablica[8]}" == "O" ]
	then
		owygral=true;
	fi

	if [ "${tablica[0]}" == "O" -a "${tablica[3]}" == "O" -a "${tablica[6]}" == "O" ]
	then
		owygral=true;
	fi

	if [ "${tablica[1]}" == "O" -a "${tablica[4]}" == "O" -a "${tablica[7]}" == "O" ]
	then
		owygral=true;
	fi

	if [ "${tablica[2]}" == "O" -a "${tablica[5]}" == "O" -a "${tablica[8]}" == "O" ]
	then
		owygral=true;
	fi

	if [ "${tablica[0]}" == "O" -a "${tablica[4]}" == "O" -a "${tablica[8]}" == "O" ]
	then
		owygral=true;
	fi

	if [ "${tablica[2]}" == "O" -a "${tablica[4]}" == "O" -a "${tablica[6]}" == "O" ]
	then
		owygral=true;
	fi

	if [ "$owygral" == true ]
	then
		echo "Wygrał O"
		przerwanie=1
		read
		continue
	fi

	if [ "$aktualnygracz" == "X" ]
	then
		echo "Gracz X: Gdzie postawić X? Wpisz:"
		for x in {0..2}
		do
			echo "${tab_z_adr[x]} ${tab_z_adr[x+3]} ${tab_z_adr[x+6]}"
		done

		echo "Lub żeby wyjść: q"

		read iks

		if [ "$iks" == "q" ];
		then
			przerwanie=1
		else
			if [ "$iks" -le 8 -a "$iks" -ge 0 ]
			then
				if [ "${tablica[$iks]}" == "_" ];
				then
					tablica[$iks]="X"
					aktualnygracz="O"
				else
					echo "Błąd, spróbuj ponownie."
					read
					continue
				fi
			fi
		fi
	else
		echo "Gracz O: Gdzie postawić O? Wpisz:"
		for x in {0..2}
		do
			echo "${tab_z_adr[x]} ${tab_z_adr[x+3]} ${tab_z_adr[x+6]}"
		done

		echo "Lub żeby wyjść: q"

		read iks

		if [ "$iks" == "q" ];
		then
			przerwanie=1
		else
			if [ "$iks" -le 8 -a "$iks" -ge 0 ]
			then
				if [ "${tablica[$iks]}" == "_" ];
				then
					tablica[$iks]="O"
					aktualnygracz="X"
				else
					echo "Błąd, spróbuj ponownie."
					read
					continue
				fi
			fi
		fi
	fi

done

