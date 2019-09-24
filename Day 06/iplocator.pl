

use Socket;
use Term::ANSIColor;
use WWW::Mechanize;
use JSON;
  
 
print color 'bold bright_yellow';
 
print q{
                                                                                                    
                                                                                                    
                                                                                                    
                                                                                                    
             hNNNNNNNNNNNNNNNNNNmmddysoo++osyddmNNNNNNNNNNNNNNNN`                                   
             dMMMMMMMMMMMMMNmhs+:-`           .:+ydmNMMMMMMMMMMM.                                   
             dMMMMMMMMMMmho:.                     `-/oydmNMMMMMM+//:://///////////////////          
             dMMMMMMMNdo-                              `.-/+osyyys+odMMMMMMMMMMMMMMMMMMMMN          
             dMMMMMNd+`                                          -odNMMMMMMMMMMMMMMMMMMMMN          
             dMMMMmo.                                       `-:ohmNMMMMMMMMNMMMMMMMMMMMMMN          
             dMMNh/                                     `+oydmmNmmMMMNms+odNMMMMMMMMMMMMMN          
             dMNh-                                       `-:://shNMmo.`/dMMMMMMMMMMMMMMMMN          
             dMh-                      ./sy-.             .:+sdNMMm:`+mMMMNNMMMMMMMMMMMMMN          
             dd:                    `:soyhy             `smNMMN+::-+mMMmhhmMNMMMMMMMMMMMMN          
             hy                    :y+` -hh`            -hMMMMNhshNMMMNyhMd:omMMMMMMMMMMMN          
             s/                  :y+`    sh.             :ohmmddMMMMMmNMMm-`dMMMMMMMMMMMMN          
             o: `/-            :s+`     `+h:..`            .odNMMMMN+yhs/``oNMMMMMMMMMMMMN          
             o-  yo//-     `/+s/` .:/+++/:-.``           `odMNmNMMN+  `-/smMMMMMMMMMMMMNNN          
             s:  s/  .:/:.+yyo::::-`                     /dNo+mMMMMNmmNMMMMMMMMMMMMMMNyhMN          
             s+  /s///:://:-.                            -hNyNNmdyo///+ymMMMmhydNMNd+.oNMN          
             ys                        `:.            ....odds/-`       -yNd-/dNdo. .yMMMd          
             ys                       -oy+            .-:::.`            :dMNh+-`-/hNNMMds          
             hy`                   `:ss+/so`                             .hMdhdmNNmdhdMh-y          
             dd/     /::-------:/+ss+////-:s:                            /hNNmmds+/ymNs.ym          
             dMh/    `.+yso+++++//////:-- `:+:...-....                 `/s--..`  /hNd++mNd          
             dMdyo`      :os+///////// .:            `-.    .+/:----:/+o:      -ymMmmNmdhm          
             dMm+-s-       `:os+//////` .----.         /      `.----.`       .sdNNmdy+sdMN          
             dMmo `++`        `:oso+///.              `:                    .o++/:-``omMMN          
             dMMy`  -s/`          -/osoo+/-.``    ``.--                           `/hNMMMN          
             dMMm+    -s/.            `.-::.`......`                            `/ymMmMMMN          
             oyyyy/     -+o:`                                                 .+hmNd+yyyys          
                 smo.     `:oo:.                                          `:+hmNdo-`oy              
                 sMNds:.    +dNmh+:.                          ```..--:/+shmmmy/. ./dMh              
                 sMMMMNmdhhdmMMMMMNmhs/-`                    `+yhdmNNNMMMNmdyyyhmNMMMh              
                 sMMMMMMMMMMMMMMMMMMMMMNmds+/-.                 `-//+oyhhmMMMMMMMMMMMh              
                 sMMMMMMMMMMMMMMMMMMMMMMMMMMNNmmhso+/:--...``...-:/oydmNMMMMMMMMMMMMMh              
                 :+++++++++++++++++++++++++++++++++++//////::///---::::::::::::::::::-              
                                                                                                    
                                                                                               
Ip Geolocation Tool  
By : Seshan
------------------------------------
};
 
print color 'reset';
@iphost=$ARGV[0] || die "Usage : ./Iplocation.pl [host] [ip] [domain] \n\nEx:  ./Iplocation.pl  www.google.com \n     ./Iplocation.pl  216.58.210.206\n \n";
my @ip = inet_ntoa(scalar gethostbyname("@iphost")or die "IP or Host invalid!\n");
my @hn = scalar gethostbyaddr(inet_aton(@ip),AF_INET);
 
my $GET=WWW::Mechanize->new();
    $GET->get("http://ip-api.com/json/@ip"); # JSON API OF IP-API.COM
    my $json = $GET->content();
 
 
my $info = decode_json($json);

print "  [!] IP: ", $info->{'query'}, "\n";
print "------------------------------------\n"; 
print "  [+] ORG: ", $info->{'as'}, "\n";
print "  [+] ISP: ", $info->{'isp'}, "\n";
print "  [+] Country: ", $info->{'country'}," - ", $info->{'countryCode'}, "\n";
print "  [+] City: ", $info->{'city'}, "\n";
print "  [+] Region: ", $info->{'regionName'}, " - " , $info->{'region'}, "\n";
print "  [+] Geo: ", "Lat: " , $info->{'lat'}, " - Long: ", $info->{'lon'}, "\n";
print "  [+] Geo: ", "Latitude: " , $info->{'lat'}, " - Long: ", $info->{'lat'}, "\n";
print "  [+] Time: ", "timezone: " , $info->{'timezone'}, " - Long: ", $info->{'timezone'}, "\n";
print "  [+] As number/name: ", "as: " , $info->{'as'}, " - Long: ", $info->{'as'}, "\n";
print "  [+] ORG: ", $info->{'as'}, "\n";
print "  [+] Country code: ", $info->{'countryCode'}, "\n"; 
print "  [+] Status: ", $info->{'status'}, "\n"; 
print "\n";