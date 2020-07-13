import random

def compatibility(name1, name2):
    score = 50
    if(abs(len(name1)-len(name2)) <= len(name1)//2):
        score += 10
    else:
        score -= 10
    if(abs(len(name1)-len(name2)) <= len(name2)//2):
        score += 10
    else:
        score -= 10
    
    score += random.randint(-(100-score),100-score)
    if(score >= 100):
        score = 100
    if(score <= 0):
        score = 0
    return score
    
def main():
    print("Compatability score")
    name1 = input("Enter the first name: ")
    name2 = input("Enter the second name: ")
    print(compatibility(name1,name2))

if __name__ == "__main__":
    main()