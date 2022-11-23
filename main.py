from craiyon import Craiyon

sel = 0


def generador(input):
    generador = Craiyon()
    result = generador.generate(input)
    result.save_images(input)


print("Welcome to the text-to-image ai built by a 13 years old boy :)")
print("I have 2 modes, single prompt and multi-prompt")

while sel != "1" and sel != "2" and sel != "3":
    sel = input("What do you want to do\n" "[1]Single prompt\n""[2]Multi-prompt\n""[3]Some info\n-->")

if sel == "1":
    prompt = input("What would you like to generate -->")
    print("Images generating, please wait a few seconds (Normally 30-40)...")
    generador(prompt)
    print("Oh! we are done, don`t forget to check your ai folder to see the generated images!")
elif sel == "2":
    print(
        "Welcome to multi prompt mode, this mode basically generates a lot of prompts automatically\n the only thing that you have to do is create a file named input.txt\n and write every prompt you want to automatically generate on each line.")
    print("When you are done, press enter.")
    pause = input()
    file1 = open('input.txt', 'r')
    count = 0

    for line in file1:
        # Explicar lo de input.txt y pulir mas cosas como decir cuando has
        # terminado y decir el tiempo que has tardado ademas de el readme y github y usar el cls
        print('Now printing {}'.format(line.strip()))
        generador(line.strip())

    print("Oh! we are done, don`t forget to check your ai folder to see the generated images!")
elif sel == "3":
    print(
        "Ok, as i said before, im a a 13 years old child that lives in Spain,\n i loved the idea of generating images from nowhere and never seen before\n so i started investigating and found a github repo\n that adapted the craiyon api to python, so i built this, also \n i was bored of the 'tokens' in weird ai webpages so i created the second mode, aimed in creating huge\n amount of images automaticlly.")
