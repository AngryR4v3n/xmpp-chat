Computer Networking: Project 2 - XMPP Client
======
**FRAN-CHAT** This CLI Python scriptt is a basic XMPP client it is used to communicate between users to connected to a XMPP server. 

#### Screenshots
![Login view]https://imgur.com/a/5QI8ZeR "Login Screen")
![Menu]https://imgur.com/Bpdqk1z "Menu")

## Dependencies & Requirements.
 This program was written in Python 3.8.5, 64-bit for best experience it is recommended to run in this Python version. 
 Same experience is not guaranteed in other Python versions.
 This program contains the following Python packages which need to be installed prior to the usage of the program. 
 Please use your Python package installer and download the following packages: 
 
 ```shell
$ pip install bullet
```
```shell
$ pip install tkinter
```

```shell
$ pip install colorama
```

```shell
$ pip install xmpppy
```

```shell
$ pip install sleekxmpp
```

Aditionally the program uses the following libraries:
* base64
* threading
* time
* binascii
* os
## Installation
```shell
$ git clone https://github.com/molinajimenez/xmpp-chat.git
```
#### ⚠️ WARNING ⚠️: Please make sure you run the following commands after installing all the packages. If this step is not done, the program **won't work**.

```shell
$ pip uninstall pyasn1 peas-modules sleekxmpp
```
```shell
$ pip install pyasn1==0.3.6 pyasn1-modules==0.1.5 sleekxmpp==1.3.3
```

#### **Notice** : While this client was being made, the SleekXMPP package was officially decrecated. The migration to Slixmpp was not done due to development constraints. 

## Contributors & References
 This program was made by Francisco Molina and some examples taken from the following links.
* [Francisco Molina ](https://github.com/molinajimenez)

#### References
* [SleekXMPP Documentation](https://sleekxmpp.readthedocs.io/en/latest/index.html)
* [SleekXMPP Examples](https://github.com/fritzy/SleekXMPP/tree/develop/examples)
* [Sleek Standard Specifications](https://xmpp.org/extensions/)
* [XMPP - definitive guide](https://oriolrius.cat/blog/wp-content/uploads/2009/10/Oreilly.XMPP.The.Definitive.Guide.May.2009.pdf)

## Version 
* Version 1.0


## Contact
#### Developer
* e-mail: mol17050@uvg.edu.gt
