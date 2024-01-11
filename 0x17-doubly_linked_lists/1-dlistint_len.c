#include "lists.h"

/**
 * dlistint_len - get the number of linked list
 * @h:header
 *
 * Return: number of nodes.
 */

size_t dlistint_len(const dlistint_t *h)
{
	const dlistint_t *new;
	int counter;

	new = h;
	counter = 0;

	while (new != NULL)
	{
		counter++;
		new = new->next;
	}
	return (counter);
}
