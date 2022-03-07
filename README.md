![SxNade](https://img.shields.io/badge/MadeBy-SxNade-red)

# Big-Papa

![Capture](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlqh70DzxUIwh08dpOzmZmCxm0t44h1q3xug&usqp=CAU)

Big-Papa Integrates Javascript and python for remote cookie stealing which then can be used for session hijacking

---

# IN ACTION

![Capture](https://github.com/SxNade/Big-Papa/blob/main/bgp.gif)

`The Higlighted data is the cookie of ongoing admin session on a router(gateway)`

***Now we can use something Like Burpsuite or your favorite cookie editor extension on firefox to Load the cookies and Hijack the admin session***

# 𝗜𝗡𝗦𝗧𝗔𝗟𝗟𝗔𝗧𝗜𝗢𝗡 𝗜𝗡𝗦𝗧𝗥𝗨𝗖𝗧𝗜𝗢𝗡𝗦

` 1 chmod +x install.sh`

`2 ./install.sh`

**PLease Note that you need to edit the Javascript File to your own Local IP address**

![Capture](https://raw.githubusercontent.com/SxNade/Big-Papa/main/rplace_ip.png)


# How Does it work?

**Big-Papa utilizes malicious javascript code injection...and then makes a GET Request(with cookies) to the Python Web server running on the attacker machine**


`Note That you need to be man in the middle in order to inject the malicious javascript Code and then steal cookies of the website that the victim is currently visting`


*`For testing purposes copy the Javascript code from the bgp.js file without the script tags and execute in the console of the browser`*


*You can use Bettercap in-order to become man-in-the-middle using bettercap or use arp spoof and then run Big-Papa to inject Javascript*



# For HTTPS?



`Big-Papa will work Perfectly against HTTP websites but For HTTPS you can use sslstrip to Downgrade it to HTTP and then utilize Big-Papa`



*SSLstrip --> https://github.com/moxie0/sslstrip.git



*Still some websites use HTTP and thus their data including Passwords can be read in Clear text but we need to steal cookies in some cases in order to Bypass 2-Factor-Authentication*



# 𝕌ℙ𝔻𝔸𝕋𝔼

`There were problems with writing code for javscript injector due to ongoing problems with netfilterqueue installation`


**BUT YOU CAN STILL USE BETTERCAP TO BECOME MAN IN THE MIDDLE AND ALSO INJECT JAVASCRIPT CODE USING BETTERCAP**

*INSTALL BETTERCAP AS FOLLOWS

`sudo apt install bettercap`

*Then you can run Big-Papa to capture cookies*

*You can manually perform the mitm attack and then inject the Javascript code with Big-Papa.py script runnning along*

`A new feature to mail the captured cookies to user specified e-mail will be added soon...`

# 𝑴𝑨𝑲𝑬_𝑰𝑻_𝑩𝑬𝑻𝑻𝑬𝑹
To make Big-Papa Even Better Contribute to it Or use and Report Any Bugs or fixes Required..

` git clone https://github.com/SxNade/Big-Papa`

https_cookie_stealer.py is a MITM PoC that allows stealing of cookies that are not
secured with the "secure" attribute, even if the target server can be reached
only via https.

This is done by injecting a small piece of HTML code into every clear text http
response for the client which forces to load a JavaScript code from the (not existing)
http service of the target server.

Example:
<script language="javascript" type="text/javascript" src="http://xxxx"></script>

It then implements a basic http service to retrieve the cookie values.

https_cookie_stealer.py is based on the MITMProxy (http://mitmproxy.org/) library libmproxy.

Running:
https_cookie_stealer.py can be run from the source base without installation.  
Just run 'python https_cookie_stealer.py' as a non-root user to get the
command-line options.

The four steps to getting this working (assuming you're running Linux)
are:

1) Flip your machine into forwarding mode (as root):
echo "1" > /proc/sys/net/ipv4/ip_forward

2) Setup iptables to intercept HTTP requests (as root):
iptables -t nat -A PREROUTING -p tcp --destination-port 80 -j REDIRECT --to-port <yourListenPort>

3) Run https_cookie_stealer.py with the command-line options you'd like (see above).

4) Run arpspoof to redirect traffic to your machine (as root):
arpspoof -i <yourNetworkdDevice> -t <yourTarget> <theRoutersIpAddress>
