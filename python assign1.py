def displayName(cls10):
	print ("the list of names of students of class 10");
	for x in cls10.keys():
		print (x);

#not case-sensitive........
def capitalize(string):
    for x in string[:].split(" "):
        string = string.replace(x, x.capitalize());
        string="".join(string);
    return string;
	
def displayRoll(cls10,name):
	if (name not in cls10):
		print ("Not in the record");
		return ;
	else:
		print (cls10[name]);	
		
if __name__ == '__main__':
	cls10= dict(zip(['Paige Whitehorn','Han Utz','Hong Bernhard','Damien Gadbois','Hayley Burmeister','Theola Hawkinson','Clay Prokop','Tammera Whitehair','Mee Hudman','Julee Westcott','Neely Fetter','Phillip Deloatch','Xiao Slevin','Winnifred Mikkelson','Precious Roots','Melanie Beckley','Graham Tiller','Gilma Edie','Pearl Buzzard','Marylyn Sutphin'],['N1001','N1002','N1003','N1004','N1005','N1006','N1007','N1008','N1009','N1010','N1011','N1012','N1013','N1014','N1015','N1016','N1017','N1018','N1019','N1020']));
	displayName(cls10);
	print ();
	PC = True;
	while PC:
		name= input("Enter the name of student to get his Roll code:");
#not case-sensitive........
		name=capitalize(name);
		displayRoll(cls10,name);
		flag=input("to continue press any key or for quit press Q/q");
		if (flag =='q' or flag == 'Q'):
			break;