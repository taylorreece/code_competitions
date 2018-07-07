<?php
//Taylor Reece, Fbook hacker cup quals
//Question 2
error_reporting(E_ALL);

function printTeams($teamA, $teamB){
	echo "Team A:\n";
	foreach($teamA as $player){
		echo " " . $player['name'] . "\n";
	}
	echo "Team B:\n";
	foreach($teamB as $player){
		echo " " . $player['name'] . "\n";
	}
}


$inputfile = fopen("input.txt", "r");
$numProblems = (int)fgets($inputfile);


for($i = 0; $i < $numProblems; $i++){
	$data = explode(" ", fgets($inputfile));
	$numPlayers = (int)$data[0];
	$M = (int)$data[1];
	$P = (int)$data[2];
	
	$players = array();
	for($j = 0; $j < $numPlayers; $j++){
		$data = explode(" ", fgets($inputfile));
		$player = array('name' => $data[0], 'shot' => (int)$data[1], 'height' => (int)$data[2]);
		array_push($players, $player);
	}
	
	
	foreach ($players as $key => $row) {
		$names[$key]  = $row['name'];
		$shots[$key]  = $row['shot'];
		$heights[$key] = $row['height'];
	}
	
	array_multisort($shots, SORT_DESC, $heights, SORT_DESC, $players);

	
	$teamA = array();
	$teamB = array();
	for($j = 0; $j < $numPlayers; $j++){
		if($j%2){
			array_push($teamB, $players[$j]);
		} else {
			array_push($teamA, $players[$j]);
		}
	}
	echo "numPlayers: $numPlayers\n";
	echo "M: $M\n";
	echo "P: $P\n";
	printTeams($teamA, $teamB);

//	echo "Case #" . ($i+1) . ": $result\n";
}
fclose($inputfile);

?>