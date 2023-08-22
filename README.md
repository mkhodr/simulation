<h1><b>Simulation of live "particles".</b></h1>
  <h2>Optimized for +10k simultaneos objects</b></h2>

Our main objective was to model a dynamic environment where particles exhibit behavior resembling real-life entities in search of sustenance.
By simulating this interaction, we aimed to provide insights into how particles navigate their environment to locate and consume food.

<h3>Particle and Food Objects:</h3>
I've designed the simulation with two main types of objects: particles and food.
Each particle possesses attributes such as size, hunger level, and velocity.
Food items are characterized by their nutritional value and position.

<h3>Chasing Mechanism:</h3>
The particles' movement is determined by their size, hunger, and the location of the nearest food item.
Using mathematical calculations, particles adjust their velocity to approach the nearest food source in the shortest way possible.

<h3>Closest Food Calculation:</h3>
I've employed distance-based calculations to determine which food item is closest to each particle.
This process helps particles make informed decisions about their movement direction.

<h3>Visualization:</h3>
A live simulation of the events with the use of python's matplotlib.
The simulation offers real-time visualization of particles' positions and their pursuit of food.
The graphical representation provides an intuitive way to observe and analyze the interaction dynamics.
<br>
<br>

![](https://github.com/mkhodr/simulation/blob/main/500p5000n.gif)
![](https://github.com/mkhodr/simulation/blob/main/100p1000n.gif)
