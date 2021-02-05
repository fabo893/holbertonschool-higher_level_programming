#include "lists.h"
#include <stdlib.h>

/**
 * pal_odd - for odd length
 * @array: array of numbers
 * @size: length of the array
 *
 * Return: 0 if is not palindrome, otherwise 1
 */
int pal_odd(int *array, int size)
{
	int idx, i = 0;

	idx = size - 1;
	size = size / 2;

	while (array[i] == array[idx] && i <= size)
	{
		i++;
		idx--;
	}

	if (i == (size + 1))
		return (1);

	return (0);
}


/**
 * palin_helper - helper for palindrome function
 * @head: head of the linked list
 * @size: length of the linked list
 *
 * Return: 0 if is not palindrome, otherwise 1
 */
int palin_helper(listint_t **head, int size)
{
	int *array, idx, i = 0, odd;
	listint_t *ls;

	array = malloc(sizeof(int) * size);
	if (array == NULL)
		return (0);

	ls = *head;
	for (idx = 0; idx < size; idx++)
	{
		array[idx] = ls->n;
		ls = ls->next;
	}
	if ((size % 2) == 0)
	{
		size = size / 2;
		idx = idx - 1;
		while (array[i] == array[idx] && i < size)
		{
			i++;
			idx--;
		}
		if (i == size)
		{
			free(array);
			return (1);
		}
		free(array);
		return (0);
	}
	odd = pal_odd(array, size);
	free(array);
	return (odd);
}


/**
 * is_palindrome - check if a singly linked list is a palindrome
 * @head: head of the linked list
 *
 * Return: 0 if is not a palindrome, otherwise 1
 */
int is_palindrome(listint_t **head)
{
	int size, res;
	listint_t *ls;

	if (head == NULL)
		return (1);

	ls = *head;
	for (size = 0; ls != NULL; size++)
		ls = ls->next;
	if (size == 1)
		return (1);

	res = palin_helper(head, size);

	if (res == 1)
		return (1);

	return (0);
}
