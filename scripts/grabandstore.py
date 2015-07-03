#!/usr/local/bin/pythonw
import psycopg2
import urllib2
import getopt
import sys
import xml.etree.ElementTree as ET


USAGE="""This is utility which downloads all characters details and updates the tables 
 -u url for character to be updated 
 -n list all database character table where status is no_info = 0
 -f list all database character table where status is full_info = 1
 -d id download and update the character"""

#Default url for Superman http://www.comicvine.com/api/character/4005-1807/
char_url = ""
api_key ="api_key=d9f41720aa3d6b4917672d37fee0e78c6d0cc33c" 
#Characters required data 
char_field_list = "field_list=aliases,name,id,api_detail_url,real_name,powers,character_friends,character_enemies,image"
char_id=""
list_n=0
list_f=0
final_get_url=""

def character_pupdate(id,api_detail,name):
            value =0
	    conn = psycopg2.connect(database="comicsdatabase",user="mehuljani")
	    cur = conn.cursor()
	    prevrow = ""
	    
	    try:
	       cur.execute("Select name from character where id=%s" % id)
            except psycopg2.DatabaseError, e:
    	    #   print 'Error %s' % e    
               sys.exit(1)
	    
            prevrow = cur.fetchone()
#	    #print prevrow

	    if prevrow:
		#print "This Needs Update Query\n"
    	        try:
	           cur.execute("UPDATE character SET name=%s,source_url=%s where id=%s", (name,api_detail,id))
	           conn.commit()
                except psycopg2.DatabaseError, e:
    	        	#print 'Error %s' % e    
               		sys.exit(1)
	    else:
		#print "This is insert query \n" 
    	        try:
	           cur.execute("INSERT INTO character(id,name,source_url,status) values(%s,%s,%s,%s)", (id,name,api_detail,value))
	           conn.commit()
		   conn.close()
                except psycopg2.DatabaseError, e:
    	        	#print 'Error %s' % e    
               		sys.exit(1)


def character_update(name,real_name,id,aliases,api_detail,image):
            value =1
	    conn = psycopg2.connect(database="comicsdatabase",user="mehuljani")
	    cur = conn.cursor()
	    prevrow = ""
	    
	    try:
	       cur.execute("Select name from character where id=%s" % id)
            except psycopg2.DatabaseError, e:
    	       #print 'Error %s' % e    
               sys.exit(1)
	    
            prevrow = cur.fetchone()
	    #print prevrow

	    if prevrow:
		#print "This Needs Update Query\n"
    	        try:
	           cur.execute("UPDATE character SET name=%s,real_name=%s,aliases=%s,source_url=%s,status=%s,image=%s where id=%s", (name,real_name,aliases,api_detail,value,image,id))
	           conn.commit()
                except psycopg2.DatabaseError, e:
    	        	#print 'Error %s' % e    
               		sys.exit(1)
	    else:
		#print "This is insert query \n" 
    	        try:
	           cur.execute("INSERT INTO character(id,name,real_name,aliases,source_url,status,image) values(%s,%s,%s,%s,%s,%s,%s)", (id,name,real_name,aliases,api_detail,value,image))
	           conn.commit()
		   conn.close()
                except psycopg2.DatabaseError, e:
    	        	#print 'Error %s' % e    
               		sys.exit(1)

def power_update(id,api_detail,name):
	    conn = psycopg2.connect(database="comicsdatabase",user="mehuljani")
	    cur = conn.cursor()
	    prevrow = ""
	    
	    try:
	       cur.execute("Select name from power where id=%s" % id)
            except psycopg2.DatabaseError, e:
    	       #print 'Error %s' % e    
               sys.exit(1)
	    
            prevrow = cur.fetchone()
	    #print prevrow

	    if prevrow:
		#print "This Needs Update Query\n"
    	        try:
	           cur.execute("UPDATE power SET name=%s,url=%s where id=%s", (name,api_detail,id))
	           conn.commit()
                except psycopg2.DatabaseError, e:
    	        	#print 'Error %s' % e    
               		sys.exit(1)
	    else:
		#print "This is insert query \n" 
    	        try:
	           cur.execute("INSERT INTO power(id,name,url) values(%s,%s,%s)", (id,name,api_detail))
	           conn.commit()
		   conn.close()
                except psycopg2.DatabaseError, e:
    	        #	print 'Error %s' % e    
               		sys.exit(1)

def character_power_update(cid,pid):
	    conn = psycopg2.connect(database="comicsdatabase",user="mehuljani")
	    cur = conn.cursor()
	    prevrow = ""
	    
	    try:
	       cur.execute("Select char_id,power_id from character_power where char_id=%s and power_id=%s" % (cid,pid))
            except psycopg2.DatabaseError, e:
    	       #print 'Error %s' % e    
               sys.exit(1)
	    
            prevrow = cur.fetchone()
	    #print prevrow

	    if prevrow:
		#print "This Needs Update Query\n"
    	       # try:
	       #    cur.execute("UPDATE character_power SET power_id=%s where char_id=%s", (pid,cid))
	       #    conn.commit()
               # except psycopg2.DatabaseError, e:
    	       # 	print 'Error %s' % e    
               #		sys.exit(1)
	    else:
		#print "This is insert query \n" 
    	        try:
	           cur.execute("INSERT INTO character_power(char_id,power_id) values(%s,%s)", (cid,pid))
	           conn.commit()
		   conn.close()
                except psycopg2.DatabaseError, e:
    	        	#print 'Error %s' % e    
               		sys.exit(1)

