<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Strict//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-strict.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">

<head>
    <title>ITensor - Intelligent Tensor Library</title>
    <meta http-equiv="content-language" content="en" />
    <meta http-equiv="content-type" content="text/html; charset=UTF-8" />
    <link rel="icon" href="favicon.ico"/>
    <link rel="stylesheet" href="style.css" type="text/css"/>
    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.6/jquery.min.js" type="text/javascript"></script>
    <script type="text/javascript">$(document).ready(function(){});</script>
    <script type="text/javascript" src="scripts/jquery.corner.js"></script>
    <script type="text/javascript" src="scripts/jquery.jeditable.mini.js"></script>

    <style type="text/css">
    </style>

</head>

<body>

<div id="main">

<div id="navbar" class="rounded">
    <ul>
    <li><a href="index.html">Home</a> </li>
    <li><a class="thispage" href="learn.php">Learn</a> </li>
    <li><a href="contribute.html">Contribute</a></li>
    </ul>
</div>


<div id="banner">
<img src="ITensor.png" /></br>
</div>

<div class="full section rounded"> <h2>Documentation</h2> </div>

<div class="full">
<p>
</p>
</div>

<div class="full edit docs" id="input">
<?php 
include_once "markdown.php";
$mdcontent = file_get_contents("/var/www/html/itensor/body.md"); 
echo Markdown($mdcontent);
?>
</div>

<div id="footer"></div>

<script type="text/javascript">
 $(document).ready(function() {
     $('.edit').editable('send.php', {
        type : "textarea",
        event : "dblclick",
        onblur : "submit",
        cancel : "Cancel",
        loadurl : "body.md",
        indicator : 'Saving...'
     });
 });
</script>


</div> <!--class="main"-->

<script type="text/javascript">$(function() {$('.rounded').corner("7px");});</script>

</body>
</html>
