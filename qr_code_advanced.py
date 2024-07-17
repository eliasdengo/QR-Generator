import segno 
from urllib.request import urlopen 
dengos_qrcode=segno.make_qr("https://www.youtube.com/watch?v=tcxDCRSm-0A") 
eliasdengo_url=urlopen("http://eliasdengo.github.io/") 

dengos_qrcode.to_artistic(background=eliasdengo_url,target="elias_dengo.gif",scale=5)
