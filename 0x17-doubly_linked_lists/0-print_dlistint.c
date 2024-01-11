#include "lists.h"

/**
 * print_dlistint - print the linkedlsit
 * @h:pointer to head
 * Return: number of nods.
 */

size_t print_dlistint(const dlistint_t *h)
{
	const dlistint_t *new;
	int counter;

	new = h;
	counter = 0;
	while (new != NULL)
	{
		printf("%d\n",new->n);
		new = new->next;
		counter++;
	}
	return (counter);
}
