import xmpp


class Connection:
    conn = None
    def __init__(self, name):
        self.connection = None
        self.jid = None
        self.domain = '@redes2020.xyz'
        self.user = name+self.domain

    def connect(self):
        self.jid = xmpp.JID(self.user)
        cli = xmpp.Client(self.jid.getDomain())
        cli.connect()
        return cli
        

    '''
    expects user and pw.
    USER: aaaa@redes2020.xyz
    '''

    def register(self,pw):
        #print(self.jid.getDomain())
        cli = self.connect()
        if(cli):
            if xmpp.features.register(cli, self.jid.getDomain(), {'username': self.jid.getNode(), 'password': pw}):
                return 0
            else:
                return -1
        else:
            return -1

    '''
    receiver: aaaa@redes.2020.xyz
    message: xxxx
    '''

    def send_message(self, receiver, message):
        self.connection.send(xmpp.Protocol.Message(receiver, message))

    def handle_incoming(self, val):
        print(val)

    def receive_message(self):
        self.connection.RegisterHandler('message', handle_incoming)
