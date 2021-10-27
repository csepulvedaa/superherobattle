# Pelea De Personajes usando SuperHero Api
#### Autor: Crístobal Sepúlveda Alvarez
#### Fecha: Octubre 2021

# Librerias utilizadas

Para ejecutar esta simulación son necesarias las siguientes librerías.

* Numpy
* Colorama
* time
* sys

Para ejecutar los tests:

* unittest
* coverage


Algunas de librerías o módulos pueden venir incluidas dentro de la instalación de Python o ser instaladas con pip.


# Módulo logic
Para ejecutar esta simulación son necesarias las siguientes librerías.
Algunas de librerías o módulos pueden venir incluidas dentro de la instalación de Python.
Este módulo contiene toda la lógica detrás de la simulación de las batallas, contiene la creación de las clases y los métodos para ejecutar las acciones.
Uso
Para ejecutar la simulación se debe ejecutar el siguiente comando:
```
'python battle.py  AcessToken'
```
Con *AccessToken* el token de acceso a SuperHeroApi, para efectos de test se dejó un token de acceso como variable global en el módulo test.
## Clase Character
Contiene los métodos y los stats para representar a un personaje héroe o villano de un team.
La variable filiation coeficient es una bonificación si el personaje es de la misma alineación de su team, de lo contrario es una penalización.

La variable stamina es una variable generada al azar entre 1 y 10, que influye en el calculo de los stats base.
La variable is_alive nos indica si el personaje este disponible para combatir o no, si la variable es falsa el personaje no se encuentra disponible en la lista de personajes disponibles para atacar

## Clase Team
Contiene los métodos y variables de instancia para representar un team.
La variable hero_list es un arreglo de objeto Character que contiene los personajes pertenecientes al team.

La variable aligment contiene la alineación del team.

La variable booleana batteling contiene el estado del team, si no tiene personajes para combatir es False.
Para escoger la alineación del team se escogió un sistema de puntos, donde un personaje Good suma un punto y un personaje bad lo resta, si los puntos al momento de revisar la alineación de todos los personajes son mayores a 0 el team es Good, de lo contrario el team es Bad.

Existen personajes que no se alinean con "good" ni "bad", estos son:

|                 |              |
| --------------- | ------------ |
| Anti-Venom      | Bizarro      |
| Black Flash     | Blackwulf    |
| Brundlefly      | Captain Cold |
| Copycat         | Deadpool     |
| Deathstroke     | Etrigan      |
| Galactus        | Gladiator    |
| Indigo          | Juggernaut   |
| Living Tribunal | Lobo         |
| Man of Miracles | Man-Bat      |
| One-Above-All   | Q            |
| Raven           | Red Hood     |
| Red Hulk        | Robin VI     |
| Sandman         | Sentry       |
| Sinestro        | The Comedian |
| Toad            | Trickster    |
| Venompool       |              |

Los cuales no suman ni restan puntos a la alineación del team.


# Batallas
Para llevar la cuenta si un héroe esta vivo o fuera de combate se lleva un contador de daño, esta decisión de diseño se toma debido que al momento de programar un videojuego se almacena el HP base y el contador de daño con el fin de programar una barra de HP dinámica.

No encontré mucho sentido de que los HP se reiniciaran después de cada ataque, ya que, si debe existir uno o varios héroes/villanos en pie, deben quedar algunos fuera de combate después de ser atacados.
Debido a la forma de calcular el HP, los stats base y los ataques, muchos personajes quedan fuera de combate con un hit si el atacante es beneficiado con un team de su misma alineación.

La lógica de las batallas procede de la siguiente manera, debido a que en una pelea de Super Héroes vs Villanos nunca se sabe lo que puede pasar, tanto el equipo como el héroe o villano atacante son elegidos completamente al azar, así como el ataque a utilizar.

Existe un tiempo de sleep para agregar dinamismo, el cual puede ser removido removiendo o comentando las lineas 44 y 52.

Las batallas proceden de la siguiente manera:

1. Se crean equipos de 5 personajes al azar.
2. Se lanza una moneda (Numero al azar entre 1 y 2) y según el resultado ataca el Team A o el Team B.
3. Para cada team que ataca, se elige al azar un personaje dentro de los que estén habilitados para combatir.
4. Para el team que recibe el daño, se elige al azar un personaje dentro de los que estén habilitados para combatir.
5. Del personaje escogido por el team atacante, se escoge al azar un ataque entre ataque rápido, ataque mental y ataque fuerte.
6. Se agrega al contador de daño el valor del ataque recibido, si este daño es mayor a los HP del personaje este queda fuera de combate, de lo contrario puede seguir atacando en un futuro.
7. Se repiten los pasos 2 al 6 hasta que exista un equipo sin personajes para atacar, este es declarado perdedor de la batalla.

# Testing


Para ejecutar los test sin imprimir en consola utilizar el comando.

```
'coverage run test.py -b'
```

