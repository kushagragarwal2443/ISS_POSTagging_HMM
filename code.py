import numpy as np

def main():
    '''This function takes input of Emission Matrix and Transition Matrix and prints if they are correct
    
    Input Parameter: None
    Return Value:None
    Function Calls: check_emis() and check_trans()'''
    
    #Introductory Message
    print("\nWelcome to the Experiment: POS Tagging using Hidden Markov Model")
    print("\nThe corpus for which you need to fill the Transition and Emission Matrices is: \n")
    print("EOS/eos Book/verb a/determiner car/noun EOS/eos Park/verb the/determiner car/noun EOS/eos The/determiner book/noun is/verb in/preposition the/determiner car/noun EOS/eos The/determiner car/noun is/verb in/preposition a/determiner park/noun EOS/eos\n")

    #Initialising the input and answer matrices
    answer_emis=[[0,0,0,0,0,1,1],[0.5,0.5,1,0,0,0,0],[0.5,0.5,0,1,0,0,0],[0,0,0,0,1,0,0]]
    answer_trans=[[0,0.33,0,0.5,0],[0,0,1,0,0],[1,0,0,0.5,0],[0,0.33,0,0,1],[0,0.33,0,0,0]]
    emission=np.zeros((4,7))
    transition=np.zeros((5,5))

    #Input Emission Matrix
    print("Enter the Emission Matrix for the above corpus")
    for i in range(4):
        for j in range(7):
            print("Value at  (",i+1,", ",j+1,") is: ",sep="",end="")
            emission[i][j]=input()
    
    #Input Transition Matrix
    print("\nEnter the Transition Matrix for the above corpus")
    for i in range(5):
        for j in range(5):
            print("Value at  (",i+1,", ",j+1,") is: ",sep="",end="")
            transition[i][j]=input()
    
    
    #Checking Emission Matrix
    print("\nEmission Matrix entered by you is:\n")
    print(emission)
    print("\nChecking your Emission Matrix against the correct one: G-Green R-Red\n")
    flag1=check_emis(emission,answer_emis)
    if(flag1==0):
        print("\nYour Emission Matrix is correct\n")
    else:
        print("\nYour Emission Matrix is wrong")
        res=input("Enter ||| 1 to check correct answer ||| 0 to End: ")
        if(res=="1"):
            print("\nThe Correct Emission Matrix is: \n")
            answer_emission=np.matrix(answer_emis)
            print(answer_emission)
            print("\n")
        else:
            print("\n")


    #Checking Transition Matrix
    print("Transition Matrix entered by you is:\n")
    print(transition)
    print("\nChecking your Transition Matrix against the correct one: G-Green R-Red\n")
    flag2=check_trans(transition,answer_trans)
    if(flag2==0):
        print("\nYour Transition Matrix is correct\n")
    else:
        print("\nYour Transition Matrix is wrong")
        res=input("Enter ||| 1 to check correct answer ||| 0 to End: ")
        if(res=="1"):
            print("\nThe Correct Transition Matrix is: \n")
            answer_transition=np.matrix(answer_trans)
            print(answer_transition)
            print()
        else:
            print("\nThankyou!")
    
    #End of main



def check_trans(transition,answer_trans):
    '''This function takes in as input the transition matrix input by the user and the correct transition matrix.
    It outputs for each index Entered_Value:Right/Wrong

    Input Parameter: 
    transition: This is the transition matrix input by the user
    answer_trans: This is the correct transition matrix
    
    Return Value: flag: 1 if the matrices do not match and 0 if they do
    Function Calls: None'''
    
    #Initialising flag and Result matrix
    flag=0
    result=[['G' for i in range(5)]for j in range(5)]

    #Changing Result Matrix if there is any mismatch
    for i in range(5):
        for j in range(5):
            if(transition[i][j]!=answer_trans[i][j]):
                result[i][j]='R'
                flag=1
    
    #Printing Entered Value:Right/Wrong
    for i in range(5):
        for j in range(5):
            print(transition[i][j],":",result[i][j],sep="",end="   ")
        print()

    #Returns 0 if matrix is totally correct and 1 otherwise
    return flag



def check_emis(emission,answer_emis):
    '''This function takes in as input the emission matrix input by the user and the correct emission matrix.
    It outputs for each index Entered_Value:Right/Wrong

    Input Parameter: 
    emission: This is the emission matrix input by the user
    answer_emis: This is the correct emission matrix
    
    Return Value: flag: 1 if the matrices do not match and 0 if they do
    Function Calls: None'''

    #Initialising flag and Result matrix
    flag=0
    result=[['G' for i in range(7)]for j in range(4)]

    #Changing Result Matrix if there is any mismatch
    for i in range(4):
        for j in range(7):
            if(emission[i][j]!=answer_emis[i][j]):
                result[i][j]='R'
                flag=1
    
    #Printing Entered Value:Right/Wrong
    for i in range(4):
        for j in range(7):
            print(emission[i][j],":",result[i][j],sep="",end="   ")
        print()

    #Returns 0 if matrix is totally correct and 1 otherwise
    return flag

main()


