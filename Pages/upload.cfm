<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<title>Untitled Document</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
<style type="text/css">
<!--
body {
	background-color: #99CCCC;
}
.style1 {
	font-family: Arial, Helvetica, sans-serif;
	font-size: 12px;
}
.style2 {
	font-family: Arial, Helvetica, sans-serif;
	font-size: 18px;
}
-->
</style></head>

<body>
<cffile action = "upload" fileField = "uploadfile" destination="d:\Inetpub\niceorspice\upload\">
<cfoutput>
  <div align="center" class="style2">Your file has been accepted for display.</div>
</cfoutput>
<div align="center"><br>
    <cfoutput></cfoutput>
    <p><br>
        <object classid="clsid:D27CDB6E-AE6D-11cf-96B8-444553540000" codebase="http://download.macromedia.com/pub/shockwave/cabs/flash/swflash.cab#version=5,0,0,0" width="100" height="22">
          <param name="BGCOLOR" value="">
          <param name="movie" value="button1.swf">
          <param name="quality" value="high">
          <embed src="button1.swf" quality="high" pluginspage="http://www.macromedia.com/shockwave/download/index.cgi?P1_Prod_Version=ShockwaveFlash" type="application/x-shockwave-flash" width="100" height="22" ></embed>
        </object>
</p>
    <p class="style1"><cfoutput>Please allow 24 hours for posting.</cfoutput><br>
      <cfoutput>Thank you for using NiceOrSpice.com</cfoutput> </p>
</div>
</body>
</html>
