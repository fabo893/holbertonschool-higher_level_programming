#include "lists.h"

/**
 * *insert_node - insert a number into a sorted singly linked list
 * @head: double pointer to the head of the list
 * @number: number to be inserted
 *
 * Return: On success, the address of the new node, otherwise NULL
 */
listint_t *insert_node(listint_t **head, int number)
{
	listint_t *h, *new, *next;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;
	new->next = NULL;

	h = *head;
	while (h != NULL)
	{
		if (h->n <= new->n)
		{
			next = h->next;
			if (next != NULL)
				if (next->n > new->n)
				{
					h->next = new;
					new->next = next;
					return (&new);
				}
		}
		h = h->next;
	}
	return (NULL);
}
