<?php
include_once "markdown.php";
$mdcontent = $_POST['value'];
file_put_contents("/var/www/html/itensor/body.md",$mdcontent);
$mdhtml = Markdown($mdcontent);
file_put_contents("/var/www/html/itensor/body.html",$mdhtml);
echo $mdhtml;
?>
