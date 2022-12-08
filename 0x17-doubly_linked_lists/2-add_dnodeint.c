#include "lists.h"

/**
  * add_dnodeint - add new nod at the beginning of the list
  * @head: pointer to the pointer to the head of list
  * @n: inter value of new node
  * Return: pointer to the new node
  */
dlistint_t *add_dnodeint(dlistint_t **head, const int n)
	{
		dlistint_t *new, *thead = *head;

		new = malloc(sizeof(dlistint_t));
		if (new == NULL)
			return (NULL);

		new->n = n;
		new->prev = NULL;

		if (*head == NULL)
		{
			new->next = NULL;
			*head = new;
			return (*head);
		}
		new->next = thead;
		thead->prev = new;
		*head = new;

		return (*head);
	}
