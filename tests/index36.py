3
	?#`  ?               @   sn   d dl Z d dlZd dlZd dlZd dlmZ d dlZdd? Z	dd? Z
dd? Zd	d
? Zdd? Zdd? Ze?  dS )?    N)?BeautifulSoupc               C   s   t d? d S )Nzreloaded ...)?print? r   r   ?&F:\code\perso\crack\hacktools\index.py?toast   s    r   c              C   s@   d} t d? td?}|dkr"d} nd} | r4t d? nt d? d S )NFzveillez vous authenntifier ...? ZgedeonTzheureux de vous revoir z!identifiant de connexion invalide)r   ?input)?isvalide?idr   r   r   ?auth   s    
r   c           	   C   s?   d} d}xb| sjyt jd?}d} W n   |d7 }tjd? Y nX |dkr
d}tjd? td? tjd? q
W |j}t|j	d	?}|j
d
?d jd?}tj|? td|? d S )NFr   zhttp://sobricom.net/loginT?   ?
   z$netsh wlan connect name="SOBRI MMM5"zerreur de connexionzhtml.parser?aZhrefzlink is )?rq?get?time?sleep?os?systemr   ?textr   ZcontentZfind_all?wbZopen_new)r	   ?loop?dataZ	dataParseZsoup?linkr   r   r   ?scraping   s&    


r   c               C   s   t jd? td? d S )Nztmac -n Wi-Fi -nr02 -re -szmac mis a jour )r   r   r   r   r   r   r   ?
macChanger4   s    
r   c              C   s?   t d? tj? } d}d}d}d}x?|r?tj? }|| | kr@d}npyPtjd? || d	 kr?ytjd
? tjd? W n   |d
7 }t d? Y nX W n   |d
7 }tjd
? Y nX |dkr?d}d}|dkr?d}tjd? t d? tjd? q"W d S )Nzconnexion checkT?<   ?   ?(   r   Fzhttp://sobricom.net/loginr   r   zhttps://www.google.com/zno internet  connexion?   ?   z$netsh wlan connect name="SOBRI MMM5"znot connected to wifi?   ??   i  )r   r   r   r   r   r   r   )?Itimer   ZrefreshZnotconectedZtourZcurtimer   r   r   ?ConnexionCheck9   s<    


r$   c              C   s>   t d? d} d}tj? }x | r8t?  t?  t?  t?  qW d S )Nzhacktools start ...Tr   r   r   r"   i  )r   r   r   r   r   r$   )ZIloopZIsleepr#   r   r   r   ?main`   s    r%   )r   r   Zrequestsr   ?sysZbs4r   Z
webbrowserr   r   r   r   r   r$   r%   r   r   r   r   ?<module>   s   '