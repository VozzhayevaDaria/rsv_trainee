from figure import Circle, Triangle


if __name__ == '__main__':
    allowed_shapes = {"triangle": Triangle, "circle": Circle}
    while True:
        data = input("Insert the figure and parameters for it using one of those patterns: \n"
                     "triangle *side 1* *side 2* *side 3* \n"
                     "circle *radius* \n")
        shape = data.split(" ")[0]
        params = list(map(int, data.split(" ")[1:]))

        try:
            figure = allowed_shapes[shape](params)
            print(figure.area())
        except KeyError:
            print("The shape wasn't found")


        print(figure.params)



