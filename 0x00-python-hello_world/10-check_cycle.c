#include "lists.h"

/**
 * check_cycle - checks a singly linked list.
 * @list - pointer.
 * Return: On success, always 0.
 */
int check_cycle(listint_t *list)
{
	listint_t *current = list;
	listint_t *list_aux = current;

	while (current && list_aux && current->next)
	{
		list_aux = list_aux->next;
		current = current->next->next;
		if (current == list_aux)
			return (1);
	}
	return (0);
}
