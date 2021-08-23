from art import logo

def add(n1,n2):
	return n1+n2

def subtract(n1,n2):
	return n1-n2

def multiply(n1,n2):
	return n1*n2

def divide(n1,n2):
	return n1/n2

new_dict={}
new_dict= {"+":add,
"-":subtract,
"*":multiply,
"/":divide
}

def calculator():
	print(logo)
	n1=float(input("Enter first number "))
	for operation in new_dict:
		print(operation)

	want_more_calulation=True
	while want_more_calulation:
		
		op=input("Pick an operation ")
		n2=float(input("Enter next number "))
		calculation_operation=new_dict[op]
		final_answer=calculation_operation(n1,n2)
		print(final_answer)

		want_more=input(f"Type 'y' to continue calulating with {final_answer} else types 'n' ").lower()
		if want_more=="y":
			n1=final_answer
			want_more_calulation=True
			
		else:
			want_more_calulation=False
			calculator()

calculator()
