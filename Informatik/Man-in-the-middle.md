
# Man-in-the-middle Angriff
## Grundsätzliches
---
Ein Man-in-the-Middle-Angriff (MITM) ist eine Form des Cyberangriffs, bei der sich der Angreifer heimlich zwischen zwei kommunizierende Parteien positioniert, um deren Kommunikation mitzulesen und/oder zu manipulieren.

Bei einem MITM-Angriff schaltet sich der Angreifer in die Verbindung zwischen zwei Benutzern oder Systemen ein, ohne dass dies von den eigentlichen Kommunikationsparteien bemerkt wird. Auf diese Weise ist es dem Angreifer möglich, vertrauliche Informationen abzufangen oder sogar eigene Inhalte einzuschleusen bzw. die Kommunikation zu manipulieren.

![](https://networksimulationtools.com/wp-content/uploads/2020/12/Man-In-The-Middle-Attack-Network-Projects.png)

## Angriffsszenerien
---
### Rogue Access Points 
Der Angreifer richtet einen eigenen böswilligen WLAN-Access-Point mit einer vertrauenserweckenden SSID ein und lockt Opfer an, die sich dann in das kompromittierte Netzwerk einwählen.
### BGP Hijacking
Durch Manipulation von Border Gateway Protocol (BGP) Announcements lenkt der Angreifer den Datenverkehr für ganze IP-Bereiche um.

### SS7-Attacken
Mithilfe von Schwachstellen im Signalling System 7 können sich Angreifer in die mobile Kommunikation einklinken und Anrufe, SMS etc. mitlesen oder manipulieren.
### Beispiel: Öffentliches Wifi (Bodenseekreis)
Zuerst verbindet sich der Angreifer mit einem Netzwerk, in dem sich das Opfer befindet. Dannach sucht er die IP-Adresse des Opfers im Netzwerk. Hier werden alle IPs Angezeigt.
![Pasted image 20231124141339.png](https://github.com/DotNaos/TGI13/blob/bc0ef581b3efd7cf865041ac598e4d11281a4771/Informatik/Images/Pasted%20image%2020231124141339.png?raw=true)

$$Das \ hier \ ist \ ein \ Latex \ test = 2x \cdot \frac{3x}{4x}$$

Für den Angriff, müssen wir sowohl das Opfer als auch den Router täuschen, indem wir dem Router sagen, dass die MAC-Adresse des Opfers unsere MAC-Adresse ist und dem Opfer sagen, dass die MAC-Adresse des Routers unsere MAC-Adresse ist.

Die Informationen zum Router lassen wir uns hier ausgeben:

![Pasted image 20231124142122.png](https://github.com/DotNaos/TGI13/blob/bc0ef581b3efd7cf865041ac598e4d11281a4771/Informatik/Images/Pasted%20image%2020231124142122.png?raw=true)

Jetzt können wir unser Opfer als target des ARP-Spoof setzen und die Datenanfragen mitlesen. Wir sind damit der Man-in-the-middle.
![Pasted image 20231126210112.png](https://github.com/DotNaos/TGI13/blob/bc0ef581b3efd7cf865041ac598e4d11281a4771/Informatik/Images/Pasted%20image%2020231126210112.png?raw=true)

Hier sehen wir, dass das Opfer an
https://m.youtube.com
https://apple.de
... 
Anfragen sendet.

Nun können wir einen DNS-Spoofer starten, der Anfragen an eine Domain, an eine andere Seite umleitet.

Wenn das Opfer jetzt auf Amazon.com gehen will, kann die Anfrage an eine Phising Seite redirected werden.

Will man sich gegen so einen Angriff in einem öffentlichen Netzwerk schützen, hilft ein VPN.  

