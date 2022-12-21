#include <stdio.h>

int main(int argc, char **argv)
{
	for (; *(argv[1]) && *(argv[1]) != ']'; argv[1]++)
	{
		if (*(argv[1]) == '+')
			puts("(*p)++;");
		if (*(argv[1]) == '-')
			puts("(*p)--;");
		if (*(argv[1]) == '>')
			puts("p++;");
		if (*(argv[1]) == '<')
			puts("p--;");
		if (*(argv[1]) == '.')
			puts("putchar(*p);");
		if (*(argv[1]) == ',')
			puts("getchar(p);");
		if (*(argv[1]) == '[')
		{
			puts("while(*p){");
			argv[1]++;
			main(argc, argv);
			puts("}");
		}
	}
	return 0;
}