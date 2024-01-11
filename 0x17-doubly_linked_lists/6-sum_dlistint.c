#include "lists.h"

/**
 * sum_dlistint - get sum of list
 * @head:pointer
 *
 * Return: sum
 */
int sum_dlistint(dlistint_t *head)
{
	dlistint_t *new;
	int sum;

	new = head;
	sum = 0;

	while (new != NULL)
	{
		sum += new->n;
		new = new->next;
	}
	return (sum);
}
