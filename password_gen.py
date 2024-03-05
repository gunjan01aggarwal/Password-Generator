import random


class  gen_password:
    def __init__(self,length,num):
        self.upper_letter=['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
        self.lower_letter=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.digits=['0','1','2','3','4','5','6','7','8','9']
        self.special_ch=['~','@','!','#','$','%','^','&','*','(',')','?',':','|']
        self.total_len=length
        self.no_of_password=num

    def gen_password(self):
        combined=self.upper_letter+self.lower_letter+self.digits+self.special_ch    
        rand_digit=random.choice(self.digits)
        rand_upper_letter=random.choice(self.upper_letter)
        rand_lower_letter=random.choice(self.lower_letter)
        rand_special_ch=random.choice(self.special_ch)

        temp_pass=rand_upper_letter+rand_lower_letter+rand_digit+rand_special_ch

        for i in range(self.total_len-4):
            temp_pass+=random.choice(combined)
            temp_pass_list=list(temp_pass)
            random.shuffle(temp_pass_list)



        password="".join(temp_pass_list)    
        
        return print(f"Generated_password is {password}")
    


length=int(input("Enter the length of a password: "))  
number=int(input("How many passwords do you want to generate? "))  
for k in range(number):
    g=gen_password(length,number)
    g.gen_password()

