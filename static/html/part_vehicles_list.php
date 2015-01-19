<!DOCTYPE html>
<HTML>
<HEAD>
<link rel="stylesheet" type="text/css" href="vehicles_list.css">
</HEAD>
<?php
include 'functions.inc.php';

$table_name = '';
$table_name = $_GET['table_name'];

$ap_kit_number = '';
$ap_kit_number = $_GET['ap_kit_number'];

$make_list = getPartMakesList($table_name, $ap_kit_number);

$vehicle_info_table = buildVehicleTable($table_name, $ap_kit_number, $make_list);
?>
<BODY>
	<div class="wrapper">
		<div class="header"></div>
		<div class="kitNumber">
			<span class="number">Kit # <?php echo $ap_kit_number;?></span></br>
			<span class="customerServiceText">If your vehicle is not listed below please contact Customer Service at 815-306-3696 
			for fitment help before ordering.</span></br></br>
			<span>Fits the Following Vehicles:</span>
		</div>
		<div class="vehicleInfo">
			<div class="spacer">&nbsp;</div>
			<table class="vehicleTable">
				<tbody>
					<?php echo $vehicle_info_table; ?>
				</tbody>
			</table>
			<div class="spacer">&nbsp;</div>
		</div>
	</div>
</BODY>
</HTML>