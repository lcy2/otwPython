
while (<ARGV>) {
    my @elements=split /,/, $_;
    foreach(@elements){
        print "<th>".$cgi->escapeHTML($_)."</th>";
    }
}
