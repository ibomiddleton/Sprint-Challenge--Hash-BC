## Interview Questions

Explain in detail the workings of a dynamic array:

* What is the runtime complexity to access an array, add or remove from the front, and add or remove from the back?

- accessing an array is 0(1)

- adding to the front is 0(n^2) because there is nested for loops
- removing from the front is 0(1)

- adding to the back is 0(n)
- removing from the back is 0(n)

* What is the worse case scenario if you try to extend the storage size of a dynamic array?

- It will take 0(n)



Explain how a blockchain is structured. What are the blocks, what is the chain? How is the data organized?

- The chain is the structure that contains all of the transactions recorded.
- The blocks are the links in the chain. They hold the index, timestamp, transactions, proof, and the previous hash.



Explain how proof of work functions. How does it operate. How does this protect the chain from attack. What kind of attack is possible?

Proof of work adds to the end of the chain when people are mining. This can prevent someone from changing a transaction to give themselves more money
because when they change it the hash changes and no longer matches the following blocks so then when you try to share your changed blockchain it will be 
denied because it is a bad hash.