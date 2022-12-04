#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

/**
  * freeptr - frees memory alocc pointers
  * @p: pointer arg
  * Return: void
  */
void freeptr(int *p)
{
	free(p);
}
/**
  * is_palindrome - checks if a linked list is a palindrome
  * @head: pointer to the pointer of the list head
  * Return: 1 if is a palindrome; 0 if not
  */
int is_palindrome(listint_t **head)
{
	listint_t *thead = *head;
	int arrlen, x, i = 0;
	int *valptr;

	if (*head == NULL)
		return (1);
	valptr = malloc(1 * sizeof(int));
	if (valptr == NULL)
		return (0);
	valptr[i] = thead->n;
	while (thead->next)
	{
		i++;
		thead = thead->next;
		valptr = realloc(valptr, i * sizeof(int));
		valptr[i] = thead->n;
	}
	for (i = 0; valptr[i]; i++)
	{}
	arrlen = i - 2;
	for (x = 0; x <= arrlen;)
	{
		if (valptr[x++] == valptr[arrlen--])
			continue;
		else
		{
			freeptr(valptr);
			return (0);
		}
	}
	freeptr(valptr);
	return (1);
}
