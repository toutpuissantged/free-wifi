from modules import * 

class HackTools(object):
    	
	def __init__(self):
		self.config={
			'user':'dev',
			'ssid':'SOBRI MMM5',
			'url':'http://sobricom.net/login',
			'ssid_list':['SOBRI MMM5','SOBRICOM','SOBRICOM 2','SOBRICOM 3','WIFI FOZANE 2'],
			'test':'https://www.google.com/',
			'refresh':60*4+10,
			'dev-data':{
				'ssid':'SOBRI MMM5',
				'url':'http://sobricom.net/login',
				'ssid_list':['SOBRI MMM5','SOBRICOM','SOBRICOM 2','SOBRICOM 3','WIFI FOZANE 2'],
				'test':'https://www.google.com/',
				'refresh':1,
			},
		}
		self.state={
            'statut':'connected',
            'reload':0,
            'wifi-name':'Sobri mimi',
            'username':'gedeon',
            'app-name':'HACKTOOLS,'

        }
		self.wifi_used=self.config['ssid']
		self.link=""
		self.infoget=InfoGet()
		self.interface=Interface(self.state)
		self.version = version()




	def arg_pars(self):
		pass

	def configLoad(self):
		temp1=open('core/version.json','r')
		temp2=temp1.read()
		temp1.close()

		temp3=json.loads(temp2)

		return temp3

	def header(self):
		print('hack tools')
		print("version {}  by anonymous13 \n".format(self.version))
		#auth()
		print("demarage du moteur ...")

	def Connect(self,ssid):
    		
		call=os.system('netsh wlan connect name="{}"'.format(ssid))
		#print('not connected to wifi ||| call :{}'.format(call))
		return call

	def toast(self):
		'''  
			permet de faire des notif a chaque reload de la boucle pricipale 
		'''
		print('reloaded ...')
		#sys.exit()	

	def scraping(self):
		'''
			soccupe de recuperer le liens de free trial et 
			l'ouvre dans un nouvel onglet du navigateur par defaut
		'''
		isvalide=False
		loop=0
		
		while not isvalide:
			
			try:
				data=rq.get(config['url'])
				isvalide=True
				
			except :
				loop+=1
				time.sleep(1)
			if loop>=10:
				loop=0
				self.Connect(self.wifi_used)
				time.sleep(1)

		dataParse=data.text
		soup = BeautifulSoup(data.content, 'html.parser')
		link=soup.find_all("a")[0].get('href')
		#link=soup.find('a').get('href')
		wb.open(self.link)
		self.state['statut']= 'connecting ...'
		
		#print('link is ',self.link)

	def macChanger(self):
		'''
			change aleatoirement l'adresse mac 
		'''
		os.system('tmac -n Wi-Fi -nr02 -re -s')
		
		#print('mac mis a jour ')

	def ConnexionCheck(self):
		'''
			le composent intelligent du core : verifier et resout les probleme de 
			connexion au wifi et a internet 
		'''
		#print('connexion check')
		
		Itime=time.time()
		loop=True
		refresh=self.config['dev-data']['refresh'] # temps de rafraichissement 
		notconected=0
		tour=1
		max_notconected=5
		max_tour=5
		first_loop=True
		first_loop_state=1
		wifi_used_id=0

		while loop:
			curtime=time.time()
			if curtime >=Itime+refresh:
				loop=False
				self.state['statut']= 'reloading'
			else:
				time.sleep(1)
				try:
					rq.get(config['url'])
					self.state['statut']= 'connected'
					if curtime >=Itime+10:
						try:
							rq.get(config['test'])
						except:
							#loop=False
							notconected+=1
							self.state['statut']= 'no internet  connexion'
							#print('no internet  connexion')
							
							wb.open(link)
							#print('link is ',link)
							time.sleep(2)

				except:
					tour+=1
					self.state['statut']= 'disconnected'

			if notconected>=max_notconected:
				notconected=0
				loop=False

			if tour>=max_tour :
				tour=0
				self.Connect(self.wifi_used)

			if first_loop==True :
				
				first_loop_state=self.Connect(self.wifi_used)
				if first_loop_state:
					first_loop=True
				else:
					first_loop=False
						
				#first_loop=False
				#print('@ first loop')
				time.sleep(1)

			time.sleep(2)

	def start(self):
		'''
			boucle principale 
		'''
		os.system('cls' if os.name=='nt' else 'clear')
		self.header()
		while True:
			self.interface.reload(self.state)
			self.interface.run()
			try:
				if (self.config['user']!='dev'):
					self.macChanger()
					self.scraping()
					self.toast()
				try :
					self.ConnexionCheck()
				except:
					pass
			except:
				pass

hack = HackTools()

hack.start()


### hack tools by anonymous13 ###