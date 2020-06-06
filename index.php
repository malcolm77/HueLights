<?PHP
echo '<H1>';
echo 'lights';
echo '</H1>';
?>

<HR>

<?PHP

// url = "http://192.168.1.126/api/qxb5PJleolvND8RAvqokpuj1eM7o4N--9bdavDAs/lights/5/state"

$response = file_get_contents("http://192.168.1.150/api/qxb5PJleolvND8RAvqokpuj1eM7o4N--9bdavDAs/");

echo '<strong>JSON Arrary</strong><br>';

$arr = json_decode($response, true);
// echo $arr['lights'];
// echo "State      : " . $arr['lights']['4']['state']['on'] . "<br>";
// echo "Brightness : " . $arr['lights']['4']['state']['bri'] . "<br>";
// echo "Name       : " . $arr['lights']['4']['name'] . "<br>";

foreach ($arr['lights'] as $light) {
	// echo "Light : " . $light['name'] . ": " . $light['state']['on'] . "<br>";
	echo "Light : " . $light['name'] . ": ";

	$state = $light['state']['on'];
	if ($state != "") { 
		echo "on" . "<br>";
	} else {
		echo "off" . "<br>";
	}
}

echo '<HR>';
echo '<strong>response</strong><br>';
// echo $response;

echo '<HR>';
echo '<br>';
echo '<br>';
echo '<br>';
echo '<br>';
echo '<br>';

?>