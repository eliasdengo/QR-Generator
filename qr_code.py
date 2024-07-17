import segno 

qrcode=segno.make_qr("Engineer Elias Dengo")
qrcode.save("Enginer.png",
            scale=5,
            light="#ADD8E6",
            dark="darkblue",
            quiet_zone="white", 
            data_dark="green",
            data_light="lightgreen"
            )