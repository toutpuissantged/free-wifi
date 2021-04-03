import time 

class InfoGet():

    def __init__(self):
        self.state={
			'active-time':0,
			'start-time':time.time(),
			'old-active-time':0,
			'requet-number':0,
			'connected-time':0,
			'not-connected-time':0,
			'all-freetrial-url':[],
			'mac-change-number':0,
		}

    def setState(self,name,newval):
        self.state[name]=newval

    def time_builder(self,yours):
        timer=int(yours)
        time_schema={
            'heures':0,
            'minutes':0,
            'seconde':0,
        }
        
        minute=timer//60
        time_schema['seconde']=timer
        if (minute<1):
            return time_schema
        seconde=timer%60
        minute=timer//60
        time_schema['seconde']=seconde
        time_schema['minutes']=minute
        if (minute//60<1):
            return time_schema

        heures=minute//60
        minute=minute%60
        time_schema['heures']=heures
        time_schema['minutes']=minute

        return time_schema

    def start_time(self):
        cur_time=time.time()
        new_time=cur_time-self.state['start-time']
        self.setState('old-active-time',cur_time)
        return(self.time_builder(new_time))


    def run(self):
        return self.start_time()


if __name__ == '__main__':
    from test import test
    test(InfoGet())