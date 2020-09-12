import sleekxmpp
from sleekxmpp.exceptions import IqError, IqTimeout
from sleekxmpp.xmlstream.stanzabase import ET, ElementBase


# basado en: https://gist.github.com/deckerego/be1abbc079b206b793cf/revisions 


class Client(sleekxmpp.ClientXMPP):
    def __init__(self, username, password, instance_name=None):
        jid = "%s/%s" % (username, instance_name) if instance_name else username
        super(Client, self).__init__(jid, password)

        self.instance_name = instance_name
        self.username = username



        self.add_event_handler('session_start', self.start)
        self.add_event_handler('message', self.receive)
        self.add_event_handler("changed_subscription", self.alertFriend)
        self.register_plugin('xep_0077')
        self.register_plugin('xep_0030') # Service Discovery
        self.register_plugin('xep_0199') # XMPP Ping
        self.register_plugin('xep_0004') # Data forms
        self.register_plugin('xep_0077') # In-band Registration
        self.register_plugin('xep_0045') # Mulit-User Chat (MUC)
        self.register_plugin('xep_0047', {"auto_accept": True})
        #self.register_plugin('xep_0055') #search
        
        if self.connect():
            print("Coonectaaadoooo")
            self.process(block=False)
        else:
            raise Exception("Chequeate tu conexion a internet / server")

    def kill(self):
        print("Closing XMPP Connection")
        self.disconnect(wait=False)

    def start(self, event):
        self.send_presence(pshow='chat', pstatus='Disponible')
        print(self.get_roster())
    
    def alertFriend(self):
        self.get_roster()


    def addRoster(self, jid):
        try:
            self.send_presence_subscription(pto=jid)
            print("User added to roster")
        except IqError:
            raise Exception("Unable to add user to rooster")
        except IqTimeout:
            raise Exception("Server not responding")


    
    def getAllUsers(self,jid, domain):
        
        users = self.Iq()
        users['type'] = 'set'
        users['from'] = jid
        users['id'] = 'search_result'
        
        users['to'] = "search."+self.instance_name
        
        itemXML = ET.fromstring("<query xmlns='jabber:iq:search'>\
                                 <x xmlns='jabber:x:data' type='submit'>\
                                    <field type='hidden' var='FORM_TYPE'>\
                                        <value>jabber:iq:search</value>\
                                    </field>\
                                    <field var='Username'>\
                                        <value>1</value>\
                                    </field>\
                                    <field var='search'>\
                                        <value>*</value>\
                                    </field>\
                                </x>\
                                </query>")
        users.append(itemXML)
        print(users)
        try:
            resp = users.send()
            print(resp)
        except IqError as e:
            print(e.iq)
        except IqTimeout:
            print("timeout")

    def send_msg(self, recipient, body):
        self.send_message(recipient,body,None,"chat")
    

    def commitSuicide(self, username):
        delete = self.Iq()
        delete['type'] = 'set'
        delete['from'] = username
        itemXML = ET.fromstring("<query xmlns='jabber:iq:register'><remove/></query>")
        delete.append(itemXML)
        print(delete)
        try:
            delete.send()
            #print("Account deleted succesfuly")
        except IqError as e:
            raise Exception("Unable to delete username", e)
        except IqTimeout:
            raise Exception("Server not responding")

    def wait_msg(self, message):
        print("called function")
        if message['type'] in ('chat', 'normal'):
            print("XMPP Message: %s" % message)
            from_account = "%s@%s" % (message['from'].user, message['from'].domain)
            print("%s received message from %s" % (self.instance_name, from_account))

    def msg_group(self, room, body):
        self.send_message(mto=room, mbody=body, mtype='groupchat')
    
    def join_group(self, room, name):
        self.plugin['xep_0045'].joinMUC(room, name, wait=True)

clientxmpp = Client('fran@redes2020.xyz', '123456', 'redes2020.xyz')
#clientxmpp.send_msg('prueba1@redes2020.xyz', "hola mafer!")
clientxmpp.getAllServerUsers("fran@redes2020.xyz","redes2020.xyz")
#clientxmpp.deleteUser("fran@redes2020.xyz")
