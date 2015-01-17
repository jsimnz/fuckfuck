Fuckfuck
=========

![logo](https://raw.github.com/jsimnz/fuckfuck/master/doc/rage-meme.jpg)

Fuckfuck is a [Turing complete](http://en.wikipedia.org/wiki/Turing_completeness) [esoteric programming language](http://en.wikipedia.org/wiki/Esoteric_programming_language) based on Spacefuck which is based on Brainfuck.
The commands are those of Brainfuck, but instead of using single characters, Fuckfuck uses a collection of variations of the word "fuck" for each command. 

Why?
----

I was bored, and was joking around with some friends about Spacefuck after attending Zach Holmans talk at CUSES2014 in which he mentioned the flak he recieved for the use of profanity in a previous talk with a slide titled: "Documentation is fucking important". Long story short, I made a language full of profanity. FUCK YEAH!

Commands
--------

<table>
	<tr>
		<th>Syntax</th>
		<th>Brainfuck equivalent</th>
		<th>Effect</th>
	</tr>
	<tr>
		<td>fuck</td>
		<td>></td>
		<td>Increments the pointer by one.</td>
	</tr>
	<tr>
		<td>fuckers</td>
		<td><</td>
		<td>Decrements the pointer by one.</td>
	</tr>
	<tr>
		<td>fuckity</td>
		<td>+</td>
		<td>Increments the value of memory at the pointer.</td>
	</tr>
	<tr>
		<td>fucking</td>
		<td>-</td>
		<td>Decrements the value of memory at the pointer.</td>
	</tr>
	<tr>
		<td>fucked</td>
		<td>.</td>
		<td>Outputs the value of memory at the pointer (encoded as ASCII)</td>
	</tr>
	<tr>
		<td>fuckable</td>
		<td>,</td>
		<td>Gets one byte of input from the input stream and stores it.</td>
	</tr>
	<tr>
		<td>fuckster</td>
		<td>[</td>
		<td>Checks if the memory value at the pointer equals zero. If it does, the interpreter will jump **forward** to the command after the matching *8* command.</td>
	</tr>
	<tr>
		<td>fuckups</td>
		<td>]</td>
		<td>Checks if the memory value at the pointer is different from zero. If it does, the intepreter will jump **back** to the command after the matching *7* command.</td>
	</tr>
</td>
