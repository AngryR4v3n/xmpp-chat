import sleekxmpp
from sleekxmpp.exceptions import IqError, IqTimeout
from sleekxmpp.xmlstream.stanzabase import ET, ElementBase
import os
import base64
import binascii
import xmpp
import threading
import time

# basado en: https://gist.github.com/deckerego/be1abbc079b206b793cf/revisions 
class UserManagement():
    def newUser(self, user, pw):
        jid=xmpp.protocol.JID(user)
        cli=xmpp.Client(jid.getDomain())
        cli.connect()

        if xmpp.features.register(cli,
                          jid.getDomain(),
                          {'username':jid.getNode(),
                           'password':pw}):
            print("Success!\n Se ha creado usuario.")
        else:
            print("Error!\n Usuario no pudo ser creado")
            

class Client(sleekxmpp.ClientXMPP):
    def __init__(self, username, password, instance_name=None):
        jid = "%s/%s" % (username, instance_name) if instance_name else username
        
        super(Client, self).__init__(jid, password)

        self.domain = username.split("@")[1]
        self.username = username

        
        self.path = os.getcwd() + "/resources/"
        self.filename = None
        self.add_event_handler('session_start', self.start)
        self.add_event_handler('message', self.wait_msg)
        self.add_event_handler("changed_subscription", self.alertFriend)
        self.add_event_handler("changed_status", self.wait_for_presences)
        
        self.add_event_handler("got_online", self.onlineTrigger)
        self.add_event_handler("got_offline", self.offlineTrigger)
        
        self.register_plugin('xep_0077')
        self.register_plugin('xep_0030') # Service Discovery
        self.register_plugin('xep_0199') # XMPP Ping
        self.register_plugin('xep_0004') # Data forms
        self.register_plugin('xep_0077') # In-band Registration
        self.register_plugin('xep_0045') # Mulit-User Chat (MUC)
        self.register_plugin('xep_0047', {"auto_accept": True})
        
        self.register_plugin('xep_0096') #envio archivos
        self.received = set()
        self.presences_received = threading.Event()
        self.contacts = []
        if self.connect():
            
            self.process(block=False)
        else:
            raise Exception("Chequeate tu conexion a internet / server")
    
    def kill(self):
        print("Closing XMPP Connection")
        self.disconnect(wait=False)

    def start(self, event):
        self.send_presence(pshow='chat', pstatus='Disponible')
        self.send_notif(self.username, recipient, "Estoy iniciando chat.")
        
        

    def send_pres(self, txt):
        self.send_presence(pshow="dnd", pstatus=txt)
        
    
    #basado en: https://github.com/fritzy/SleekXMPP/blob/develop/examples/roster_browser.py
    def list_contacts(self):
        try:
            self.get_roster()
        except IqError as err:
            print('Error: %s' % err.iq['error']['condition'])
        except IqTimeout:
            print('Error: Request timed out')
        


       #print('Recolectando presencias...\n')
        self.presences_received.wait(5)

        #print('Roster for %s' % self.boundjid.bare)
        groups = self.client_roster.groups()
        
        data = []
        for group in groups:
            print('\n%s' % group)
            print('-' * 72)
            
            for jid in groups[group]:
                temp = []
                
                self.contacts.append(jid)
                sub = self.client_roster[jid]['subscription']
                connections = self.client_roster.presence(jid)
                show = 'available'
                status = ''
                for res, pres in connections.items():
                    if pres['show']:
                        show = pres['show']
                    
                
                temp.append(jid)
                temp.append(sub)
                temp.append(show)
                
                data.append(temp)
        return data
    
    def wait_for_presences(self, pres):
        """
        Track how many roster entries have received presence updates.
        """
        self.received.add(pres['from'].bare)
        if len(self.received) >= len(self.client_roster.keys()):
            self.presences_received.set()
        else:
            self.presences_received.clear()

        #print(pres)
        
    def onlineTrigger(self, presence):
        #print(self.client_roster.keys())
        if presence['status']:   
            print('\n'+'Recibiendo estados: '+presence['status'])
            
    def offlineTrigger(self, presence):
        return presence
    
    def alertFriend(self):
        self.get_roster()


    def addRoster(self, jid):
        try:
            self.send_presence_subscription(pto=jid)
            print("Se agrego usuario al rooster")
        except IqError:
            raise Exception("Unable to add user to rooster")
        except IqTimeout:
            raise Exception("Server not responding")


    
    def get_users(self, username="*"):
        
        users = self.Iq()
        users['type'] = 'set'
        users['from'] = self.jid
        users['id'] = 'search_result'
        
        users['to'] = "search."+self.domain
        
        itemXML = ET.fromstring("<query xmlns='jabber:iq:search'>\
                                 <x xmlns='jabber:x:data' type='submit'>\
                                    <field type='hidden' var='FORM_TYPE'>\
                                        <value>jabber:iq:search</value>\
                                    </field>\
                                    <field var='Username'>\
                                        <value>1</value>\
                                    </field>\
                                    <field var='search'>\
                                        <value>{0}</value>\
                                    </field>\
                                </x>\
                                </query>".format(username))
        users.append(itemXML)
        #print(users)
        try:
            resp = users.send()
            data = []
            temp = []
            cont = 0
            for i in resp.findall(".//{jabber:x:data}value"):
                cont += 1
                txt = ''
                if i.text != None:
                    txt = i.text

                temp.append(txt)
                if cont == 4:
                    cont = 0
                    data.append(temp)
                    temp = []
            return data
        except IqError as e:
            print(e.iq)
        except IqTimeout:
            print("timeout")
        
    def send_msg(self, recipient, body):
        #time.sleep(4)
        self.send_message(recipient,body,None,"chat")
    
    #suicidepreventionmonth.
    def commitSuicide(self):
        delete = self.Iq()
        delete['type'] = 'set'
        delete['from'] = self.boundjid.bare
        itemXML = ET.fromstring("<query xmlns='jabber:iq:register'><remove/></query>")
        delete.append(itemXML)
        try:
            delete.send()
            print("Account deleted succesfuly")
        except IqError as e:
            raise Exception("Unable to delete username", e)
        except IqTimeout:
            raise Exception("Server not responding")

    def wait_msg(self, message):
        if len(message['body']) > 3000:
            print("Recibiste una imagen, revisala en la carpeta /resources")
            received = message['body'].encode('utf-8')
            received = base64.decodebytes(received)
            with open("./resources/imageToSave.png", "wb") as fh:
                fh.write(received)
        elif message['type'] == 'groupchat':
            print("Received group chat from {0}: {1} ".format(message['from'],message['body']) )
        elif str(message).find('http://jabber.org/protocol/chatstates') > -1:
            if str(message).find('active') > -1:
                from_account = "%s@%s" % (message['from'].user, message['from'].domain)
                print('Usuario se conecto: ', from_account, message['body'])
            elif str(message).find('composing') > -1:
                from_account = "%s@%s" % (message['from'].user, message['from'].domain)
                print(from_account, 'Esta escribiendo un mensaje')
            elif str(message).find('inactive') > -1:
                from_account = "%s@%s" % (message['from'].user, message['from'].domain)
                print(from_account, ' esta inactivo')
        else:
            
            print("Recibiste un nuevo mensaje: %s" % message['body'])
            from_account = "%s@%s" % (message['from'].user, message['from'].domain)
            print(from_account, message['body'])

    def msg_group(self, room, body):
        self.send_message(mto=room, mbody=body, mtype='groupchat')
        print("sent group")
    
    def join_group(self, room, nickname):
        self.plugin['xep_0045'].joinMUC(room, nickname)

    def create_group(self, room, nickname):
        stat = "Que onda"
        self.plugin['xep_0045'].joinMUC(room,nickname, pstatus=stat, pfrom=self.jid, wait=True)
        self.plugin['xep_0045'].setAffiliation(room, self.jid, affiliation="owner")
        self.plugin['xep_0045'].configureRoom(room, ifrom=self.jid)

    def send_notif(self, sender, receiver, msg):
        notif = self.Message()
        notif['from'] = sender
        notif['to'] = receiver
        notif['type'] = 'chat'
        itemXML = ET.fromstring("<body>{0}</body>".format(msg))
        itemXML2 = ET.fromstring("<active xmlns='http://jabber.org/protocol/chatstates' />")
        notif.append(itemXML)
        notif.append(itemXML2)
        notif.send()

