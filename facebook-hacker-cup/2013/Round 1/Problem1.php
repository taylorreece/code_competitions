<?php
//Taylor Reece, Fbook hacker cup quals
//Question 1
error_reporting(E_ALL);

function printGrid($inputArray){
	foreach($inputArray as $row){
		foreach($row as $item){
			echo $item;
		}
		echo "\n";
	}
}

function formsSquare($inputArray, $rowSize){
	$topX = -1;
	$topY = -1;
	$bottomX = -1;
	$bottomY = -1;

	for($i = 0; $i < $rowSize; $i++){
		for($j = 0; $j < $rowSize; $j++){
			if($inputArray[$i][$j] == "#" && $topX == -1){
				$topX = $i; $topY = $j;
			}
			if($inputArray[$rowSize - 1 - $i][$rowSize - 1 - $j] == "#" && $bottomX == -1){
				$bottomX = $rowSize - 1 - $i;
				$bottomY = $rowSize - 1 - $j;
			}
		}
	}
	
	for($i = 0; $i < $rowSize; $i++){
		for($j = 0; $j < $rowSize; $j++){
			if($i >= $topX && $j >= $topY && $i <= $bottomX && $j <= $bottomY && $inputArray[$i][$j] != "#"){
				return false;
			}
			if(($i < $topX || $j < $topY || $i > $bottomX || $j > $bottomY) && $inputArray[$i][$j] == "#") {
				return false;
			}
		}
	}
	
	if(!(($bottomX - $topX) == ($bottomY - $topY))){ return false; } // Not a square
	
	return true; // Passed all tests.
}

$inputfile = fopen("input.txt", "r");
$numProblems = (int)fgets($inputfile);

for($i = 0; $i < $numProblems; $i++){
	$rowSize = (int)fgets($inputfile);
	$problem = array();
	for($j = 0; $j < $rowSize; $j++){
		$lineIn = str_split( fgets($inputfile)  );
		
		array_push($problem, $lineIn);
		
	}
//	echo "\n";
//	printGrid($problem);
	$result = (formsSquare($problem,$rowSize)) ? "Yes" : "No";
	echo "Case #" . ($i+1) . ": $result\n";
}
fclose($inputfile);

?>