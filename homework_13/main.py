def name_task(func):
    def wrapper():
        message = f"---- {func.__name__} ----"
        print(message)
        func()
        print(f"{'-'*len(message)}")

    return wrapper


@name_task
def task_1_2():
    from Country import Country

    bosnia = Country("Bosnia", 10_000_000)
    herzegovina = Country("Herzegovina", 5_000_000)

    bosnia_herzegovina_1 = bosnia.add(herzegovina)
    bosnia_herzegovina_2 = bosnia + herzegovina

    print(bosnia_herzegovina_1.population)
    print(bosnia_herzegovina_1.name)

    print(bosnia_herzegovina_2.population)
    print(bosnia_herzegovina_2.name)


@name_task
def task_3():
    from Car import Car

    bugatti_chiron = Car("Bugatti", "Chiron", 2016, 220)

    print(bugatti_chiron)
    print(bugatti_chiron.accelerate())
    print(bugatti_chiron.accelerate())
    print(bugatti_chiron.brake())


@name_task
def task_4():
    from Robot import Robot, Board

    # creating the non-infinite location for robot to move in
    my_board = Board(6, 6)

    # creating the robot on (1, 1)
    my_robot = Robot("down", 1, 1, my_board)
    print(my_robot.display_position())

    my_robot.move(2)
    my_robot.turn("left")
    print(my_robot.display_position())
    ##
    my_robot.turn("right")
    my_robot.move(3)
    ##
    print(my_robot.display_position())
    my_robot.move(1)

    my_robot.turn("left")
    my_robot.move(3)
    print(my_robot.display_position())


if __name__ == "__main__":
    task_1_2()
    task_3()
    task_4()
