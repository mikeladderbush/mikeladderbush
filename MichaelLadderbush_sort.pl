#Michael Ladderbush

#This code is a sorter that will take any number of input strings from the user and then output those strings
#sorted into alphabetical order.

#!/usr/bin/perl
use warnings;
use strict;

my @list = sort @ARGV;
print("@list\n");


