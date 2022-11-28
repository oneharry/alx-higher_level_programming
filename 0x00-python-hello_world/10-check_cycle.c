#include "lists.h"

/**
  * check_cycle - checks if a linked list has loop
  * @list: pointer to linked list
  * Return: 1 or 0 for true or false
  */
int check_cycle(listint_t *list)
{
	listint_t *first = list;
	listint_t *last = list;

	if (list == NULL)
		return (0);

	while (first && last && last->next)
	{
		first = first->next;
		last = last->next->next;

		if (first == last)
			return (1);
	}
	return (0);
}
