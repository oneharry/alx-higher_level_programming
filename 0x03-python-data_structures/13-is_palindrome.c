#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>
/**
  * is_palindrome - checks if a linked list is a palindrome
  * @head: pointer to the pointer of the list head
  * Return: 1 if is a palindrome; 0 if not
  */
int is_palindrome(listint_t **head)
{
	listint_t *thead = *head;
	int arrlen, i = 0;
	int *valptr;

	if (thead == NULL)
		return (0);
	valptr = malloc(1 * sizeof(int));
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
	for (i = 0; i <= arrlen;)
	{
		if (valptr[i++] == valptr[arrlen--])
			continue;
		else
		{
			free(valptr);
			return (0);
		}
	}
	free(valptr);
	return (1);
}
