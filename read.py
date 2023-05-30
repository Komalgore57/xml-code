import yaml
import sqlite3

def checkLeave(company,employ_id):
    conn = sqlite3.connect('test.db')
    data = tuple(conn.execute(f"SELECT leave,name from {company} WHERE ID={employ_id} ;"))
   # print(data[0][0],'****')
    if(data[0][0]<1):
        return False
    else:
        return True


def managerApproval(employ_id,):
    responce = input(f"employee id: {employ_id}  asking for leave ==> YES OR NO !!")
    return 'y' in responce.lower()
    

def hRApproval(employ_id=123):
    responce = input(f"employee id: {employ_id}  asking for leave ==> YES OR NO !!")
    return 'y' in responce.lower()


with open('config.yml', 'r') as file:
    prime_service = yaml.safe_load(file)
    
    
# company='gvc'
# employ_id=1


def process(company,employ_id):
    conn = sqlite3.connect('test.db')
    data = list(conn.execute(f"SELECT leave,name from {company} WHERE ID={employ_id} ;"))
    if(data[0]==0):
        return 0
    else:
        steps=prime_service['company'][company]['process']['Leave-Management']
        totalSteps=steps['total-steps']
        for i in range(1,totalSteps+1):
            procedureName =steps['step'+str(i)]
            procedure =list(steps['step'+str(i)].keys())[0]
            
           # print(list(procedureName.keys())[0])
            if(procedure=='leave-count' and  procedureName['leave-count']['required']):

               # print(procedureName)
                print(checkLeave(company,employ_id))
                if(checkLeave(company,employ_id) ):
                    print("You have leave balance !!")
                    
                else:
                    return 'NO BLANCE'
            elif(procedure=='Manager-Approval' and  procedureName['Manager-Approval']['required']):
                print(f'Gone to {list(steps["step"+str(i)].keys())[0]}')
                if managerApproval(employ_id=employ_id):
                    pass
                else:
                    return 'MANAGER DISAPPROVED !!!'
            elif(procedure=='HR-Approval' and  procedureName['HR-Approval']['required']):
                print(f'Gone to {list(steps["step"+str(i)].keys())[0]}')
                if hRApproval(employ_id=employ_id):
                    pass
                else:
                    return 'HR DISAPPROVED !!!'
            elif(procedure=='send-Email' and  procedureName['send-Email']['required']):
                print("EMIAL SEND")
        query=f'''UPDATE {company} SET leave = leave - 1 where id = {employ_id}'''
        conn.execute(query)
        conn.commit()
        conn.close()
        return "APPROVED !!"
            
            
#print(process(company='gvc',employ_id=1))