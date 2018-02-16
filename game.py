from time import sleep

loan_flag = False
land_flag = False
probing_equipment_flag = False
probing_cost_flag = False
dig_equipment_flag = False
dig_cost_flag = False
sell_flag = False




account = 0
cash = 0

def set_loan(loan):
    account -= loan
    cash += loan
    loan_flag = True

while True:
    if loan_flag:
        loan = raw_input("Plaese input the loan: ")
        set_loan(loan)
    if land_flag:
        
