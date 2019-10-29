# Homework 7
For this homework you will be working in your local environment. The templates for this homework are [here](https://github.com/browncs6/Homework7.git). You will need to duplicate this repo (read: [duplicating](https://help.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository)). When creating a new repo (to duplicate to) please name it cs0060-_your-cs-login_-hw7, then set it to be [private](https://help.github.com/en/github/administering-a-repository/setting-repository-visibility#making-a-repository-private). Then complete all your work/testing locally and push to your private repo. Then add the following github usernames as [contributors](https://help.github.com/en/github/setting-up-and-managing-your-github-user-account/inviting-collaborators-to-a-personal-repository) (so we can access your code).

* jnrolfe
* samstronghammer
* leonhardfs
* hershgupta404
* caoruiming
* aninah

__We will need to clone your repo and run your code for grading__.

If you choose to use your personal computer and do not have Python installed, go [here](https://www.python.org/downloads/) and get Python 3._x_._x_ 

_You should do this homework sequentially as the code written in one problem can most likely be used in the next problem._

## 1. `variables.py`

1. Create a variable (_int_) named `myInt` and assign it a value of 1
2. Create a variable (_str_) named `myString` and assign it a value of "Tux"
3. Create a variable (_list_) named `myList` and assign it values of `myInt, myString, 10`
4. Create a variable (_list_) named `my2DList` and assign it 2 copies of `myList`. _E.g._ when printed out, `my2DList` should have a similar structure as something like `[[1,2,3],[1,2,3]]`
5. Create a variable (_dict_) named `myDict` and give it the following (key, value) pairs
  a. `myString` : "is a cool guy"
  b. `myInt` : `myInt`
  c. 'my list' : `myList`
  d. 'some key' : 'some value'

__NOTE__: Do not modify the comments (first 2 lines in the file) or the code under the `if __name__ == "__main__"` block.

## 2. `if_statement.py`
1. Import the [argparse module](https://docs.python.org/2/library/argparse.html)
2. Using `argparse`, create a new parser and add an argument to the parser named 'size' of type `int`.
3. Parse 'size' and assign it to a variable named 'puzzle_size'
4. Create an if statment that multiplies 'puzzle_size' by `-1` if it is negative.
5. Create another if statement that makes sure that puzzle size is both odd and greater than `2`. If "puzzle_size" is even, add one to "puzzle_size" to make it odd.

__NOTE__: Do not modify the comments (first 2 lines in the file) or the code under the `if __name__ == "__main__"` block.

## 3. `function.py`

1. Create a function named "ascii_t" that that takes a parameter named 'puzzle_size'.
2. Make the parameter have a default value of `6`.
3. Write some if statements that ensure 'puzzle_size' is positive, odd, and greater than `2`. If 'puzzle_size' is even, add one to 'puzzle_size' to make it odd. If 'puzzle_size' is negative, multiply it by `-1`; you should still make sure it is greater than `2` though! _hint: you can copy-paste your if statements from the previous problem._
4. Create a nested [for loop](https://www.w3schools.com/python/python_for_loops.asp) that prints makes a "t" of astericks (`*`) where the length and height are equal to "puzzle_size". 
    
    _E.g._ Both `ascii_t(4)` and `ascii_t(5)` should print:
    ```    
           *
           *
       * * * * *
           *
           *
    ```

5. Read about [while loops](https://wiki.python.org/moin/WhileLoop). Why would using a while loop to do the ASCII art task a bad idea? A sentence or two should suffice; turn this in to gradescope.

__NOTE__: Do not modify the comments (first 2 lines in the file) or the code under the `if __name__ == "__main__"` block.

## 4. `more_function.py`
1. Create two functions called "ascii_hline" and "ascii_vline" that take a parameter called 'puzzle_size'. For both functions, use an if statement to insure that 'puzzle_size' is positive and greater than `0`. If 'puzzle_size' is equal to `0` then set it equal to `1`. If 'puzzle_size' is negative, then multiple it by `-1`.
    a. "ascii_hline" use a for loop to print a horizontal line of astericks (`*`) with a length equal to 'puzzle_size'
    b. "ascii_vline" use a for loop to print a vertical line of astericks (`*`) with a length equal to 'puzzle_size'
3. Copy over your `ascii_t` function from the previous problem. Remove the default value of `6` from the 'puzzle_size' parameter.
4. Create a function called "ascii_selector" that has parameters named 'ascii_functions', 'selection', and 'puzzle_size'.
    i. 'ascii_functions' should be a list of functions ("ascii_hline", "ascii_vline", "ascii_t")
    ii. 'selection' should be a string ('hline', 'vline', 't')
    iii. 'puzzle_size' should be an integer.
This function should use 'selection' to select the correct ascii function to call in 'ascii_function' while passing it 'puzzle_size'.
4. Adding to the bottom of the file (under the `if __name__ == "__main__"` block), create a variable (_list_) named 'ascii_functions' containing `ascii_hline`, `ascii_vline`, and `ascii_t`
5. Call your `ascii_selector` function passing 'ascii_functions', 'selection', 'puzzle_size'

## 5. `decorators.py`
