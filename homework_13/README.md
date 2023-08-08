## HW: OOP. Class

1. Create add method to add two countries together. This method should create another country object with the name of the two countries combined and the population of the two countries added together.

    ```python
    bosnia = Country('Bosnia', 10_000_000)
    herzegovina = Country('Herzegovina', 5_000_000)

    bosnia_herzegovina = bosnia.add(herzegovina)
    bosnia_herzegovina.population -> 15_000_000
    bosnia_herzegovina.name -> 'Bosnia Herzegovina'
    ```

2. Implement previous method with magic method
    ```python
    bosnia = Country('Bosnia', 10_000_000)
    herzegovina = Country('Herzegovina', 5_000_000)

    bosnia_herzegovina = bosnia + herzegovina
    bosnia_herzegovina.population -> 15_000_000
    bosnia_herzegovina.name -> 'Bosnia Herzegovina'
    ```

3. Create a Car class with the following attributes: brand, model, year, and speed. The Car class should have the following methods: accelerate and brake. The accelerate method should increase the speed by 5, and the brake method should decrease the speed by 5.

4. Create a Robot class with the following attributes: orientation (left, right, up, down), position_x, position_y. The Robot class should have the following methods: move, turn, and display_position. The move method should take a number of steps and move the robot in the direction it is currently facing. The turn method should take a direction (left or right) and turn the robot in that direction. The display_position method should print the current position of the robot.