<?php
Function databaseConnection() {
	$db_connect = mysql_connect('localhost', 'root', 'PLOK1234plok');
	
	if (!$db_connect) {
		die('Could not connect: ' . mysql_error());
	}
}

Function getPartMakesList($table_name, $ap_kit_number) {
	
	$db_connect = databaseConnection();
	
	if (!mysql_select_db('test_willie')) {
		die('Could not select database: ' . mysql_error());
	}
	
	$make_list_query = "SELECT DISTINCT(make) FROM $table_name ";
	$make_list_query .= "WHERE ap_kit_number = '$ap_kit_number'";
	echo $make_list_query;
exit();
	$make_list = mysql_query($make_list_query);
	if (!$make_list) {
		die('Could not query:' . mysql_error());
	}
	
	mysql_close($db_connect);
	
	return($make_list);
}

Function getPartVehicles($table_name, $ap_kit_number, $make) {
	
	$db_connect = databaseConnection();
	
	if (!mysql_select_db('test_willie')) {
		die('Could not select database: ' . mysql_error());
	}
	
	$vehicle_list_query = "SELECT beginning_year, ending_year, model, fitment_notes ";
	$vehicle_list_query .= "FROM $table_name ";
	$vehicle_list_query .= "WHERE make = '$make[0]' AND ap_kit_number = '$ap_kit_number'";
		
	$vehicle_list = mysql_query($vehicle_list_query);
	if (!$vehicle_list) {
		die('Could not query:' . mysql_error());
	}
	
	mysql_close($db_connect);
	
	return($vehicle_list);
}

Function buildVehicleTable($ap_kit_number, $make_list) {
	
	$num_makes = mysql_num_rows($make_list);
	$vehicle_info_table = '';
	
	$i = 1;
	while ($i <= $num_makes) {
		$make = mysql_fetch_row($make_list);
		$i++;
		
		$vehicle_list = getPartVehicles($ap_kit_number, $make);
		
		$num_vehicles = mysql_num_rows($vehicle_list);
		$j = 1;
		$vehicle_info_table .= '<tr><th colspan="4" class="makeHeader">&nbsp;</th></tr><tr><th colspan="4" class="makeHeader">'.$make[0].'</th></tr>';
		$vehicle_info_table .= '<tr><th>BEGINNING YEAR</th><th>ENDING YEAR</th><th>MODEL</th><th>FITMENT NOTES</th><tr>';
		
		while($j <= $num_vehicles) {
			$k = 0;
			
			$vehicle_info_array = mysql_fetch_row($vehicle_list, $k);
			
			$vehicle_info_table .= '<tr><td>'.$vehicle_info_array[0].'</td><td>'.$vehicle_info_array[1].'</td>';
			$vehicle_info_table .= '<td>'.$vehicle_info_array[2].'</td><td>'.$vehicle_info_array[3].'</td></tr>';
			
			$j++;
			$k++;
		}
	
	}
	
	return($vehicle_info_table);

}
?>