#include <stdio.h>
#include <stdlib.h>

/* for assembly label naming and error message */
int loop_count = 0;
/* for error message */
int line_index = 1;

/**
 * parse_body - Writes to 'output' assembly file all corresponding
 * instructions in 'input' file.
 * If it encounters an EOF or a ']' char, it returns the char
 * to properly verify loop syntax.
 * If its recursive child returns EOF instead of ']',
 * It just keeps returning it to the top to handle the error.
 */
char parse_body(FILE *input, FILE *output)
{
	char current_char = '\0';

	while (current_char != EOF || current_char != ']')
	{
		current_char = fgetc(input);
		switch (current_char)
		{
			// rbx is the array pointer
			case '+':
				fputs("\taddb $1, (%rbx)\n", output);
				break;
			case '-':
				fputs("\tsubb $1, (%rbx)\n", output);
				break;
			case '>':
				fputs("\tinc %rbx\n", output);
				break;
			case '<':
				fputs("\tdec %rbx\n", output);
				break;
			case '.':
				// putchar
				fputs("\tmov $1, %rax\n\tmov $1, %rdi\n\tmov %rbx, %rsi\n\tmov $1, %rdx\n", output);
				break;
			case ',':
				// getchar
				fputs("\tmov $0, %rax\n\tmov $0, %rdi\n\tmov %rbx, %rsi\n\tmov $1, %rdx\n", output);
				break;
			case '[':
				/*
				 * to save current loop count before
				 * the child starts making it go higher:
				 */
				int current_loop_count = loop_count;
				char loop_result;

				fprintf(output, "loop%d:\n", loop_count);
				loop_count++;
				loop_result = parse_body(input, output);

				// stop execution if right bracket wasn't found
				// main function will see the right bracket
				// while it's expecting an EOF, and error.
				if (loop_result != ']')
					return (loop_result);

				fprintf(output, "jmp endloop%d\nendloop%d:\n", current_loop_count, current_loop_count);
				break;
			case '\n':
				line_index++;
				break;
		}
	}

	return (current_char);
}

int main(int argc, char **argv)
{
	FILE *input;
	FILE *output;

	if (argc != 3)
	{
		printf("Usage: %s input_file output_file\n", argv[0]);
		return (1);
	}

	input = fopen(argv[1], "r");
	if (!input)
	{
		fprintf(stderr, "Couldn't read input file.\n");
		return (1);
	}
	output = fopen(argv[2], "w");
	if (!output)
	{
		fprintf(stderr, "Couldn't open/create output file.\n");
	}

	// 30000 byte array in RAM, rbx is the pointer
	fprintf(output, ".global _start\n_start:\n\tpush %%rbp\n\tmov %%rsp, %%rbp\n\tsub $30000, %%rsp\n");

	if (parse_body(input, output) != EOF)
	{
		fprintf(stderr, "Invalid syntax in line %d\n", line_index);
		return (EXIT_FAILURE);
	}
	fprintf(output, "\tleave\n\tmov $60, %%rax\n\tmov $0, %%rdi\n\tsyscall");

	return (EXIT_SUCCESS);
}