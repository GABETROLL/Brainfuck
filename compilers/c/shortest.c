#include <stdio.h>

int main(int argc, char **argv)
{
	for (; *(argv[1]) && *(argv[1]) != ']'; argv[1]++)
	{
		if (*(argv[1]) == 43)
			puts("(*p)++;");
		if (*(argv[1]) == 45)
			puts("(*p)--;");
		if (*(argv[1]) == 62)
			puts("p++;");
		if (*(argv[1]) == 60)
			puts("p--;");
		if (*(argv[1]) == 46)
			puts("putchar(*p);");
		if (*(argv[1]) == 44)
			puts("getchar();");
		if (*(argv[1]) == 91)
		{
			puts("while(*p){");
			argv[1]++;
			main(argc, argv);
			puts("}");
		}
	}
	return 0;
}