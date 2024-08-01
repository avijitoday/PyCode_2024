import pyfiglet

def bannerText(text):
    # Create a Figlet object
    figlet = pyfiglet.Figlet(font='slant')
    # Generate the banner
    banner = figlet.renderText(text)
    return  banner


print(bannerText("ABCDQWERT"))
height = float(input("Please enter height (in Meter):"))
weight = int(input("Please enter height (in Kilogram):"))

bmi = weight / (height * height)

if bmi < 18.5 :
    print(f"You are underweight & your BMI is {bmi} !")
elif bmi <25 :
    print("Your BMI is {bmi}, you have a normal weight !")
elif bmi <25 :
    print("Your BMI is {bmi}, you have a normal weight !")
elif bmi <30 :
    print("Your BMI is {bmi}, you are slightly overweight !")
elif bmi <35 :
    print("Your BMI is {bmi}, you obase !")
else:
    print("Your BMI is {bmi}, you are clinically obase !")


