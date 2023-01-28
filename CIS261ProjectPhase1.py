#
#
#
def GetEmpName():
    empname = input("Enter employee name: ")
    return empname

def GetHoursWorked():
    hours = int(input("Enter your work hours: "))
    return hours


def GetHourlyRate():
    hourlyrate = int(input("Enter Hourly rate: "))
    return hourlyrate


# write the GetTaxRate function
def GetTaxRate():
    taxrate = float(input("Enter tax rate:"))
    return taxrate




def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(empname, hours, hourlyrate,grosspay, taxrate, incometax, netpay):
    print(empname, f"{hours:,.2f}", f"{hourlyrate:.2f}",f"{grosspay:,.2f}", f"{taxrate:,.1%}",f"{incometax:,.2f}", f"{netpay:,.2f}")

def PrintTotals(TotEmployees, TotHours, TotGroosPay, TotTax, TotNetPay):
    print()
    print(f"\nTotal Number of Employees: {TotEmployees}"
          f"\nTotal Hours Worked: {TotHours:,.2f}"
          f"\nTotal Gross Pay: {TotGrossPay:,.2f}"
          f"\nTotal Tax: {TotTax:,.2f}"
          f"\nTotal Net Pay: {TotNetPay:,.2f}")
    print()
def PrintTotals(TotEmployees, TotHours, TotGrossPay, TotTax, TotNetPay):    
    print()
    print(f"Total Number Of Employees: {TotEmployees}")
    print(f"Total Hours Worked: {TotHours:,.2f}")



if __name__ == "__main__":
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    while True:
        empname = GetEmpName()
        if (empname.upper() == "END"):
            break

        hours = GetHoursWorked()
        hourlyrate = GetHourlyRate()
        taxrate = GetTaxRate()

        grosspay, incometax, netpay = CalcTaxAndNetPay(hours, hourlyrate, taxrate)
        printinfo(empname, hours, hourlyrate, grosspay, taxrate, incometax, netpay)
        TotEmployees += 1
        TotHours += hours
        TotGrossPay += grosspay
        TotTax += incometax
        TotNetPay += netpay

PrintTotals (TotEmployess, TotHours, TotGrossPay, TotTazx)

       
        













