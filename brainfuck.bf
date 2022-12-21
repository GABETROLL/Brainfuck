DATA STRUCTURE:

pointer code pointer code pointer 0 pointer data pointer data

each 'pointer' is pointing to the element at the right
there can only be one pointer for code and one pointer for data
so only one of each pointer can be a non zero

The 0 is used as a separator for code and data
and is the last char fed in the input code loop below


>>>            0th code cell is going to be empty to keep track of where the start is
,----------
[              Check if input minus 10 is 0; input is new line; to end taking input code
	++++++++++ Add 10 back to input byte
	>>         Move to next code cell
	,          Get input byte
	----------
]

>+      Mark data pointer

<<<[<<] Go back to empty 0th code cell
>       Go to 1st code cell pointer
+       mark code pointer
>       Go to first code character

-------------------------------------------
wasn't plus:
[
	-
	wasn't comma:
	[
		-
		wasn't minus:
		[
			-
			wasn't period:
			[
				--------------
				wasn't left arrow:
				[
					--
					wasn't right arrow:
					[
						-----------------------------
						wasn't left bracket or any bf character:
						[-]
						was left bracket:
						[]
					]
					was right arrow:
					[]
				]
				was left arrow:
				[]
			]
			was period:
			[
				< move to current data cell
				. output

			]
		]
		was minus:
		[
			<<<[->>+<<] copies current data cell to next data cell; assuming next data cell is 0
			>>          moves to new data cell
			-           subtract from data
			<<          move to old data cell to point at a 0 and end the branching process
		]
	]
	was comma:
	[
		<<<[-] delete old cell's data to be replaced
		,      input new data
		[->>+<<] copies current data cell to next data cell; assuming next data cell is 0
		already in old cell; ready to exit nested if statements
	]
]

was plus:

<<<[->>+<<] copies current data cell to next data cell; assuming next data cell is 0
>>          moves to new data cell
+           increment data
<<          move to old data cell to point at a 0 and end the branching process


>>>>>



