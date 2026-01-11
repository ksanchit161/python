# def validateTicket(ticket_ID):
    
#         if not ticket_ID.startswith("TKT-"):
#             raise Exception("Bad Input")
        
#         code = ticket_ID[4:]

#         if len(code) != 4:
#             raise Exception("Bad Format")
        
#         digits = code[:2]
#         letters = code[2:]

#         if digits.isdigit() and letters.isalpha() and letters.isupper():
#             print("Valid Ticket")
#         else:
#             raise Exception("Bad Format")
            
# validateTicket("TKT-12AB")

code=input()
def validate(code):
    if not code.startswith("CHEM-"):
        raise Exception("Protocol Error")
    temp=code.split("-")
    if (not temp[1][0].isupper()) or (not len(temp[1])==5) or (not code[6:].isdigit()):
        raise Exception("Format Error")
    else:
        print("Batch ready")
validate(code)
    