
from modules import InfoGet
import os,time

class Interface():

    def __init__(self,state):
        self.info=InfoGet()
        os.system('cls' if os.name=='nt' else 'clear')
        self.state=state

    def setState(self,name,val):
        self.state[name]=val

    def reload(self,state):
        self.state['reload']+=1
        self.state=state
        self.state['statut']='not connected'
    
    def run(self):
        if True:
            os.system('cls' if os.name=='nt' else 'clear')
            #print(self.info.run(),end="\r")
            data=self.info.run()
            heures=''
            minutes=''
            seconde=''
            if(data['heures']>0):
                heures=' {} h'.format(data['heures'])

            if(data['minutes']>0):
                minutes=' {} m'.format(data['minutes'])

            if(data['seconde']>0):
                seconde=' {} s'.format(data['seconde'])

            print(" > {} : {} \t  reload : {} \t --- {} --- \t user > {} \t active time >{} {} {} ".format(self.state['wifi-name'],self.state['statut'],self.state['reload'],self.state['app-name'],self.state['username'],heures,minutes,seconde),end="\r")
            time.sleep(1)

if __name__ == '__main__':
    from test import test
    test(Interface())