#Breach Bot Starter Code
breachYear = 2017

#Greets user
print("Hello! I'm Breach Bot.")
userName = input("What is your name?\n")
print("Nice to meet you " + userName)

#Recounts year of breach
todaysYear = input("What year is it?\n")
timePassed = int(todaysYear) - breachYear
print("Wow! That means it has been " + str(timePassed) + " years since the National Health Services 2017 Breach!")


#Introduces breach
print("Would you like to learn about the National Health Services 2017 Breach?")
giveInfo = input("Type 'yes' or 'no'\n")

#Explains breach
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) breach details, (b) organization's response, (c) I would like to hear your reflection")
  topic = input()
  
  if topic.lower() == "a":
    print("The NHS or the National Health Service was not able to access basic patient or medical records due to a ransomware attack that was supposedly pulled by a North Korean hacking group in 2017. The attack called WannaCry used Eternalblue, a name for a software vulnerability found in Microsoft’s operating system, and a SMB or Server Message Block, which is a file sharing protocol, in order to infect 60 NHS trusts leading to the UK losing £92 million and 19,000 canceled appointments.")
  
  elif topic.lower() == "b":
    print("NHS with the help of Marcus Hutchins, a computer security researcher, was able to utilize a kill switch to put a stop to the cyber-attack. The NHS did not give their users any advice on recommended actions, rather because the NHS was more of the victim and lost a lot from the attack they were able to get a boost in funds and investments from the government for cyber security improvement.")
  
  elif topic.lower() == "c":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")


#Introduces my take
print("\nI'm excited to share my perspective with you. Are you ready to hear my take?")
giveInfo = input("Type 'yes' or 'no'\n")

#Shares my take
while giveInfo.lower() == "yes":
  print("What would you like to learn more about? Enter the lowercase letter of the following options: \n(a) relation to the CIA Triad, (b) my reaction, (c) my advice, (d) none")
  topic = input()
  
  if topic.lower() == "a":
    print("This data breach connects to integrity because of how the ransomware used for the WannaCry attack caused the NHS’ database to become encrypted and scrambled.")
  
  elif topic.lower() == "b":
    print("I agree with the organization's response because of how they informed the public about the data breach as soon as it happened in order to lessen the public’s confusion. They also acknowledged that they were at fault as well for having ignored warnings about their outdated technology prior to the incident and have thus made changes by investmenting more into cybersecurity.")
  
  elif topic.lower() == "c":
    print("I would convince victims to take action by informing them about how dangerous data breaches can be because of how they can be used to take your private and important information. My advice would be to tell them to only entrust their important information to websites or organizations that are highly secure and trustworthy and change their passwords to be more secure.")
    
  elif topic.lower() == "d":
    break
  
  else:
    print("Sorry, I didn't catch that. Choose one of the options listed.")
  
  input("Press enter to continue\n")

  
#Chatbot ends conversation
print("Thanks for chatting with me, and I hope you learned something new!")