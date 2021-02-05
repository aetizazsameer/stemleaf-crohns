# Created as a part of The STEM & Leaf Corps Computational Biology Program Fall 2020.
# All rights to this work retained.

import math
import random

global name, location, genetics, smoker, nsaids, high_fat, ATG16L1, IRGM, NOD2, IL23R
crohns = started = developed = simulated = False


def execute(userinput):
    global name, crohns, genetics, smoker, nsaids, high_fat, ATG16L1, IRGM, NOD2, IL23R
    if userinput == "exit":
        exit()
    elif userinput == "help":
        print("Commands: help, start, develop, simulate, exit")
    elif userinput == "start":
        global started
        name = input("What is the person's name? ").title()
        genetics = strbool(input(f"Does {name} have relatives with Crohn's disease? "))
        smoker = strbool(input(f"Does {name} smoke? "))
        nsaids = strbool(input(f"Does {name} regularly use aspirin, ibuprofen, or birth control? "))
        high_fat = strbool(input(f"Does {name} have a high-fat diet? "))
        ATG16L1 = strbool(input(f"Does {name} have a mutation in the ATG16L1 protein-encoding gene? "))
        IRGM = strbool(input(f"Does {name} have a mutation in the IRGM protein-encoding gene? "))
        NOD2 = strbool(input(f"Does {name} have a mutation in the NOD2 protein-encoding gene? "))
        IL23R = strbool(input(f"Does {name} have a mutation in the IL23R receptor? "))

        if genetics:
            print(f"\n{name}'s family medical history indicates that he/she is genetically predisposed to "
                  f"Crohn's disease. ")
        if smoker:
            print(f"\n{name}'s smoking habits increase his/her likelihood of developing Crohn's disease. ")
        if nsaids:
            print(f"\n{name}'s usage of non-steroidal anti-inflammatory drugs slightly increases his/her likelihood "
                  f"of developing Crohn's disease. ")
        if high_fat:
            print(f"\n{name}'s high-fat diet slightly increases his/her likelihood of developing Crohn's disease. ")
        if ATG16L1:
            print(f"\n{name} has a mutation in the ATG16L1 gene, which encodes for the Autophagy related "
                  f"16 like 1 protein, which in turn typically regulates autophagy, the recycling of cell parts "
                  f"and proteins when they are no longer needed by the body. "
                  f"\nMutations in the ATG16L1 gene tend to correlate to mutations in the NOD2 gene as well as "
                  f"increased risk of developing Crohn's disease. ")
        if IRGM:
            print(f"\n{name} has a mutation in the IRGM gene, which encodes for the Immunity-related GTPase family M "
                  f"protein, which in turn typically plays a role in innate immunity and autophagy, the recycling of "
                  f"cell parts and proteins when they are no longer needed by the body. "
                  f"\nMutations in the IRGM gene tend to correlate to increased susceptibility to Crohn's disease. ")
        if NOD2:
            print(f"\n{name} has a mutation in the NOD2 gene, which encodes for Nucleotide-binding oligomerization "
                  f"domain-containing protein 2, which in turn typically regulates the expression of antimicrobial "
                  f"peptides, recognizes bacterial molecules, and prompts immune responses. "
                  f"\nThe NOD2 gene can bind to ATG16L1 and other adaptor proteins. Mutations in the gene tend to "
                  f"correlate to mutations in the ATG16L1 gene and increased risk of developing Crohn's disease. ")
        if IL23R:
            print(f"\n{name} has a mutation in the IL23R gene, the receptor for IL23, which help differentiate "
                  f"T-helper 17 cells. In turn these inhibit T regulatory cells which can calm inflammation. "
                  f"\n A harmful mutation in the IL23R gene worsens its ability to bind IL23R, and thereby decreases "
                  f"the amount of differentiation in T-helper 17 cells and increases the activity of T regulatory "
                  f"cells. As a result, {name}'s immune system is at a decreased risk of prompting an excessive "
                  f"immune response.")

        chance = 2
        factors = IL23R, genetics, smoker, nsaids, high_fat, ATG16L1, IRGM, NOD2
        for i in factors:
            if factors.index(i) == 0 and i:
                chance -= 1
            if factors.index(i) > 0 and i:
                chance += 1

        if random.randint(1, 10) <= chance:
            print(f"\n{name} is at risk of developing Crohn's disease. ")
            crohns = started = True
        else:
            print(f"\n{name} is at low risk of developing Crohn's disease. ")
            crohns = started = False
            if strbool(input(f"\nFor demonstration purposes, would you like to increase {name}'s risk of developing "
                             f"Crohn's disease? ")):
                print(f"\n{name} is at risk of developing Crohn's disease. ")
                crohns = started = True
            else:
                exit()
    elif userinput == "develop":
        developing()
    elif userinput == "simulate":
        simulate()
    else:
        print("\nError: type help for a list of commands. ")


