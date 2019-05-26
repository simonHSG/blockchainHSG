Blockchain Project Coding@HSG by Salim Buggle & Simon Hofer
==============================================================
Disclaimer: We used an Udemy course as the foundation for coding this program.

How to run the program:
1. Install all the files in a directory of your choice
2. Open your terminal
3. Set the right directory with: cd [path to directory with the files]
4. Type in the terminal: python node.py
5. Click enter to run the program

How the program works:
- You start from the user perspective of Salim with a balance of 0.00 coins
- You have four main options as a user:
	1: Add a new transaction value -> lets you transfer coins
	2: Mine a new block -> lets you mine a block and rewards you 10 coins
	3: Output the blockchain blocks -> lets you print all the blocks
	4: Check transaction validity -> checks if there are any invalid transactions
	q: quit -> lets you quit the program
- Because you don’t have any blocks mined yet, ‘1: Add a new transaction value’ will not work because of your insufficient balance
- We recommend you start with ‘2’ -> this will add 10.00 coins to your balance
- You can then start a transaction with ‘3’ and enter the recipient (e.g. Simon) as well as the amount (e.g. 5)