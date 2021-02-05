#include "lists.h"

/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: head of the linked list
 *
 * Return: 0 if is not a palindrome, otherwise 1
 */
int is_palindrome(listint_t **head)
{
	int size, half = 0, idx = 0, i;
	listint_t *ls, *ll;

	if (*head == NULL)
		return (1);

	ls = *head;
	for (size = 0; ls != NULL; size++)
		ls = ls->next;
	if (size == 1)
		return (1);

	half = size / 2;
	while (idx <= half)
	{
		ll = ls;
		for (i = 0; i < size; i++)
			ll = ll->next;
		if (ls->n != ll->n)
			return (0);
		ls = ls->next;
		idx++;
		size--;
	}
	return (1);
}
