#!/usr/local/bin/perl
#
# Generic Feedback Form - rename this file to something.cgi
#
#                 Copyright NetCorps
#                 all rights reserved
#           You may edit to suit your needs
#
# You need to put your site in place of this one.
$returnpage = "www.niceorspice.com";
#

#
#
#
#
require CGI;
CGI::ReadParse(*in);
#
# Send the mail
#


if( "$in{submitter_email}" eq "" )  {
        $in{submitter_email} = "support\@niceorspice.com";
}
if( "$in{submitter_name}" eq "" )  {
        $in{submitter_name} = "niceorspice";
}

$sendTo = "$in{email}";


if ( "$in{email}" ne "" ) {
 open(SM, "| /usr/ucb/mail $sendTo") || die;
 print(SM "From: $in{submitter_name} <$in{submitter_email}>\n".
                           "To: $in{recipient} <$in{email}>\n".
                           "Subject: $in{subject}\n\n");


print SM $in{"subject"},"\n";
print SM "--------------------------------------\n";
print SM "Submitter Name...: ",$in{"submitter_name"},"\n";
print SM "Street Address...: ",$in{"org_street1"},"\n";
print SM "Street Address...: ",$in{"org_street2"},"\n";
print SM "City.............: ",$in{"org_city"},"\n";
print SM "State............: ",$in{"org_state"},"\n";
print SM "Postal Code......: ",$in{"org_postal"},"\n";
print SM "Submitter Email..: ",$in{"submitter_email"},"\n";
print SM "Submitter Phone..: ",$in{"submitter_phone"},"\n";
print SM "Submitter Fax....: ",$in{"submitter_fax"},"\n";
print SM "--------------------------------------\n";
print SM "More info. on....: ",$in{"checkbox1"},"\n";
print SM "More info. on....: ",$in{"checkbox2"},"\n";
print SM "More info. on....: ",$in{"checkbox3"},"\n";
print SM "More info. on....: ",$in{"checkbox4"},"\n";
print SM "--------------------------------------\n";
print SM "Comments.........: ",$in{"comments"},"\n";
print SM "\n";
close(SM);

print CGI::header();
print "<HTML>\n";
print "<HEAD>\n";
print "<TITLE>Completed Contact Form</TITLE>\n";
print "</HEAD>\n";
print "<BODY BGCOLOR=#FFFFFF>\n";
print "\n";
print "<center>\n";
print "<h3>\n";
print "<font face=arial>Completed Contact Form</font>\n";
print "</h3>\n";
print "Thank you ",$in{"submitter_name"}, " for taking the time to complete the form.\n";
print "<P>\n";
print "<A HREF=\"http://",$returnpage,"\">Back to ",$returnpage,"</A>\n";
print "</CENTER>\n";
print "</BODY>\n";
print "</HTML>\n";
}