def character_fande_update(cid,feid,ch):
	    conn = psycopg2.connect(database="comicsdatabase",user="mehuljani")
	    cur = conn.cursor()
	    prevrow = ""
	    
	    try:
	       cur.execute("Select char_id from character_fande where char_id=%s and fande_id=%s", (cid,feid))
            except psycopg2.DatabaseError, e:
    	       #print 'Error %s' % e    
               sys.exit(1)
	    
            prevrow = cur.fetchone()
	    #print prevrow

	    if prevrow:
		#print "This Needs Update Query\n"
    	        try:
	           cur.execute("UPDATE character_fande SET flag=%s where char_id=%s and fande_id=%s", (ch,cid,feid))
	           conn.commit()
                except psycopg2.DatabaseError, e:
    	        	#print 'Error %s' % e    
               		sys.exit(1)
	    else:
		#print "This is insert query \n" 
    	        try:
	           cur.execute("INSERT INTO character_fande(char_id,fande_id,flag) values(%s,%s,%s)", (cid,feid,ch))
	           conn.commit()
		   conn.close()
                except psycopg2.DatabaseError, e:
    	        	print 'Error %s' % e    
               		sys.exit(1)

# if -u url is provided then set char_url as arg
# aa:
def usage():
	print USAGE

def download(url):
	"""Copy the contents of a file from a given URL
	to a local file.
	"""
	import urllib
	webFile = urllib.urlopen(url)
	localFile = open("../images/" + url.split('/')[-1], 'w')
	localFile.write(webFile.read())
	webFile.close()
	localFile.close()


def getandupdate():
	#print char_url
	final_get_url = char_url + "?" + api_key + "&" +  char_field_list
	#print "\n" + final_get_url
	resp = urllib2.urlopen(final_get_url).read()
	# print "\n\n\n" + resp
	tree = ET.fromstring(resp)
	
	for ch in tree.iterfind('./results/name'):
		name= ch.text

	for ch in tree.iterfind('./results/real_name'):
		real_name= ch.text

	for ch in tree.iterfind('./results/id'):
		id = ch.text

	for ch in tree.iterfind('./results/aliases'):
		aliases = ch.text

	for ch in tree.iterfind('./results/api_detail_url'):
		api_detail = ch.text

	for ch in tree.iterfind('./results/image/small_url'):
		image = ch.text

        download(image); 
        image = "../images/" + image.split('/')[-1] 

#	print name,real_name,id,aliases.replace("\n",":"),api_detail,image
	character_update(name,real_name,id,aliases,api_detail,image)

	#print "These are are my powers :\n"
	power = {}
	for ch in tree.iterfind("./results/powers/"):
		for ch2 in ch.iter():
        		power[ch2.tag]=ch2.text
		#print power["id"],power["api_detail_url"],power["name"]
		power_update(power["id"],power["api_detail_url"],power["name"])
		character_power_update(id,power["id"])

	#print "These are are my enemies :\n"
	enemies = {}
	for ch in tree.iterfind("./results/character_enemies/"):
		for ch2 in ch.iter():
        		enemies[ch2.tag]=ch2.text
		#print enemies["id"],enemies["api_detail_url"],enemies["name"]	
		character_pupdate(enemies["id"],enemies["api_detail_url"],enemies["name"])
		character_fande_update(id,enemies["id"],0)

	#print "These are are my friends :\n"
	friends = {}
	for ch in tree.iterfind("./results/character_friends/"):
		for ch2 in ch.iter():
        		friends[ch2.tag]=ch2.text
		#print friends["id"],friends["api_detail_url"],friends["name"]	
		character_pupdate(friends["id"],friends["api_detail_url"],friends["name"])
		character_fande_update(id,friends["id"],1)

	sys.exit(0)

def getlistnoinfo():
	    conn = psycopg2.connect(database="comicsdatabase",user="mehuljani")
	    cur = conn.cursor()
	    prevrow = ""
	    
	    try:
	       cur.execute("Select * from character where status=0")
            except psycopg2.DatabaseError, e:
    	       print 'Error %s' % e    
               sys.exit(1)
	    
            prevrow = cur.fetchall()
	    #print prevrow
	    for row in prevrow:
	    	#print " ",row


def getlistfullinfo():
	    conn = psycopg2.connect(database="comicsdatabase",user="mehuljani")
	    cur = conn.cursor()
	    prevrow = ""
	    
	    try:
	       cur.execute("Select * from character where status=1")
            except psycopg2.DatabaseError, e:
    	       #print 'Error %s' % e    
               sys.exit(1)
	    
            prevrow = cur.fetchall()
	    #print prevrowi
	    for row in prevrow:
	    	#print " ",row


# if -u url is provided then set char_url as arg
def main():
	try :
 		opts,args = getopt.getopt(sys.argv[1:],"u:nfd:")
	except getopt.GetoptError as err:
        	# print help information and exit:
        	#print(err) # will print something like "option -a not recognized"
        	usage()
        	sys.exit(2)

	for o,a in opts:
		if o == "-u":
			global char_url
			char_url = a
			getandupdate()
		elif o == "-n" :
			list_n = 1
			getlistnoinfo()
		elif o == "-f" :
			list_f = 1
			getlistfullinfo()
		elif o == "-d" :
			char_id = a
		else:
			usage()
			sys.exit(2)	


if __name__ == "__main__":
	main()
