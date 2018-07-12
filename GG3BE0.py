
# coding: utf-8

# In[56]:


import sqlite3
def check_request(request):
    if(request):
        #有新需求
        relist = []
        #符合條件的物品存放的三圍陣列
        for r in request:
            allwants = check_newtable(r)
            allwants.append(check_oldtable(r))
            if(len(allwants) == 0):
                relist.append(allwants)
            else:
                continue
        return relist
    else:
        print("No new request")
        norequest = []
        return norequest
        
def check_database(DB_name):
    print("GG")
    
#比對newtable    
def check_newtable(request):
    DB_name =  'C:\\Users\\User\\Desktop\\專題\\sqlite3\\' + request[3] + '.sqlite'
    wants = []
    conn = sqlite3.connect(DB_name)
    c = conn.cursor()
    c.execute("SELECT * FROM new WHERE price < ?", (request[2],))
    wants = c.fetchall()
    
    return wants

#比對oldtable
def check_oldtable(request):
    DB_name =  'C:\\Users\\User\\Desktop\\專題\\sqlite3\\' + request[3] + '.sqlite'
    wants = []
    conn = sqlite3.connect(DB_name)
    c = conn.cursor()
    c.execute("SELECT * FROM old WHERE price < ?", (request[2],))
    wants = c.fetchall()
    
    return wants
    


# In[57]:


def main():
    #---------------------爬蟲過程------------------
    
    
    
    #-----------------------------------------------
    #--------------------接收request----------------
    
    
    
    #-----------------------------------------------
    #-------------------尋找合適商品----------------
    reqq = [['老二王','iphone 7','15000','cellphone'],
            ['老王','Asus','200','laptop']]
    relist = check_request(reqq)
    if(len(relist) != 0):
        print(len(relist))
        print(relist[1])
    else:
        print("not found")
    #-----------------------------------------------
    #----------------------寄信---------------------
    
    
    
    #-----------------------------------------------
if __name__ == "__main__":
    main()

