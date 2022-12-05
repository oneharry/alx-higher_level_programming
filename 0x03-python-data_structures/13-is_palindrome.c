#include "lists.h"
#include <stddef.h>
#include <stdlib.h>
#include <stdio.h>

/**
  * reverselist - reverse linked list
  * @head: pointer to head of list
  * Return: struct node
  */
listint_t *reverselist(listint_t **head)
{
	listint_t *current = *head;
	listint_t *next, *prev = NULL;

	while (current != NULL)
	{
		next = current->next;
		current->next = prev;
		prev = current;
		current = next;
	}
	*head = prev;
	return (*head);
}
/**
  * is_palindrome - checks if a linked list is a palindrome
  * @head: pointer to the pointer of the list head
  * Return: 1 if is a palindrome; 0 if not
  */
int is_palindrome(listint_t **head)
{
	listint_t *thead, *rev, *mid;
	int x, len = 0;

	if (*head == NULL || (*head)->next == NULL)
		return (1);

	thead = *head;
	while (thead)
	{
		len++;
		thead = thead->next;
	}

	thead = *head;
	for (x = 0; x < (len / 2) - 1; x++)
		thead = thead->next;

	if ((len % 2) == 0 && thead->n != thead->next->n)
		return (0);
	thead = thead->next->next;
	rev = reverselist(&thead);
	mid = rev;

	thead = *head;
	while (rev)
	{
		if (rev->n != thead->n)
			return (0);
		thead = thead->next;
		rev = rev->next;
	}
	reverselist(&mid);

	return (1);
}
