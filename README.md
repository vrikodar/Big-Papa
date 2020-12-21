[![made-with-python](https://img.shields.io/badge/Made%20with-Python-1f425f.svg)](https://www.python.org/)
[![Python Version](https://img.shields.io/badge/python-3.6+-green)](https://www.python.org)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://github.com/SxNade)
[![Stage](https://img.shields.io/badge/Release-Stable-brightgreen.svg)]()
[![Update](https://img.shields.io/badge/updated-today-brightgreen)
[![Ask Me Anything !](https://img.shields.io/badge/Ask%20me-anything-1abc9c.svg)](https://github.com/SxNade)
[![Discord](https://img.shields.io/discord/591914197219016707.svg?label=&logo=discord&logoColor=ffffff&color=7389D8&labelColor=6A7EC2)](https://github.com/SxNade)

# Big-Papa

![Capture](https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQlqh70DzxUIwh08dpOzmZmCxm0t44h1q3xug&usqp=CAU)

Big-Papa Integrates Javascript and python for remote cookie stealing which then can be used for session hijacking

# IN ACTION

![Capture](https://raw.githubusercontent.com/SxNade/Big-Papa/main/cookies.png)

`The Higlighted data is the cookie of ongoing admin session on a router(gateway)`

***Now we can use something Like Burpsuite to Load the cookies and Hijack the admin session***

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

`Full Code of Big-Papa will be released in 1-2 Days till now only the basic Javascript Code and Python Script is released`


*You can manually perform the mitm attack and then inject the Javascript code with Big-Papa.py script runnning along*

`A new feature to mail the captured cookies to user specified e-mail will be added soon...`

# 𝑴𝑨𝑲𝑬_𝑰𝑻_𝑩𝑬𝑻𝑻𝑬𝑹
To make Big-Papa Even Better Contribute to it Or use and Report Any Bugs or fixes Required..

` git clone https://github.com/SxNade/Big-Papa`

