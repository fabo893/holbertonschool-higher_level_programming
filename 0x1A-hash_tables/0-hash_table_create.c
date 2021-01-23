#include "hash_tables.h"

/**
 * *hash_table_create - create a hash table
 * @size - te size of the array
 *
 * Return: On success, a pointer to the newly created hash table
 */
hash_table_t *hash_table_create(unsigned long int size)
{

	hash_table_t *table;

	table = malloc(sizeof(hash_node_t) * size);
	if (table == NULL)
		return (NULL);

	return (table);
}