Se testearon las clases del modulo logic obteniendo un 99% de coverage.
Debido a la aleatoriedad del modulo battle y su función de imprimir en consola sin almacenar variables se decidió no aplicar tests.


```
Name       Stmts   Miss  Cover
------------------------------
logic.py     161      2    99%
tests.py     103      0   100%
------------------------------
TOTAL        264      2    99%
```

# Ejemplo de Ejecución

```
Building Team A
Building Team B
----------------------------------------
SuperHero / Villian Status: Team A
 Alive : Human Torch
 Alive : Rip Hunter
 Alive : Goliath
 Alive : Zatanna
 Alive : Yoda
----------------------------------------
SuperHero / Villian Status: Team B
 Alive : Yoda
 Alive : Mandarin
 Alive : Weapon XI
 Alive : Jyn Erso
 Alive : Nebula
----------------------------------------
Battle Turn 1 Team B attacks -> Team A
----------------------------------------
> Yoda Attacks Goliath With a Fast Attack
>> Goliath Took 4.466 Damage
> Human Torch Attacks Nebula With a Strong Attack
>> Nebula Took 1029.818 Damage
Nebula Fainted
----------------------------------------
SuperHero / Villian Status: Team A
 Alive : Human Torch
 Alive : Rip Hunter
 Alive : Goliath
 Alive : Zatanna
 Alive : Yoda
----------------------------------------
SuperHero / Villian Status: Team B
 Alive : Yoda
 Alive : Mandarin
 Alive : Weapon XI
 Alive : Jyn Erso
----------------------------------------
Battle Turn 2 Team B attacks -> Team A
----------------------------------------
> Weapon XI Attacks Goliath With a Strong Attack
>> Goliath Took 116.364 Damage
> Rip Hunter Attacks Yoda With a Strong Attack
>> Yoda Took 216.727 Damage
Yoda Fainted
----------------------------------------
SuperHero / Villian Status: Team A
 Alive : Human Torch
 Alive : Rip Hunter
 Alive : Goliath
 Alive : Zatanna
 Alive : Yoda
----------------------------------------
SuperHero / Villian Status: Team B
 Alive : Mandarin
 Alive : Weapon XI
 Alive : Jyn Erso
----------------------------------------
Battle Turn 3 Team A attacks-> Team B
----------------------------------------
> Goliath Attacks Mandarin With a Fast Attack
>> Mandarin Took 73.636 Damage
> Jyn Erso Attacks Rip Hunter With a Strong Attack
>> Rip Hunter Took 0.011 Damage
----------------------------------------
SuperHero / Villian Status: Team A
 Alive : Human Torch
 Alive : Rip Hunter
 Alive : Goliath
 Alive : Zatanna
 Alive : Yoda
----------------------------------------
SuperHero / Villian Status: Team B
 Alive : Mandarin
 Alive : Weapon XI
 Alive : Jyn Erso
----------------------------------------
Battle Turn 4 Team B attacks -> Team A
----------------------------------------
> Jyn Erso Attacks Human Torch With a Strong Attack
>> Human Torch Took 0.011 Damage
> Zatanna Attacks Mandarin With a Strong Attack
>> Mandarin Took 5994.0 Damage
Mandarin Fainted
----------------------------------------
SuperHero / Villian Status: Team A
 Alive : Human Torch
 Alive : Rip Hunter
 Alive : Goliath
 Alive : Zatanna
 Alive : Yoda
----------------------------------------
SuperHero / Villian Status: Team B
 Alive : Weapon XI
 Alive : Jyn Erso
----------------------------------------
Battle Turn 5 Team A attacks-> Team B
----------------------------------------
> Rip Hunter Attacks Weapon XI With a Mental Attack
>> Weapon XI Took 538.909 Damage
Weapon XI Fainted
> Jyn Erso Attacks Rip Hunter With a Mental Attack
>> Rip Hunter Took 0.011 Damage
----------------------------------------
SuperHero / Villian Status: Team A
 Alive : Human Torch
 Alive : Rip Hunter
 Alive : Goliath
 Alive : Zatanna
 Alive : Yoda
----------------------------------------
SuperHero / Villian Status: Team B
 Alive : Jyn Erso
----------------------------------------
Battle Turn 6 Team B attacks -> Team A
----------------------------------------
> Jyn Erso Attacks Human Torch With a Mental Attack
>> Human Torch Took 0.011 Damage
> Goliath Attacks Jyn Erso With a Mental Attack
>> Jyn Erso Took 73.636 Damage
----------------------------------------
SuperHero / Villian Status: Team A
 Alive : Human Torch
 Alive : Rip Hunter
 Alive : Goliath
 Alive : Zatanna
 Alive : Yoda
----------------------------------------
SuperHero / Villian Status: Team B
 Alive : Jyn Erso
----------------------------------------
Battle Turn 7 Team A attacks-> Team B
----------------------------------------
> Zatanna Attacks Jyn Erso With a Mental Attack
>> Jyn Erso Took 10368.0 Damage
Jyn Erso Fainted
Team A Wins.
```


