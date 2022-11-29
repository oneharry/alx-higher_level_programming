#include "lists.h"

/**
  * insert_node - inserts a number in a sorted list
  * @head: pointer to pointer of first node of listint_t list
  * @number: integer to be included in new node
  * Return: address of the new element or NULL if it fails
*/
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (current == NULL || current->n >= number)
	{
		new->next = current;
		*head = new;
		return (new);
	}
	while (current && current->next && current->next->n < number)
	{
		current = current->next;
	}
	new->next = current->next;
	current->next = new;

	return (new);
}
