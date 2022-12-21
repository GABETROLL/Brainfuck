#include <stdio.h>

/**
 * parse - Interprets code.
 * @data: pointer to data, similar to the reader in a Turing machine.
 * @code: pointer to current code instruction (all are chars)
 * FAULTY CODE CAN LEAD TO SEGMENTATION FAULTS!!!!
 * Return: 1 if bracket found, 0 if not found, -1 if child parse didn't find a bracket.
 */
char *parse(char **data, char *code)
{
	for (; *code && *code != ']'; code++)
	{
		if (*code == '+') {**data++;}
		if (*code == ',') {}
		if (*code == '-') {**data--;}
		if (*code == '.') {putchar(**data);}
		if (*code == '<') {*data--;}
		if (*code == '>') {*data++;}
		if (*code == '[')
		{
			code = parse(data, code + 1);
			if (*code != ']')
			{
				return (code);
			}
		}
	}
	return (code);
}

int main(int argc, char *argv[])
{
	char data[300];
	char code[];

	if (*parse(&data, code)) {return (1);}

	return (0);
}