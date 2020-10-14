import collections, requests, json

CredentialPlugin = collections.namedtuple('CredentialPlugin', ['name', 'inputs', 'backend'])

def call_cyberark(**kwargs):
    #
    # IMPORTANT:
    # replace this section of code with Python code that *actually*
    # interfaces with some third party credential system
    # (*this* code is just provided for the sake of example)
    #
    url = kwargs.get('url')
    cert = kwargs.get('cert')
    key = kwargs.get('key')
    appid = kwargs.get('appid')
    safe = kwargs.get('safe')
    username = kwargs.get('username')

    password = "none"

    # make tempdir for cert/keys
    tempdir = subprocess.check_output(['mktemp','-d']).decode("utf-8").replace('\n','')
    certfile = tempdir + "/" + "gpacert.crt"
    fcert = open(certpath, 'w')
    fcert.write(cert)
    fcert.close

    keyfile = tempdir + "/" + "gpa_private.key"
    fkey = open(keyfile, 'w')
    fkey.write(key)
    fkey.close

    cyberark_url = url + "?AppID=" + appid + "&Safe=" + safe + "&Username=" + username 
    resp = requests.get(cyberark_url,cert=(certfile,keyfile), verfiy=False)
    myjson = resp.json()
    password = myjson['Content']
    
    return password

    #raise ValueError(f'Could not find a value for {identifier}.')

example_plugin = CredentialPlugin(
    'My CyberArk Credential Plugin',
    # see: https://docs.ansible.com/ansible-tower/latest/html/userguide/credential_types.html
    # inputs will be used to create a new CredentialType() instance
    #
    # inputs.fields represents fields the user will specify *when they create*
    # a credential of this type; they generally represent fields
    # used for authentication (URL to the credential management system, any
    # fields necessary for authentication, such as an OAuth2.0 token, or
    # a username and password). They're the types of values you set up _once_
    # in AWX
    #
    # inputs.metadata represents values the user will specify *every time
    # they link two credentials together*
    # this is generally _pathing_ information about _where_ in the external
    # management system you can find the value you care about i.e.,
    #
    # "I would like Machine Credential A to retrieve its username using
    # Credential-O-Matic B at identifier=some_key"

    inputs={
        'fields': [{
            'id': 'url',
            'label': 'Cyberark AIM URL',
            'type': 'string',
        },{
            'id': 'appid',
            'label': 'Cyberark App ID',
            'type': 'string'
        }{
            'id': 'safe',
            'label': 'Cyberark Safe',
            'type': 'string'
        }{
            'id': 'username',
            'label': 'Cyberark Safe Username',
            'type': 'string'
        }{
            'id': 'cert',
            'label': 'Cyberark Certificate',
            'type': 'string',
            'multiline': True,
            'secret': True,
        },  {
            'id': 'key',
            'label': 'Cyberark Private Key',
            'type': 'string',
            'multiline': True,
            'secret': True,
        }],
        'required': ['url', 'appid', 'safe','username','cert','key'],
    },
    # backend is a callable function which will be passed all of the values
    # defined in `inputs`; this function is responsible for taking the arguments,
    # interacting with the third party credential management system in question
    # using Python code, and returning the value from the third party
    # credential management system
    backend = call_cyberark
)
