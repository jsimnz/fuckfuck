Language Spec v2
--------
Proposal for a new language as instigated by [issue #1](https://github.com/jsimnz/fuckfuck/issues/1)

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
