Fuckfuck
=========

Fuckfuck is a [Turing complete](http://en.wikipedia.org/wiki/Turing_completeness) [esoteric programming language](http://en.wikipedia.org/wiki/Esoteric_programming_language) based on Spacefuck which is based on Brainfuck.
The commands are those of Brainfuck, but instead of using single characters, Fuckfuck uses a series of "f"s terminated with an "uck" for each command. 

The number of "f"s pre statement represents the action that the Fuckfuck interpreter will perform. 

Why?
----

I was bored, and was joking around with some friends about Spacefuck after attending Zach Holmanns talk at CUSES2014 in which he mentioned the use of profanity in the tech world. Long story short, I made a language full of profanity. FUCK YEAR!

Commands
--------
( *NOTE EACH COMMAND MUST BE TERMINATED* WITH an "uck", kind of like how ';' in C-style languages end statements. For example the . command in Brainfuck is equivilent to fffff, terminated with uck, so . => fffff uck. Please look at the [examples](examples/) )

<table>
	<tr>
		<th>Characters per line</th>
		<th>Brainfuck equivalent</th>
		<th>Effect</th>
	</tr>
	<tr>
		<td>f</td>
		<td>></td>
		<td>Increments the pointer by one.</td>
	</tr>
	<tr>
		<td>ff</td>
		<td><</td>
		<td>Decrements the pointer by one.</td>
	</tr>
	<tr>
		<td>fff</td>
		<td>+</td>
		<td>Increments the value of memory at the pointer.</td>
	</tr>
	<tr>
		<td>ffff</td>
		<td>-</td>
		<td>Decrements the value of memory at the pointer.</td>
	</tr>
	<tr>
		<td>fffff</td>
		<td>.</td>
		<td>Outputs the value of memory at the pointer (encoded as ASCII)</td>
	</tr>
	<tr>
		<td>ffffff</td>
		<td>,</td>
		<td>Gets one byte of input from the input stream and stores it.</td>
	</tr>
	<tr>
		<td>fffffff</td>
		<td>[</td>
		<td>Checks if the memory value at the pointer equals zero. If it does, the interpreter will jump **forward** to the command after the matching *8* command.</td>
	</tr>
	<tr>
		<td>ffffffff</td>
		<td>]</td>
		<td>Checks if the memory value at the pointer is different from zero. If it does, the intepreter will jump **back** to the command after the matching *7* command.</td>
	</tr>
</td>
