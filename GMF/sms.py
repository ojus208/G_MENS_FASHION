from twilio.rest import Client 
 
account_sid = 'AC159bf72e0da7b32743c938369db9bfaa' 
auth_token = '76cfca110b1984bb7535d136f7ab5ca9' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create(  
                              messaging_service_sid='MG558627416573f90653834e32e75a9640', 
                              body='your OTP for gmf is 505050',      
                              to='+919165130008' 
                          ) 
 
print(message.sid)