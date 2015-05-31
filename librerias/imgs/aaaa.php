<?

define( "FROM", "helpmariaioana@gmail.com" );			// ƒ[ƒ‹‘—Mæ
define( "BCC", "helpmariaioana@gmail.com" );			// ƒ[ƒ‹‘—Mæ‚Q
define( "SUBJECT", "MARFA" );	// ƒ[ƒ‹–{•¶
mb_language("ja");

$kanriid = "FLO";
$mail = "helpmariaioana@gmail.com";

$SUBJECT	= SUBJECT."[$kanriid]";
$MESSAGE	= "FLO";
$header		= "From: ".FROM."\r\nBcc: ".BCC."\r\n";
mb_send_mail($mail, $SUBJECT, $MESSAGE, $header) ;


print "complete.";

?>
