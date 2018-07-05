
# coding: utf-8

# In[9]:


import sqlite3

def check_request(request):
    allwants = []
    if(request):
        #有新需求
        allwants.append(check_newtable())
        allwants.append(check_oldtable())
    else:
        print("No new request")
        
def check_database(DB_name):
    
    
#比對newtable    
def check_newtable(DB_name, request):
    wants = []
    conn = sqlite3.connect(DB_name)
    c = conn.cursor()
    c.execute("SELECT * FROM new WHERE price < ?" % request[1])
    wants = c.fetchall()
    return wants

#比對oldtable
def check_oldtable(DB_name, request):
    wants = []
    conn = sqlite3.connect(DB_name)
    c = conn.cursor()
    c.execute("SELECT * FROM old WHERE price < ?" % request[1])
    wants = c.fetchall()
    return wants
    


# In[5]:


def main():
    print("GG")
    
if __name__ == "__main__":
    main()

