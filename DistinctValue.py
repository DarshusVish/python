def distinct_char(ip1, ip2):
    ip1 = "".join(x.split())           # remove space from string
    if ip2 in ip1 and ip1.count(ip2) >= 2:
        ipr = ip1[::-1]                 # reverse the string to find 2nd character
        i1 = ip1.index(ip2)
        print(f"first {ip2} is at ",i1)
        i2 = len(ip1) - ipr.index(ip2) -1
        print(f"Last {ip2} is at",i2)
        sf = ip1[(i1+1):i2]         # No of letter in between first and last letter with duplication
        f = sf.replace(ip2,'')      # duplication removed
        print(f"Distinct letters are: {list(f)} \nNo of letters are: {len(f)}")
        return len(f)                  # return final value
    else:
        return -1

x = input("Enter 1st string:")
y = input("Enter 2nd string:")[0]

distinct_char(x,y)