def developing():
    global crohns, location, developed

    if not started:
        print("Error: run start before develop!")

    else:
        def secrete_cytokines():
            if random.randint(0, 1) == 1:
                print(f"\nMacrophages in mucosal epithelial barriers along {name}'s gastrointestinal tract "
                      f"secreted cytokines excessively, prompting an immune response. ")
            else:
                if strbool(input(f"\nMacrophages in mucosal epithelial barriers along {name}'s gastrointestinal tract "
                                 f"secreted cytokines in usual quantities. For demonstration purposes, would you like "
                                 f"this to be increased to excessive quantities? ")):
                    print(f"\nMacrophages in mucosal epithelial barriers along {name}'s gastrointestinal tract "
                          f"secreted cytokines excessively, prompting an immune response. ")
                else:
                    exit()

        def immune_response():
            global location
            locations = "mouth", "esophagus", "stomach", "intestine", "intestine", "intestine", \
                        "colon", "colon", "colon"
            location = locations[random.randint(0, 8)]

            # intestine and colon are the likeliest locations to develop Crohn's disease
            print(f"The immune response caused inflammation in {name}'s {location}, marking the development of "
                  f"Crohn's disease. ")

        if crohns:
            secrete_cytokines()
            immune_response()
            developed = True


def strbool(s):
    if s.lower() in ("yes", "true", "y", "t", "1"):
        return True
    elif s.lower() in ("no", "false" "n", "f", "0"):
        return False


def simulate():
    global simulated
    if not started or not developed:
        print("Error: run develop before simulate!")
    else:
        simulated = True
        remission = False

        age = random.randint(20, 30)
        # 20-30 is the most common age for Crohn's to be diagnosed.
        ending_age = 73 + random.randint(-6, 2)
        # 73 is the global life expectancy, but Crohn's patients tend to have slightly reduced life expectancies.
        cancer = gastrointestinal_obstruction = tiredness = weakness = anemia = parasite_exposure = \
            episcleritis = scleritis = False

        while age < ending_age:
            print(f"\n{name}'s current age is {age}. ")
            rand = random.randint(0, 3)
            if not remission and rand == 0:
                remission = True
                print(f"\n{name} is now in remission. ")
            elif remission and rand != 0:
                remission = False
                print(f"\n{name} is no longer in remission. ")

            if not remission:
                if not cancer and random.randint(0, 14) == 0:
                    cancer = True
                    print(f"\n{name} developed {location} cancer after becoming predisposed to it through Crohn's "
                          f"disease. {name}'s life expectancy has significantly declined. ")
                    ending_age = math.ceil(ending_age * .8)

                elif not gastrointestinal_obstruction and random.randint(0, 9) == 0:
                    gastrointestinal_obstruction = True
                    print(f"\n{name} has a gastrointestinal obstruction in his/her {location} and requires surgery. "
                          f"After surgery, {name} is in remission but has a slightly reduced life expectancy. ")
                    ending_age -= random.randint(0, 2)
                    remission = True

                elif not anemia and random.randint(0, 9) == 0:
                    anemia = True
                    print(f"\n{name} has developed anemia in his/her {location} after becoming predisposed to it "
                          f"through Crohn's disease. {name}'s life expectancy has markedly declined. ")
                    ending_age = math.ceil(ending_age * .9)

                if not tiredness and random.randint(0, 2) == 0:
                    tiredness = True
                    print(f"\n{name} is experiencing tiredness as a symptom of his/her Crohn's disease. ")
                    ending_age -= random.randint(0, 1)

                elif tiredness and not weakness and random.randint(0, 2) == 0:
                    weakness = True
                    print(f"\n{name} is experiencing weakness as a symptom of his/her Crohn's disease. ")
                    ending_age -= random.randint(0, 1)

                if not episcleritis and random.randint(0, 5) == 0:
                    episcleritis = True
                    print(f"\n{name} has developed episcleritis, an inflammatory disease, in his/her eye. ")

                elif episcleritis and not scleritis and random.randint(0, 5) == 0:
                    scleritis = True
                    print(f"\n{name}'s episcleritis has developed into scleritis, a more serious inflammatory disease "
                          f"in his/her eye. ")
                    ending_age -= random.randint(0, 3)

            if not parasite_exposure and random.randint(0, 14) == 0:
                parasite_exposure = True
                print(f"\n{name} was exposed to Trichuris suis, pig whipworm ova, a parasite which increases Crohn's "
                      f"disease patients' immune capabilities to withstand Crohn's disease. {name}'s life expectancy "
                      f"has markedly increased. ")
                ending_age = math.ceil(ending_age * 1.05)

            age += random.randint(1, 4)
        print(f"\n{name} passed away at age {age}. ")
        print(f"\n{name} was particularly susceptible to Crohn's disease due to the following risk factors: ")
        risk_factors = genetics, smoker, nsaids, high_fat, ATG16L1, IRGM, NOD2
        risk_factors_labels = "genetics", "smoking", "non-steroidal anti-inflammatory drug use", "high-fat diet", \
                              "ATG16L1 mutation", "IRGM mutation", "NOD2 mutation"
        for i in range(7):
            if risk_factors[i]:
                print(f" - {risk_factors_labels[i]} ")

        if IL23R:
            print(f"\n{name}'s susceptibility to Crohn's was reduced due to an IL23R harmful mutation. ")

        print(f"\nIn his/her lifetime, {name} developed the following: "
              f"\n - Crohn's disease in his/her {location} ")
        developments = cancer, anemia, gastrointestinal_obstruction, tiredness, weakness, episcleritis, scleritis, \
                       parasite_exposure
        developed_labels = f"{location} cancer", "anemia", f"gastrointestinal obstruction in his/her {location}", \
                           "tiredness", "weakness", "episcleritis", "scleritis", "parasite exposure"
        for i in range(8):
            if developments[i]:
                print(f" - {developed_labels[i]} ")
        simulated = True
        exit()


command = ""
execute("help")
while command != "exit" and not simulated:
    command = input("Enter command here: ")
    execute(command)
