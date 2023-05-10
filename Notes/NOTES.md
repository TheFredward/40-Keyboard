## Matrix concepts

- Each **key** acts like a ***switch*** in a matrix of rows and columns made up of wires
    - When key is pressed circuit is complete
- A board controller detects this and then it registers the key

<br>

## Detection 

- Keyboard controller will scan all columns, and activate them one at a time
    - Once active the controller detects which rows are activated

<br>

## Multi key presses

- Ghosting can occur, when 3 keys are pressed if you consider the fact that the column + row is complete due to the other detection on the same row
    - This generates a ghost

<br>

## Diodes

- Using diodes in series alleviates the possibility of Ghosting
    - Diodes stop the current from flowing in the wrong direction 
    - The specific diode used is **switching diode** a **1N4148**
